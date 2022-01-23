#!/Python/Python39/python
import http.cookies as Cookie
from Database import Database as db
import random
import cgi
import string

def randomID():
    string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    choiceStr = ""
    for i in range(3):
        choiceStr = choiceStr + random.choice(string.ascii_letters)
    number = random.randint(1000000, 9999999)
    ID = str(number) + choiceStr
    return ID

htmlHeader = """
<html>
    <head>
        <title>Login User</title>  
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
"""

htmlLoginFailed = """
    <h3 style="align: center">Wrong Username or Password</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br>
    <button type = "button" onclick = "window.location.href='login.py'">Back</button>
"""

htmlSuccessful = """
    <script type="text/javascript">
        window.location = "http://localhost:8080/renthouse/loginCookie.py";
    </script>
"""


form = cgi.FieldStorage()
username_ = form.getvalue("username")
password_ = form.getvalue('password')
liste = [username_, password_]

user = db.authenticationForUser(liste)
sessionID = randomID()

if user is not None:
    cookie = Cookie.SimpleCookie()
    cookie["session"] = sessionID
    cookie["session"]["domain"] = "localhost/"
    cookie["session"]["path"] = "/"
    cookie["sessionID"] = sessionID
    print("Content-type: text/html")
    print("{}".format(cookie.output()))
    print(htmlHeader)
    print(htmlSuccessful)
    db.addLog(sessionID,user)

else:
    print(htmlHeader)
    print(htmlLoginFailed)
print("</body></html>")