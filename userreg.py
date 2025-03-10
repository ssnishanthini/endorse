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
    <title> User Register</title>
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
          margin-top:px;
          margin-left: 50px;
          color: white;
        }
        .one:hover{
          background-color: rgb(250, 154, 154);
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
          margin-left: 50px;
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
      <header>
    <div class="header">
        <div class="row">
        <div class="col-md-4" ></div>
            <div class="col-md-4">
              <img src="./images/logo.jpg" alt="logo" id="logo" style="display: inline-block;">
              <p id="head" style="display: inline-block;">ENDORSE</p>
            </div>
            <div class="col-md-4"></div>    
        </div>
    </div>
</header>""")

print("""

    <nav class="navbar navbar-expand-lg navbar-dark">
      <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#main_nav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="main_nav">
        <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="home.py?id=%s">Home </a> </li>
                <li class="nav-item"><a class="nav-link" href="mobiles.py?id=%s">Mobile </a></li>
                <li class="nav-item"><a class="nav-link" href="electronics.py?id=%s">Electronics </a></li>
                <li class="nav-item"><a class="nav-link" href="homeappliances.py?id=%s">Home Appliances </a> </li>
                <li class="nav-item"><a class="nav-link" href="kids.py?id=%s">Kids </a></li>
                <li class="nav-item"><a class="nav-link" href="sports.py?id=%s">Sports </a></li>
                <li class="nav-item"><a class="nav-link" href="books.py?id=%s">Books </a></li>
                <div class="dropdown one" style="display: inline-block;">
                    <button class="btn dropdown-toggle text-light" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="fa-solid fa-right-to-bracket"></i> Login        
                    </button>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="userlogin.py">User Login</a></li>
                      <li><a class="dropdown-item" href="business_login.py">Business Login</a></li>
                      <li><a class="dropdown-item" href="admin_login.py">Admin Login</a></li>
                    </ul>
                  </div>
                  <div class="dropdown one" style="display: inline-block;">
                    <button class="btn dropdown-toggle text-light" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="fa-solid fa-user"></i> Register
                    </button>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="userreg.py">User Registration</a></li>
                      <li><a class="dropdown-item" href="business_reg.py">Business Registration</a></li>
                    </ul>
                  </div>             
                </ul>
                </div>
            </div>
            </nav>
            """)
print("""
            <section>
              <div class="row">
                <div class="col-md-1"></div>
                          <div class="col-md-5">
                            <div class="reg">
                            <center>
                            <h1>Register</h1>
                            <p>Welcome, register yourself here.</p>
                            <center><hr width="90%"></center>
                            <form method="post" enctype="multipart/form-data">
                              <div class="form-group">
                                  <input type="text" class="form-control" placeholder="Name" id="name" name="name" required autofocus>
                                </div>
                                <div class="form-group">
                                    <input type="email" class="form-control" placeholder="Mail id" id="email" name="email" required>
                                </div> 
                                <div class="form-group">
                                    <input type="password" class="form-control" placeholder="Password" id="password" name="password" required>
                                </div> 
                                <div class="form-group">
                                  <label for="gender">Gender</label>
                                  <input type="radio" id="gender" name="gender" value="male">
                                  <label for="male">Male</label>
                                  <input type="radio" id="gender" name="gender" value="female">
                                  <label for="female">Female</label>
                              </div>
                                <div class="form-group">
                                    <input type="tel" class="form-control" placeholder="Mobile no" id="mobile" name="mobile" required>
                                </div>
                                <div class="form-group">
                                    <textarea class="form-control" placeholder="Address" id="address" name="address" required></textarea>
                                </div>
                              <div class="form-group">
                                <input type="tel" class="form-control" placeholder="Pincode" id="pincode" name="pincode" required>
                            </div>
                            <div class="form-group">
                              <label for="Photo" style="display: inline-block;">Photo </label>
                              <input type="file" class="form-control" style="width: 40%; display: inline-block;" placeholder="Photo" id="photo" name="photo" required>
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
                            <div class="col-md-5 bg-secondary" id="new">
                              <div class="box">
                              <center>
                              <img src="./images/logo.jpg" alt="logo" style="height: 100px; width: 100px;">
                              <p id="head">ENDORSE</p>
                            </center>
                            </div>
                            </div>
                            <div class="col-md-1"></div>
                            </div>
                            </div>
            </section>
<footer>
                <div class="footer">
                    <div class="row">
                      <div class="col-md-6" style="padding-top: 20px;">
                        <h5>About Us</h5>
                        <p style="text-align: justify;">Widely known as online classifieds platform, Endorse is all about you. Our aim is to empower every person in the country to independently connect with buyers and sellers online. We care about you - and the transactions that bring you closer to your dreams. Want to buy your first car? We're here for you. Want to sell commercial property to buy your dream home? We're here for you. Whatever job you've got, we promise to get it done.</p>
                      </div>
                        <div class="col-md-6" style="padding-top: 20px;">
                            <img src="./images/logo.jpg" style="display: inline-block; height: 30px;width: 30px;margin-top: -15px;" alt="cakes"> 
                            <h1 style="display: inline-block;font-family: Mistral;">ENDORSE</h1><br>
                            <script>
                                a=new Date();
                                year=a.getFullYear();
                                document.write("Copyrights claimed @ "+year+". All rights reserved.")
                            </script>
                            
                            <center><hr style="width: 80%;"></center>
                            <a>Delhi |</a> <a>Chennai |</a> <a>Banglore |</a> <a>Hydrabad |</a> <a>Mumbai |</a> <a>Koltata |</a> <a>coimbatore |</a> <a>Pune |</a> <a>All cities</a>
                            <br>
              
                            <!-- <h5>Show us some love & connect with us!</h5> -->
                            <a href="https://www.instagram.com/"><i class="fa-brands fa-instagram" style="color: white;"></i></i></a>
                            <a href="https://www.facebook.com/"><i class="fa-brands fa-facebook" style="color: white;"></i></a>
                            <a href="https://twitter.com/?lang=en"><i class="fa-brands fa-twitter" style="color: white;"></i></a>
                            <a href="https://www.youtube.com/"><i class="fa-brands fa-youtube" style="color: white;"></i></a>
                        </div>
                        
                    </div>
                </div>
              </footer> 
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
    q = """INSERT INTO userreg(name,email,password,gender,mobile,address,pincode,photo,status)values('%s','%s','%s','%s','%s','%s','%s','%s','false')""" % (Name, Email, Password, Gender,Mobile, Address, Pincode, fn)
    cur.execute(q)
    con.commit()
    print("""
    <script>
    alert('Registration Successful');
    window.location.href="userlogin.py";
    </script>
    """)

