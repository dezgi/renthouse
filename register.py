#!/Python/Python39/python
from Database import Database as db
import cgi


htmlRegisterSuccessful = """
<html>
    <head>
    <title>Confirm</title>
    <link rel="stylesheet" href="common.css">
    </head>
    <body>
    <h3>Successfully Registered</h3>
    <button type = "button" style= "position: absolute; top: 30px; right: 25px;" 
    onclick = "window.location.href='index.py'" >Home Page</button>
    </body>
</html>

"""
htmlRegisterFailed = """
<html>
    <head>
    <title>Confirm</title>
    <link rel="stylesheet" href="common.css">
    </head>

    <body>
    <h2>Register Error</h2>
    <h3>Please Check Your Username</h3>
    <button type = "button" style= "position: absolute; top: 30px; right: 25px;" 
    onclick = "window.location.href='index.py'" >Home Page</button>
    </body>
</html>

"""
databaseInput = []
form = cgi.FieldStorage()
databaseInput.append(form.getvalue("username"))
databaseInput.append(form.getvalue('password'))
databaseInput.append(form.getvalue('fullname'))
databaseInput.append(form.getvalue('email'))
databaseInput.append(form.getvalue('phoneno'))


if db.userregistration(databaseInput): # if registration is successfull
    print(htmlRegisterSuccessful)

else:# if registration is failed 
    print(htmlRegisterFailed) 






