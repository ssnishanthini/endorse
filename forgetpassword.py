#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forget Password</title>
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
          margin_top: 50px;
        }
        .one:hover{
          color: blue;
        }
        .two{
            padding: 100px;
        }
        .form-group{
            padding: 10px;
        }
        .form-control{
            width: 300px;
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
    </style>
    </head>
    <body>
  <header>
    <div class="header">
        <div class="row">
            <div class="col-md-4">
              <img src="./images/logo.jpg" alt="logo" id="logo" style="display: inline-block;">
              <p id="head" style="display: inline-block;">ENDORSE</p>
            </div>
            <div class="col-md-5" ></div>
            <div class="col-md-3">
                <div class="dropdown one" style="display: inline-block;">
                    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="fa-solid fa-right-to-bracket"></i> Login        
                    </button>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="userlogin.py">User Login</a></li>
                      <li><a class="dropdown-item" href="business_login.py">Business Login</a></li>
                    </ul>
                  </div>
                  <div class="dropdown one" style="display: inline-block;">
                    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="fa-solid fa-user"></i> Register
                    </button>
                    <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="userreg.py">User Registration</a></li>
                      <li><a class="dropdown-item" href="business_reg.py">Business Registration</a></li>
                    </ul>
                  </div>             
            </div>    
        </div>
    </div>
</header>

        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container-fluid">
            <!-- <a class="navbar-brand" href="#">Brand</a> -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#main_nav">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="main_nav">
              <ul class="navbar-nav">
                  <li class="nav-item dropdown has-megamenu">
                      <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">All Categories</a>
                      <div class="dropdown-menu megamenu" role="menu">
                       <div class="row">
                      <div class="column">
                          <h5><a href="mobiles.html">Mobile</a></h5>
                          <a href="redmi.html">Redmi</a>
                          <a href="samsung.html">Samsung</a>
                          <a href="oppo.html">Oppo</a>
                          <a href="vivo.html">Vivo</a>
                          <a href="iphone.html">iPhone</a>
                      </div>
                      <div class="column">
                          <h5><a href="electronics.html">Electronics</a></h5>
                          <a href="lap.html">Laptop</a>
                          <a href="tv.html">Tv</a>
                          <a href="camera.html">Camera</a>
      
                      </div>
                      <div class="column">
                          <h5><a href="homeappliances.html">Home Appliances</a></h5>
                          <a href="washing.html">Washing Machine</a>
                          <a href="fridge.html">Refridgerator</a>
                          <a href="ac.html">Air Conditioner</a>
                      </div>
                      <div class="column">
                          <h5><a href="kids.html">Kids</a></h5>
                          <a href="tricycle.html">Tricycle</a>
                          <a href="toys.html">Toy Vehicles</a>
                          <a href="softtoy.html">Soft Toys</a>
                          <a href="puzzle.html">Games Puzzle</a>
                      </div>
                      <div class="column">
                          <h5><a href="sports.html">Sports</a></h5>
                          <a href="crickrt.html">Cricket</a>
                          <a href="Batmiton.html">Batmiton</a>
                          <a href="football.html">Football</a>
                      </div>
                      <div class="column">
                          <h5><a href="books.html">Books</a></h5>
                          <a href="biography.html">Biography</a>
                          <a href="fantasy.html">Fantacy</a>
                          <a href="fiction.html">Hystorical fiction</a>
                      </div>
                      </div>
                      </div>
                      </li>
                      <li class="nav-item"><a class="nav-link" href="home.html">Home </a> </li>
                      <li class="nav-item"><a class="nav-link" href="mobiles.html">Mobile </a></li>
                      <li class="nav-item"><a class="nav-link" href="electronics.html">Electronics </a></li>
                      <li class="nav-item"><a class="nav-link" href="homeappliances.html">Home Appliances </a> </li>
                      <li class="nav-item"><a class="nav-link" href="kids.html">Kids </a></li>
                      <li class="nav-item"><a class="nav-link" href="sports.html">Sports </a></li>
                      <li class="nav-item"><a class="nav-link" href="books.html">Books </a></li>
      
                      </ul>
                      </div>
                  </div>
                  </nav>      

        <section>
            <form method="post" enctype="multipart/form-data">
                <div class="two">
                <center>
                <h2>Forget Password</h2>
                <hr width="80%">
                <div class="form-group">
                    <label for="mail">Enter Mail Id</label>
                    <input type="email" class="form-control" placeholder="Mail id" id="email" name="email" required autofocus>
                </div> 
                    <br>
                    <button class="btn btn-primary" input type="submit" value="submit" name="sub">Submit</button>
                    <button class="btn btn-primary" name="cancel"><a href="home.py" style="text-decoration: none; color:white">Cancel</a></button>

                </div> 
                </center>
                </div>
            </forms>
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
Email = form.getvalue("email")
Submit = form.getvalue("sub")
if Submit != None:
    q = """SELECT `password` FROM `userreg` WHERE `email`='%s';""" % (Email)
    cur.execute(q)
    rec = cur.fetchone()
    con.commit()
    fromadd = 'ssnishanthini2002@gmail.com'
    ppassword = 'ytag jiux dlxu wolt'
    toadd = Email
    subject = "password from askexpert"
    body = "hello expert your password is {}".format(rec)
    msg = """subject:{} \n\n {}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(fromadd, ppassword)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    print("""
        <script>
        alert('Mail sent successfully');
        window.location.href="userlogin.py";
        </script>
        """)

