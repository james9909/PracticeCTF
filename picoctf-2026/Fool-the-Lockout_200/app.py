from flask import Flask, render_template, request, redirect, url_for, session, make_response
import time
import secrets
import json


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

user_db = {}    
""" format ->
    username: "password"
    } 
"""

request_rates = {}
""" format ->
    "ip_addr":{
        "num_requests": int
        "epoch_start": timestamp
        "lockout_until" : int      # -1 if not locked out, timestamp of lockout end
    }
"""

MAX_REQUESTS = 10      # max failed attempts before a user is locked out
EPOCH_DURATION = 30     # timeframe for failed attempts (in seconds)
LOCKOUT_DURATION = 120      # duration a user will be locked out for (in seconds)

RATE_LIMITED_HTML = "<h1>Rate Limited Exceeded</h1><p>You have sent too many requests, requests from your IP will be temporarily blocked.</p>"
 


## ------------------------ HELPER FUNCTIONS ------------------------ ##

"""Quick function to no-cache web page responses"""
def no_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "-1"
    return response


"""Returns true if a user is logged in, false otherwise"""
def logged_in():
    if "user" in session:
        return True
    return False


"""Returns the current user (or None if there is none)"""
def current_user():
    if "user" in session:
        return session["user"]
    return None


"""Add a new user to db"""
def add_new_user(username, password):
    user_db[username] = password
    print("Added (username=%s, password=%s) to user_db" % (username, password))


""" Updates the request rates db for a given client ip, since information will likely be stale."""
def refresh_request_rates_db(client_ip):
    curr_time = time.time()
    if client_ip not in request_rates:
        return
    
    # check if attempt interval has elapsed, if so sets it to 0
    epoch_start_time = request_rates[client_ip]["epoch_start"] 
    if curr_time - epoch_start_time > EPOCH_DURATION:
        request_rates[client_ip]["num_requests"] = 0
        request_rates[client_ip]["epoch_start"] = -1
    
    # if was locked out but period ended update store
    lockout_end = request_rates[client_ip]["lockout_until"]
    if (lockout_end != -1) and time.time() >= lockout_end:
        request_rates[client_ip]["lockout_until"] = -1

   
"""For a given user IP, checks how many requests the user has made (by updating the storage) and if 
the user it has exceeded the assigned rate limit.  Returns true if the user has exceeded rate limit, 
false otherwise. """
def exceeded_rate_limit() -> bool:          # Could do a daemon, but since checks of status are always done before updating its not really necessary
    curr_time = time.time()

    # Grab the IP of the client
    client_ip = request.remote_addr
    print(f"Request ip address: {client_ip}", flush=True)

    # refresh & add new entry to db if it doesnt exist
    refresh_request_rates_db(client_ip)            
    if client_ip not in request_rates:
        request_rates[client_ip] = {
            "num_requests": 0,
            "epoch_start": -1,
            "lockout_until": -1
        }
        print(f"New entry added to db", flush=True)

    # log request if it was a POST
    if request.method == "POST":
        request_rates[client_ip]['num_requests'] += 1
        # if epoch hasnt started, set epoch
        if request_rates[client_ip]['epoch_start'] == -1:
             request_rates[client_ip]['epoch_start'] = curr_time
        print(f"DB updated - {client_ip}:{request_rates[client_ip]}", flush=True)

    # check if we exceeded rate threshold, return True if so
    if request_rates[client_ip]['num_requests'] > MAX_REQUESTS:
        if request_rates[client_ip]["lockout_until"] == -1:
            request_rates[client_ip]['lockout_until'] = curr_time + LOCKOUT_DURATION
            print("Account locked out")
            print(f"DB - {client_ip}:{request_rates[client_ip]}", flush=True)
        return True

    return False


## ------------------------  APP ROUTES ------------------------ ##

""" Login portal """
@app.route("/login", methods=['GET', 'POST'])
def login():
    ## TODO - check rate limit
    if exceeded_rate_limit():
        return RATE_LIMITED_HTML

    # if POST, accept form data and try to add user
    if request.method == "POST":
        user_input = request.form['username']
        pswd_input = request.form['password']
        print("User input: %s, password input: %s" % (user_input, pswd_input))

        # non-existent user or bad password
        if (user_input not in user_db) or (user_db[user_input] != pswd_input):
            msg = f"Invalid username or password."
            return render_template("login.html", error=msg)
        
        # authenticate user
        session["user"] = user_input        
        print("Successfully logged in, session=%s" % (session))
        return redirect(url_for("index"))       # note 'index' refers to the FUNCTION NAME
        
    # return normal page if 'GET'
    return no_cache(make_response(render_template('login.html'))) 


""" Homepage """
@app.route("/", methods=['GET'])
def index():
    if exceeded_rate_limit():
        return RATE_LIMITED_HTML
    
    # authenticate
    if not logged_in():
        return redirect(url_for("login"))
    
     # display homepage according to login
    user = current_user()
    flag = open("/challenge/flag.txt").read().strip()
    return no_cache(make_response(render_template("index.html", user=user, flag=flag)))


""" Logout """
@app.route("/logout", methods=['GET'])
def logout():
    if exceeded_rate_limit():
        return RATE_LIMITED_HTML
    
    if "user" in session:
        session.pop('user', None)
        print("Logged out, popped session")
    return redirect(url_for("login"))


if __name__ == '__main__':
    username, password = None, None
    # get profile data
    try:
        with open("/challenge/profile.json", "r") as file:
            profile = json.load(file)
            username = profile["username"]
            password = profile["password"]
    except Exception as e:
        print(f"Error setting up profile in app:\n{e}")
        exit(1)

    # add new user
    add_new_user(username, password)
   
    # start app
    app.run(host='0.0.0.0', port=8000, debug=True)  