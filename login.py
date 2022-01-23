#!/Python/Python39/python
import cgi
import http.cookies as Cookie
from Database import Database as db
import os

htmlLogin = """
<html>
    <head>
        <title>Login Page</title>
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
        <div class="form-container">
            <form  action="loginCheck.py" method="post">
                <h1>Login</h1>
                <input type="text" placeholder="Username" name="username"/>
                <input type="password" placeholder="Password" name="password"/>
                <button type = "submit" id="signInNow" >Login</button>
            </form>
        </div>
   <button type = "button" style= "position: absolute; top: 30px; right: 25px;" 
    onclick = "window.location.href='index.py'" >Home Page</button>
    <script src="login.js"></script>
    </body>
</html>
"""

print(htmlLogin)
if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cUser = db.get_user_of_the_session(cookie["sessionid"].value)
    db.updateUserLog(cookie["sessionid"].value,-1)
