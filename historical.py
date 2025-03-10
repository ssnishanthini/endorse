#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
q = """Select * from userreg where id='%s' """ % (uid)
cur.execute(q)
res = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historical Fiction</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
    body, ul {
        margin: 0;
        padding: 0;
    }
    body {
        display: flex;
        justify-content: flex-start;
    }
    .sidebar {
      background-color: white;
      color: black;
        width: 250px;
        overflow-y: auto;
        height: 100vh;
    }
    .sidebar h2 {
        color: black;
        text-align: center;
        padding: 10px;
        margin: 0;
        font-size: 20px;
    }
    .sidebar ul {
        list-style: none;
        padding: 0;
        font-size:20px;
    }
    .sidebar ul li {
        padding: 5px;
        text-align: left;
    }
    .sidebar ul li a {
        color: black;
        text-decoration: none;
        display: block;
        transition: background-color 0.3s, color 0.3s;
    }
    .sidebar ul li a:hover {
        background-color: grey;
        color: white;
    }
    .content {
        flex-grow: 1;
        padding: 16px;
        transition: 0.3s;
        text-align: center;
    }
    .card{
      box-shadow: 2px 2px 5px black;
      margin: 10px;
    }
    .dropdown .btn:hover{
        background-color: lightgray;

    }
</style>
</head>
<body>
<div class="menu-toggle"></div>
<div class="sidebar">
<ul style="text-decoration: none;">
<h2 style="margin-bottom: 20px;">Category</h2> 
<div class="dropdown">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
         Mobiles 
    </button>
    <ul class="dropdown-menu">
      <li><a href="redmi.py?id=%s">Redmi</a></li>
      <li><a href="samsung.py?id=%s">Samsung</a></li>
      <li><a href="oppo.py?id=%s">Oppo</a></li>
      <li><a href="vivo.py?id=%s">Vivo</a></li>
      <li><a href="iphone.py?id=%s">iPhone</a></li>
    </ul>
  </div> <hr> 
  <div class="dropdown">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
         Electronics 
    </button>
    <ul class="dropdown-menu">
      <li><a href="lap.py?id=%s">Laptop</a></li>
      <li><a href="tv.py?id=%s">Tv</a></li>
      <li><a href="camera.py?id=%s">Camera</a></li>
    </ul>
  </div><hr>
  <div class="dropdown">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
         Home Appliances
    </button>
    <ul class="dropdown-menu">
      <li><a href="washing.py?id=%s">Washing Machine</a></li>
      <li><a href="fridge.py?id=%s">Refridgerator</a></li>
      <li><a href="ac.py?id=%s">Air Conditionar</a></li>
    </ul>
  </div><hr>
  <div class="dropdown">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
         Kids
    </button>
    <ul class="dropdown-menu">
      <li><a href="tricycle.py?id=%s">Tricycle</a></li>
      <li><a href="toys.py?id=%s">Toy Vehicle</a></li>
      <li><a href="softtoy.py?id=%s">Soft Toys</a></li>
      <li><a href="puzzle.py?id=%s">Game Puzzles</a></li>
    </ul>
  </div><hr>
  <div class="dropdown">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
         Sports
    </button>
    <ul class="dropdown-menu">
      <li><a href="crickrt.py?id=%s">Cricket</a></li>
      <li><a href="Batmiton.py?id=%s">Batmiton</a></li>
      <li><a href="football.py?id=%s">Football</a></li>
    </ul>
  </div><hr>
  <div class="dropdown">
    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
         Books
    </button>
    <ul class="dropdown-menu">
      <li><a href="biography.py?id=%s">Biography</a></li>
      <li><a href="fantasy.py?id=%s">Fantasy</a></li>
      <li><a href="historical.py?id=%s">Historical</a></li>
    </ul>
  </div><hr> 
</div>
<div class="content">
<div class="container mt-4">
<div class="row">
""" % (uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid, uid,))

q = """Select * from user_sell where brand='Hystorical fiction' """
cur.execute(q)
rec = cur.fetchall()
for i in rec:
    print("""
            <div class="col-md-4">
            <div class="card" style="width: 18rem;">
              <img class="card-img-top" src="./documents/%s" alt="mobile" height="200px">
              <div class="card-body">
                <h5 class="card-title">%s</h5>
                <p class="card-text">%s</p>
                <p class="card-text">Starting from<br><b>Rs.%s</b></p>
                <a href="buy_now.py?id=%s&cid=%s" class="btn btn-primary">Buy Now</a>
              </div>
            </div>
            </div>
    """ % (i[6], i[3], i[4], i[5], uid, i[0]))

print(""" 
</div>
</div>
</div>
</body>
</html>
""")

