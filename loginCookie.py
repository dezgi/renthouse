#!/Python/Python39/python
import http.cookies as Cookie
from Database import Database as db
import random
import cgi
import os


htmlHeader = """
<html>
    <head>
        <title>Login User</title>  
        <link rel="stylesheet" href="common.css">
    </head>
    <body>
"""

htmlWrong = """
    <h3 style="align: center">Wrong Username or Password</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br>
    <button type = "button" onclick = "window.location.href='login.py'">Back</button>
"""

htmlSessionError = """
    <h3 style="align: center">Session Error - Error Code: 118</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br>
    <button type = "button" onclick = "window.location.href='login.py'">Back</button>
"""

htmlSessionUserError = """
    <h3 style="align: center">Session User Error  - Error Code: 119</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br>
    <button type = "button" onclick = "window.location.href='login.py'">Back</button>
"""

htmlLoginError = """
    <h3 style="align: center">Login Required  - Error Code: 120</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page</button><br>
    <button type = "button" onclick = "window.location.href='login.py'">Back</button>
"""


htmlCookieError = """
    <h3 style="align: center">Login Required - Error Code: 121</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br>
    <button type = "button" onclick = "window.location.href='login.py'">Back</button>
"""

htmlKeyError = """
    <h3 style="align: center">Key Error - Error Code: 122</h3>
    <button type = "button" onclick = "window.location.href='index.py'" >Home Page </button><br>
    <button type = "button" onclick = "window.location.href='login.py'">Back</button>
"""



htmlNewPosition = """
    <h2>Post your Job</h2>
            <div class="form-container tableBox">
                <form action="post.py" method="post">
                    <h2>Create a Job Position</h2>
                    <span>Fill the blanks</span>
                    <input type="text" placeholder="Position Name"  name="position"/>
                    <input type="text" placeholder="Description" name="description"/>
                    <input type="text" placeholder="Expectation" name="expectation"/>
                    <input type="date" placeholder="Deadline" name="deadline"/>
                    <button type = "submit" id="post">Post</button><br>
                    <button type = "button" onclick = "window.location.href='index.py'">Log Out</button>
                </form>
        </div>
"""

htmltable = """
        <br><br><div class="tableBox">
            <span class="counter pull-right"></span>
            <table class="tableVisual">
                <thead>
                <tr>
                    <th>{userCapital}</th>
                </tr>
                <tr>
                    <th>Position Name</th>
                    <th>Description</th>
                    <th>Expectations</th>
                    <th>Deadline</th>
                </tr>
                </thead>
                <tbody>
"""

htmlrow = """
            <tr> 
                <td>{i[0]}</td>
                <td>{i[1]}</td>
                <td>{i[2]}</td>
                <td>{i[3]}</td>
            </tr>
"""

htmlEmpty= """
                <tr> 
                    <td>No internship position available at the moment</td>
                </tr>
"""
htmltableEnd= """
            </tbody>
        </table>
    </div>
"""


htmlend = """
        </body>
</html>
"""

print("Content-type: text/html")
print(htmlHeader)
if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    try:
        if db.getLogStatus(cookie["sessionID"].value) == -1:
            print(htmlLoginError)
        else:
            cUser = db.getSessionUsername(cookie["sessionID"].value)
            if cUser is None:
                print(htmlSessionUserError)
            else:
                db.updateLogStatus(cookie["sessionID"].value, 1)
                print(htmlNewPosition)
                position = db.getinternshippositionsforacompany(cUser)
                userCapital = cUser.capitalize()
                print(htmltable.format(**locals()))

                if len(position) == 0:
                    print(htmlEmpty)
                else:
                    for i in position:
                        print(htmlrow.format(**locals()))
                    print(htmltableEnd)
    except KeyError:
        print(htmlKeyError)


else:
    print(htmlCookieError)
print(htmlend)



