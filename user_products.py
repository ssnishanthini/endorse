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
    <title>Business Products</title>
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
      background-color: #111;
      color: white;
        width: 170px;
        overflow-y: auto;
        height: 180vh;
        padding-top: 20px;
    }
    .sidebar #head{
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 25px;
        font-family: algerian;
        margin: 0;
    }
    .sidebar ul {
        list-style: none;
        padding: 0;

    }
    .sidebar ul li {
        padding: 5px;
        text-align: left;
    }
    .sidebar ul li a {
        color: white;
        text-decoration: none;
        display: block;
        padding: 10px 0px 10px 20px;
        # transition: background-color 0.3s, color 0.3s;
    }
    .sidebar ul li a:hover {
        background-color: white;
        color: black;
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
<div id="head">
<i class="fa-solid fa-user fa-2xl" style="height: auto; width: auto;"></i> <br>Business
</div> 
<ul>
<li><a href="business_sell.py?id=%s"><i class="fa-solid fa-shop"></i> Sell Products</a></li>
<li><a href="business_products.py?id=%s"><i class="fa-solid fa-list-check"></i> My Products</a></li>
<li><a href="orders.py?id=%s"><i class="fa-solid fa-cart-shopping"></i> Orders</a></li>
<li><a href="home.py"><i class="fa-solid fa-right-from-bracket"></i> Logout </a></li>
</ul>
</div>
<div class="content">
<div class="container mt-4">
<div class="row">
""" % (uid, uid, uid))

q = """Select * from user_sell where sellid='%s' """ % (uid)
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

