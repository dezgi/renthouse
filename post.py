#!/Python/Python39/python
import cgi
import http.cookies as Cookie
from Database import Database as db
import os

ad_list = []

htmlFailed = """
<html>
        <head>
            <title>Post Error</title>  
            <link rel="stylesheet" href="common.css">
        </head>
    <body>
         <h2>Post Error</h2>
         <button type = "button" onclick = "window.location.href='loginCookie.py'" >Back</button>
    </body>
</html>
"""

htmlCookie = """
<html>
        <head>
            <title>Post Error</title>  
            <link rel="stylesheet" href="common.css">
        </head>
    <body>
         <h2>Login Required - Error Code: 121</h2>
         <button type = "button" onclick = "window.location.href='login.py'" >Back</button>
    </body>
</html>
"""

htmlUser = """
      <html>
       <head>
           <title>User</title>  
           <link rel="stylesheet" href="common.css">
       </head>
       <body>
       <h2>Successfully Posted</h2>
       <h3>Position: {ad_list[0]}</h3>
       <h3>Description: {ad_list[1]}</h3>
       <h3>Expectation: {ad_list[2]}</h3>
       <h3>Deadline: {ad_list[3]}</h3>
       <h3>Username: {ad_list[4]}</h3>
       <button type = "button" <a onclick = "window.location.href='loginCookie.py'">Back</a></button>
       </body>
   </html>
"""
cUser=""
if "HTTP_COOKIE" in os.environ:
    cookies = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cUser = str(db.get_user_of_the_session(cookies["sessionid"].value))

    form = cgi.FieldStorage()

    ad_list.append(form.getvalue("street"))
    ad_list.append(form.getvalue('city'))
    ad_list.append(form.getvalue('noofbedrooms'))
    ad_list.append(form.getvalue('monthlyfee'))
    ad_list.append(cUser)

    returnval = db.addAdvertisement(ad_list)
    if returnval == "NullValue":
        print(htmlFailed)
    else:
        print(htmlUser.format(**locals()))

else:
    print(htmlCookie)


