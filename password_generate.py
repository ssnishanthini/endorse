#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql,cgi,cgitb,random,string

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")


q = """SELECT * FROM userreg WHERE id='%s'""" % (uid)
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
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Bootstrap Example</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
      <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <style>
      table,th,td{
            border: 1px solid;
            padding: 5px;
        }
    </style>
    <body>
    <table>
    <tr>
    <th>Name</th>
    <th>Email</th>
    <th>Password</th>
    <th>Gender</th>
    <th>Mobile</th>
    <th>Address</th>
    <th>Photo</th>
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
    q = """UPDATE userreg SET password='%s', status='true' WHERE id='%s'""" % (Password, uid)
    cur.execute(q)
    con.commit()
    print("""
    <script>
    alert('Password generated successfully');
    window.location.href="userlogin.py";
    </script>
    """)

    print("""
        </table>
        </body>
        </html>
    """)

