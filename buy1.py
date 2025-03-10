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
    <title>Register</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

    <style>
        .header{
            color: black;
            padding-left: 10px;
            height: 90px;
        }
        #head{
            font-family: Mistral;
            font-size: 65px;
        }
        #logo{
          height: 80px;
          width: 50px;
          margin-top: -33px;
        }
        .one{
          text-decoration: none; 
          padding-bottom: 10px;
          color: black;
          margin-top:10px;
        }
        .one:hover{
          color: blue;
        }
        footer{
          background-color: rgb(5, 1, 59);
          color: white;
        }
        .footer{
          text-align: center;
        }


        /* Create three equal columns that floats next to each other */
        .column {
          float: left;
          width: 15.33%;
          padding: 0px;
          background-color: #ccc;
          height: 250px;
        }

        .column a {
          float: none;
          color: black;
          padding: 5px;
          text-decoration: none;
          display: block;
          text-align: left;
        }

        .column a:hover {
          background-color: #ddd;
        }
        .navbar .megamenu{ 
            padding: 1rem; 
        }
        /* Create three equal columns that floats next to each other */
        .column {
          float: left;
          width: 30%;
          padding: 10px;
          background-color: #ccc;
          height: 250px;
        }

        .column a {
          float: none;
          color: black;
          padding: 5px;
          text-decoration: none;
          display: block;
          text-align: left;
        }

        .column a:hover {
          background-color: #ddd;
        }
        nav{
          background-color: rgb(5, 1, 59);
        }
        .nav-item{
          margin-left: 70px;
          color: white;
        }
        .nav-item:hover{
          background-color: rgb(250, 154, 154);
        }
        .nav-link{
          color: white;
        }
        li{
            list-style-type: none;
        }
        @media all and (min-width: 992px) {
        .navbar .has-megamenu{
            position:static!important;
        }
        .navbar .megamenu{
            left:0; right:0; 
            width:100%; 
            margin-top:0;  
        }
        }	
        @media(max-width: 991px){
          .navbar.fixed-top .navbar-collapse, .navbar.sticky-top .navbar-collapse{
            overflow-y: auto;
            max-height: 90vh;
            margin-top:10px;
          }
        }
        .reg{
          box-shadow: 2px 2px 5px black;
          margin: 20px -10px 20px 0px;
          padding: 10px;
          background-color: white;
        }
        .form-control{
          width: 50%;
        }
        .form-group{
          padding: 5px;
        }
        #new{
          box-shadow: 2px 2px 5px black;
          margin: 20px 0px 20px 0px;
          padding: 200px 0px 200px 0px;
        }
        .box{
          box-shadow: 2px 2px 5px black;
          background-color: white;
          margin: 0px 150px 0px 150px;
          border-radius: 30%;
        }

    </style>
</head>
<body>
""")
print("""
            <section>
              <div class="row">
              
                <div class="col-md-2"></div>
                          <div class="col-md-10">
                            <div class="reg">
                            <center>
                            <h1>Order Summary</h1>
                            <center><hr width="90%"></center>
                            <form method="post" enctype="multipart/form-data"> 
                            <div class="form-group">
                                    <textarea class="form-control" placeholder="Address" id="address" name="address" rows="5" required></textarea>
                                </div>
                                
                                <div class="form-group">
                                  <label for="payment">Payment</label>
                                  <input type="radio" id="payment" name="payment" value="upi">
                                  <label for="male">UPI</label>
                                  <input type="radio" id="payment" name="Payment" value="card">
                                  <label for="female">Card</label>
                              </div>
                               
                                <div class="form-group">
                                    <textarea class="form-control" placeholder="Address" id="address" name="address" rows="5" required></textarea>
                                </div>
                              
                            <br>
                                <button input type="submit" class="btn btn-primary" name="register">Register</button>
                                <button class="btn btn-primary" name="cancel"><a href="home.py" style="text-decoration: none; color:white">Cancel</a></button>
                                <center><hr width="90%"></center>
                                <p>If already registered <a href="./userlogin.py" style="font-size: 15px; color: black;">Login</a> yourself.</p>
                            </center>
                            </form>
                            </div>
                            </div>
                            </div>
                            </div>
            </section>
            
              </body>
              </html>
""")

form = cgi.FieldStorage()
Name = form.getvalue("name")
Email = form.getvalue("email")
Password = form.getvalue("password")
Gender = form.getvalue("gender")
Mobile = form.getvalue("mobile")
Address = form.getvalue("address")
Pincode = form.getvalue("pincode")
Register = form.getvalue("register")
if Register != None:
    photo = form['photo']
    fn = os.path.basename(photo.filename)
    open("./documents/" + fn, "wb").write(photo.file.read())
    q = """INSERT INTO userreg(name,email,password,gender,mobile,address,pincode,photo,status)values('%s','%s','%s','%s','%s','%s','%s','%s','false')""" % (
    Name, Email, Password, Gender, Mobile, Address, Pincode, fn)
    cur.execute(q)
    con.commit()
    print("""
    <script>
    alert('Registration Successful');
    window.location.href="userlogin.py";
    </script>
    """)

