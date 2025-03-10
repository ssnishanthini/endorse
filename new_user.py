#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>User</title>
    <style>
        .sidenav {
            height: 100%;
            width: 170px;
            position: fixed;
            top: 0;
            left: 0;
            background-color: #111;
            padding-top: 20px;
         }
         .dropdown:hover{
            background-color: white;
            color: black;
         }
         .dropdown{
            color:white;
            padding: 10px 0px 10px 8px;

         }
         a{
            text-decoration: none;
            color: white;
            display: block;
            padding: 10px 0px 10px 20px;
        }
        #logo{
            height: 50px;
            width:50px;
            padding-left: 10px;
        }
        #head{
            color: white; 
            font-size: 25px;
            font-family: algerian; 
            text-align: center;
        }
        i:hover{
            color: black;
            background-color: white;
            height:15px;
            width:30px;
        }
        i{
            color: white;
            text-align: center;
            padding-bottom: 30px;
            height:20px;
            width:30px;
        }
        a:hover{
            background-color: white;
            color: black;
        }
        .btn{
            color: white;
        }
        table,th,td{
            border: 1px solid;
            padding: 5px;
        }

    </style>
</head>
<body>
    <div class="row">
        <div class="col-md-2">
            <div class="sidenav">
                <div id="head">
                    <i class="fa-solid fa-user fa-2xl" style="height: auto; width: auto;"></i> <br>Admin
                </div>
                <div class="content">
                <div class="dropdown">
                    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="fa-regular fa-user"></i> Business 
                    </button>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="all_business.py">All Business</a></li>
                      <li><a class="dropdown-item" href="new_business.py">New Business</a></li>
                    </ul>
                  </div>

                <a href="new_user.py"><i class="fa-regular fa-user"></i> User </a>
                <a href="home.py"><i class="fa-solid fa-right-from-bracket"></i> Logout </a>
              </div>
            </div>
            </div>
""")

print("""
<div class="col-md-10">
        <table border="5px">
            <th>Name</th>
            <th>Email Id</th>
            <th>Password</th>
            <th>Gender</th>
            <th>Mobile No</th>
            <th>Address</th>
            <th>Pincode</th>
            <th>Photo</th>

""")

q = """Select * from userreg"""
cur.execute(q)
rec = cur.fetchall()
for i in rec:
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><img src="./images/%s" style="height:100px; width:100px;"></td>""" % (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))

print("""
    </tr>
    </table>
    </div>
    </div>
</body>
</html>
""")