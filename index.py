#!/Python/Python39/python

import cgi
from Database import Database as db

htmlHeader = """
<html>
    <head>
        <title>Welcome to Rent in North Cyprus</title>
        <link rel="stylesheet" href="common.css">
        
    </head>
    <body>
        <h1 style="	margin: 1em 0 0.5em 0;
        font-weight: bold;
        font-size: 35px;
        color: #520202;
        ">Welcome to Rent in North Cyprus</h1>  
        <button type = "button" onclick = "window.location.href='signUp.py'" > Register</button><br>
        <button type = "button" onclick = "window.location.href='login.py'" > Log In</button>
 """
htmltable = """
        <div class = "tableBox">
            <table id="{tableID}" class= "tableVisual" >
            <tbody>
                
                <tr>
                    <th>Street</th>
                    <th>City</th>
                    <th>Number of Bedrooms</th>
                    <th>Monthly Fee</th>
                    <th>Delete</th>
                </tr>
                
                <tr>
                    <td id={warningID} style="display: none">No available house to rent</td>
                </tr>
"""

htmlrow = """
                <tr> 
                    <td class="myTableHeader"> <a onclick = "window.location.href='housedetails.py?{i[0]}'"> {i[0]}</a></td>
                    <td>{i[2]}</td>
                    <td>{i[3]}</td>
                    <td>{i[4]}</td>
                    <td>{i[5]}</td>
                </tr>
"""

htmlEmpty= """
                <tr> 
                    <td>No available house to rent</td>
                </tr>
"""
htmltableEnd= """
        </tbody>
        </table>
        </div>
"""

htmlend = """
        <script src="search.js"></script>
     </body>
</html>
"""

if not db.checkDatabesExistance():
    db.databaseInitiation()

#i = 0
#houses = db.getinternshippositions()

# lefkosa=[]
# girne=[]
# gazimagusa= []
# iskele= []
# guzelyurt= []
# lefke= []

# for i in houses:
#     if i[-1] == 1:
#         lefkosa.append(i)
#     elif i[-1] == 2:
#         girne.append(i)
#     elif i[-1] == 3:
#         gazimagusa.append(i)
#     elif i[-1] == 4:
#         iskele.append(i)
#     elif i[-1] == 5:
#         guzelyurt.append(i)
#     elif i[-1] == 6:
#         lefke.append(i)


print(htmlHeader)

# cityname= "Gazimagusa"
# tableID= "table" + str(1)
# warningID= "warning" + str(1)
# print(htmltable.format(**locals()))
# if len(gazi)==0:
#     print(htmlEmpty)
# else:
#     for i in gazi:
#         print(htmlrow.format(**locals()))
# print(htmltableEnd)

# cityname= "Girne"
# tableID= "table" + str(2)
# warningID= "warning" + str(2)
# print(htmltable.format(**locals()))
# if len(girne)==0:
#     print(htmlEmpty)
# else:
#     for i in girne:
#         print(htmlrow.format(**locals()))
# print(htmltableEnd)


# cityname= "Guzelyurt"
# tableID= "table" + str(3)
# warningID= "warning" + str(3)
# print(htmltable.format(**locals()))
# if len(guzelyurt)==0:
#     print(htmlEmpty)
# else:
#     for i in guzelyurt:
#         print(htmlrow.format(**locals()))
# print(htmltableEnd)

# cityname= "Iskele"
# tableID= "table" + str(4)
# warningID= "warning" + str(4)
# print(htmltable.format(**locals()))
# if len(iskele)==0:
#     print(htmlEmpty)
# else:
#     for i in iskele:
#         print(htmlrow.format(**locals()))
# print(htmltableEnd)

# cityname= "Lefke"
# tableID= "table" + str(5)
# warningID= "warning" + str(5)
# print(htmltable.format(**locals()))
# if len(lefke)==0:
#     print(htmlEmpty)
# else:
#     for i in lefke:
#         print(htmlrow.format(**locals()))
# print(htmltableEnd)

# cityname= "Lefkosa"
# tableID= "table" + str(6)
# warningID= "warning" + str(6)
# print(htmltable.format(**locals()))
# if len(lefkosa)==0:
#     print(htmlEmpty)
# else:
#     for i in lefkosa:
#         print(htmlrow.format(**locals()))
# print(htmltableEnd)

print(htmlend)
