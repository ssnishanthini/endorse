#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()
form=cgi.FieldStorage()
uid=form.getvalue("id")
q="""Select * from userreg where id='%s' """%(uid)
cur.execute(q)
res=cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
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
        .card-title{
          text-decoration: none;
        }
        .card-body{
          text-align: center;
        }
        .card{
          margin: 20px;
        
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
        """%(uid, uid, uid, uid, uid, uid, uid))

print("""
<section>
   <!-- Carousel -->
   <div id="demo" class="carousel slide" data-bs-ride="carousel">

  <!-- Indicators/dots -->
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
    <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
    <button type="button" data-bs-target="#demo" data-bs-slide-to="2"></button>
  </div>
  
  <!-- The slideshow/carousel -->
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="./images/slide1.jpg" alt="Los Angeles" class="d-block" style="width:100%" height="500px">
    </div>
    <div class="carousel-item">
      <img src="./images/slide2.jpg" alt="Chicago" class="d-block" style="width:100%" height="500px">
    </div>
    <div class="carousel-item">
      <img src="./images/slide3.webp" alt="New York" class="d-block" style="width:100%" height="500px">
    </div>
  </div>
  
  <!-- Left and right controls/icons -->
  <button class="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
    <span class="carousel-control-next-icon"></span>
  </button>
</div>

<div class="text">
  <center><h4 style="color: hotpink; margin-top: 50px;"><i>The platform allows users to buy and sell products across India.</i></h4>
    <h1 style="line-height: 60px;">Buy and sell new and used products.</h1>
    <P style="margin-bottom: 50px;">The marketplace makes it easier to buy and sell a variety of products and services, including as electronics, mobiles, furniture, household items, books, cars, and bikes.</P>
  </center>
</div>
<hr>
<center>
<h2 style="line-height: 60px;">Get Your Dream Mobiles</h2>
</center>
<div class="row" id="body">""")

print("""  
  <div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
  <a href="mobiles.py?id=%s">
  <div class="card" style="width: 18rem;">
    <center>
    <img class="card-img-top" src="./images/redmi.jpg" alt="Cake" style="height: 200px; width: 150px;">
    </center>
    <div class="card-body">
      <a href="#" class="card-title">Redmi</a>
    </div>
  </div>
  </a>
  </div>"""%(uid))


print(""" 
<div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
<a href="mobiles.py?id=%s">
<div class="card" style="width: 18rem;">
  <center>
  <img class="card-img-top" src="./images/samsung.jpg" alt="Cake" style="height: 200px; width: 150px;">
  </center>
  <div class="card-body">
    <a href="#" class="card-title">Samsung</a>
  </div>
</div>
</a>
</div>"""%(uid))

print("""    
<div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
<a href="./mobiles.py?id=%s">
<div class="card" style="width: 18rem;">
  <center>
  <img class="card-img-top" src="./images/vivo.jpg" alt="Cake" style="height: 200px; width: 150px;">
  </center>
  <div class="card-body">
    <a href="#" class="card-title">Vivo</a>
  </div>
</div>
</a>
</div>"""%(uid))

print("""
<div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
<a href="mobiles.py?id=%s">
<div class="card" style="width: 18rem;">
    <center>
    <img class="card-img-top" src="./images/oppo.jpg" alt="Cake" style="height: 200px; width: 150px;">
    </center>
    <div class="card-body">
      <p class="card-title">Oppo</p>
    </div>
  </div>
  </a>
  </div>
</div>
"""%(uid))

print("""
<hr>
<center>
<h2 style="line-height: 60px;">Toys and Games</h2>
</center>

<div class="row" id="body">""")

print("""
  
  <div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
  <a href="kids.py?id=%s">
  <div class="card" style="width: 18rem;">
    <center>
    <img class="card-img-top" src="./images/chess.jpg" alt="Cake" style="height: 200px; width: 150px;">
    </center>
    <div class="card-body">
      <a href="#" class="card-title">Game Puzzles</a>
    </div>
  </div>
  </a>
  </div>"""%(uid))

print("""
<div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
  <a href="kids.py?id=%s">
<div class="card" style="width: 18rem;">
  <center>
  <img class="card-img-top" src="./images/softtoy.jpg" alt="Cake" style="height: 200px; width: 150px;">
  </center>
  <div class="card-body">
    <a href="#" class="card-title">Soft Toys</a>
  </div>
</div>
</a>
</div>"""%(uid))

print(f"""    
<div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
  <a href="kids.py?id=%s">
<div class="card" style="width: 18rem;">
  <center>
  <img class="card-img-top" src="./images/tricycle.jpg" alt="Cake" style="height: 200px; width: 150px;">
  </center>
  <div class="card-body">
    <a href="#" class="card-title">Tricycle</a>
  </div>
</div>
</a>
</div>"""%(uid))

print("""
<div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
  <a href="kids.py?id=%s">
  <div class="card" style="width: 18rem;">
    <center>
    <img class="card-img-top" src="./images/toy vehicle.jpg" alt="Cake" style="height: 200px; width: 150px;">
    </center>
    <div class="card-body">
      <a href="#" class="card-title">Toy Vehicles</a>
    </div>
  </div>
  </a>
  </div>
</div>""" % (uid))

print("""
<hr>
<div class="text">
  <center><h4 style="color: hotpink; margin-top: 50px;"><i>Cash on delivery avalilable.</i></h4>
    <h1 style="line-height: 60px;">Delivery within a week .</h1>
    <P style="margin-bottom: 50px;">The marketplace makes it easier to buy and sell a variety of products and services, including as electronics, mobiles, furniture, household items, books, cars, and bikes.</P>
  </center>
</div>
<hr>
<center>
  <h2 style="line-height: 60px;">Home & Lifestyle</h2>
  </center>
  
  
  <div class="row" id="body">""")

print("""
    
    <div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
      <a href="homeappliances.py?id=%s">
    <div class="card" style="width: 18rem;">
      <center>
      <img class="card-img-top" src="./images/washing-machine.png" alt="Cake" style="height: 200px; width: 150px;">
      </center>
      <div class="card-body">
        <a href="#" class="card-title">Washing Machine Frontload</a>
      </div>
    </div>
    </a>
    </div>""" % (uid))

print("""    
  <div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
    <a href="homeappliances.py?id=%s">
  <div class="card" style="width: 18rem;">
    <center>
    <img class="card-img-top" src="./images/fridge.png" alt="Cake" style="height: 200px; width: 150px;">
    </center>
    <div class="card-body">
      <a href="#" class="card-title">Refridgerator</a>
    </div>
  </div>
  </a>
  </div>""" % (uid))

print("""            
  <div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
    <a href="homeappliances.py?id=%s">
  <div class="card" style="width: 18rem;">
    <center>
    <img class="card-img-top" src="./images/ac.jpg" alt="Cake" style="height: 200px; width: 150px;">
    </center>
    <div class="card-body">
      <a href="#" class="card-title">Air Conditionar</a>
    </div>
  </div>
  </a>
  </div>""" %(uid))

print("""  
  <div class="col-12 col-sm-6 col-md-6 col-lg-3 col-xl-3">
    <a href="homeappliances.py?id=%s">
    <div class="card" style="width: 18rem;">
      <center>
      <img class="card-img-top" src="./images/topload.jpg" alt="Cake" style="height: 200px; width: 150px;">
      </center>
      <div class="card-body">
        <a href="#" class="card-title">Topload Washing Machine</a>
      </div>
    </div>
    </a>
    </div>
  </div>
</section>""" %(uid))


print("""
<hr>
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


print("""
  <script>
    function myfunction() {
        window.alert("kindly login yourself");
    }
    </script>
""")