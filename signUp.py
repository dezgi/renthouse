#!/Python/Python39/python
import cgi
import http.cookies as Cookie
from Database import Database as db
import os

htmlSignUP = """
<html>
    <head>
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
        <div class="form-container">
                <form action="register.py" method="post">
                    <h1>Create Account</h1>
                    <input type="text" placeholder="User Name"  name="username"/>
                    <input type="text" placeholder="Password"  name="password"/>
                    <input type="text" placeholder="Full Name"  name="fullname"/>
                    <input type="text" placeholder="E-Mail"  name="email"/>
                    <input type="text" placeholder="Phone Number"  name="phoneno"/>
                    <button type = "submit" id="signUpNow">Sign Up</button>
                </form>
            </div>
   <button type = "button" style= "position: absolute; top: 30px; right: 25px;" 
    onclick = "window.location.href='index.py'" >Home Page</button>
    <script src="login.js"></script>
    </body>
</html>
"""

print(htmlSignUP)
if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cUser = db.getSessionUsername(cookie["sessionID"].value)
    db.updateLogStatus(cookie["sessionID"].value,-1)
