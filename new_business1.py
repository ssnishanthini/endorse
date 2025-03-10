#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql,cgi,cgitb,random,string

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")

print("""
<!DOCTYPE html>
    <html lang="en">
    <head>
      <title>New User</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
      <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
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
        table{
        margin-top:10px;
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
    <div class="col-md-10">
    <table>
    <tr>
    <th>Name</th>
    <th>Email</th>
    <th>Password</th>
    <th>Gender</th>
    <th>Mobile</th>
    <th>Address</th>
    <th>Photo</th>
""")


q = """Select * from business_reg where status='false'"""
cur.execute(q)
res = cur.fetchall()

for i in res:
    Name = i[1]
    Email = i[2]


    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_chars = random.choices(characters, k=length)
        return ''.join(random_chars)


    # Generate a password
    password = Name[0:2] + Email[1:4] + generate_random_string(2)

    print("""
    <tr>
     <td>%s</td>
     <td>%s</td>
     <td><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal%s">
      Generate
    </button></td>
     <td>%s</td>
     <td>%s</td>
     <td>%s-%s</td>
     <td><img src="./images/%s" style="height:100px; width:100px;"></td>
    """ % (i[1], i[2], i[0], i[4],i[5],i[6],i[7],i[8]))

    print("""
    <!-- The Modal -->
    <div class="modal" id="myModal%s">
      <div class="modal-dialog">
        <div class="modal-content">

          <!-- Modal Header -->
          <div class="modal-header">
            <h4 class="modal-title">Modal Heading</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
          </div>

          <!-- Modal body -->
          <div class="modal-body">
            <form method="post">
              <input type="text" id="password" class="form-control" placeholder="password" name="password" value="%s"><br>

          <!-- Modal footer -->
          <div class="modal-footer">
            <input type="submit" name="submit" class="btn btn-primary" style="width:100px;" value="submit">
            <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
            </form>
          </div>

        </div>
      </div>
    </div>""" % (i[0], password))

Password = form.getvalue("password")
Submit = form.getvalue("submit")
if Submit != None:
    q = """UPDATE business_reg SET password='%s', status='true' WHERE id='%s'""" % (Password, uid)
    cur.execute(q)
    con.commit()
    print("""
    <script>
    alert('Password generated successfully');
    window.location.href="business_login.py";
    </script>
    """)

    print("""
        </table>
        </body>
        </html>
    """)

