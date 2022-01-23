import sqlite3
from datetime import date
from subprocess import STARTF_USESHOWWINDOW


class Database():

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.name= "Database"
    
    @staticmethod
    def userregistration(registrationDetails):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        for i in registrationDetails:
            if i is None:
                return False # not accept is the value is null
        keyUsername = registrationDetails[0]
        isUserExist = c.execute("SELECT username FROM User "
                                "WHERE username = ?",(keyUsername,))
        user = isUserExist.fetchone()
        if user != None:
            return False
        c.execute(
            "INSERT INTO User(username, password, fullname, email, phoneno)VALUES(?,?,?,?,?)", registrationDetails)

        conn.commit()
        conn.close()
        return True

    @staticmethod 
    def authenticationForUser(account):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        keyUsername = account[0]
        keyPassword = account[1]

        ACCOUNT = c.execute("SELECT username,password FROM User WHERE username = ? AND password = ?",
                             (keyUsername, keyPassword,))
        ID = ACCOUNT.fetchall()

        conn.commit()
        conn.close()

        if ID == []:
            return None
        else:
            return ID[0][0]
    
    
    ########## FURKAN #########
    @staticmethod
    def getinternshippositions():
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

    @staticmethod
    def addAdvertisement(ad_details):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        for i in ad_details:
            if i is None:
                return "NoValue"


        id = c.execute("SELECT MAX(houseid) FROM House")

        largestID = id.fetchone()
        largest = largestID[0]
        if largestID[0] == None:
            largest = 1
        else:
            largest = largest+1
        ad_list = []
        ad_list.append(largest)
       # ad_list.extend(houseDetails)

        c.execute(
            "INSERT INTO House(houseid, street, noOfBedrooms, monthlyFee,cityname)VALUES(?,?,?,?,?)",ad_list)
        conn.commit()
        conn.close()
        return "Succesful"
    
    @staticmethod
    def userDetails(userName):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        userExits =c.execute("SELECT username,email,fullname,phoneno FROM User "
                                "WHERE username = ? ",(userName,))

        userInfo = userExits.fetchmany()
        userlist = []
        for i in userInfo[0]:
            userlist.append(i)

        conn.commit()
        conn.close()

        if userInfo == []:
            return "User is not Exist"
        else:
            return userlist



            ########### Log ##########
    @staticmethod
    def addingUserLog(sessionid,username):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO UserLog(sessionid, username)VALUES(?,?)",(sessionid,username,))
        conn.commit()
        conn.close()

    @staticmethod
    def updateUserLog(sessionid,status):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(
            "UPDATE UserLog SET status = ? WHERE sessionid = ?",(status,sessionid,))
        conn.commit()
        conn.close()

    @staticmethod
    def getUserLogStatus(sessionid):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        status = c.execute(
            "SELECT status FROM UserLog WHERE sessionid = ?", (sessionid,))

        sessionStatus = status.fetchone()

        conn.commit()
        conn.close()
        if sessionStatus is not None:
            return sessionStatus[0]
        else:
            return None

    @staticmethod
    def get_user_of_the_session(sessionid):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        user = c.execute(
            "SELECT DISTINCT username FROM UserLog WHERE sessionid = ?", (sessionid,))
        userofSession = user.fetchone()
        conn.commit()
        conn.close()
        if userofSession is not None:
            return userofSession[0]
        else:
            return None

            
            
            ############# Database ############
    @staticmethod
    def checkDatabesExistance():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        flag = False

        # get the count of tables with the name
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='User' ''')

        # if the count is 1, then table exists
        if c.fetchone()[0] == 1:
            flag = True

        # commit the changes to db
        conn.commit()
        # close the connection
        conn.close()
        return flag
 
    @staticmethod
    def databaseInitiation():
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS User(
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    fullname TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phoneno TEXT NOT NULL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS City(
                    cid INTEGER PRIMARY KEY,
                    cname TEXT NOT NULL
                    )""")

        c.execute("""CREATE TABLE IF NOT EXISTS House(
                    houseid INTEGER PRIMARY KEY,
                    street TEXT NOT NULL,
                    noOfBedrooms INTEGER,
                    monthlyFee INTEGER NOT NULL,
                    cityname TEXT NOT NULL,
                    FOREIGN KEY(cityname) REFERENCES City (cname)
                    )""")

        c.execute("""CREATE TABLE UserLog(
                    sesionid TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    status INTEGER DEFAULT 0)""")

        cities = [(1, 'Lefkosa'),
                  (2, 'Girne'),
                  (3, 'GaziMagusa'),
                  (4, 'Iskele'),
                  (5, 'Guzelyurt'),
                  (6, 'Lefke')]

        users = [('hilal',123,'hilalboluk','hilal.boluk@metu.edu.tr','5555555'),
                ('ezgi',1234,'ezgidisbudak','disbudak.ezgi@metu.edu.tr','77777777')]
        houses = []

        c.executemany("INSERT INTO City(cid, cname)VALUES(?, ?)", cities)
        c.executemany(
            "INSERT INTO User(username, password, fullname, email, phoneno)VALUES(?,?,?,?,?)",users)
        c.executemany(
            "INSERT INTO House(houseid,street, noOfBedrooms, monthlyFee, cityname)VALUES(?,?,?,?,?)",houses)

        conn.commit()
        conn.close()


