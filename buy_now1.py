#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()
form = cgi.FieldStorage()
cartid = form.getvalue("cid")
uid = form.getvalue("id")
q = """Select * from userreg where id='%s' """ % (uid)
cur.execute(q)
res = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>Business</title>
    <style>
      .sidenav {
        height: 100%;
        width: 0px;
        position: fixed;
        top: 0;
        left: 0;
        background-color: #111;
        padding-top: 20px;
      }
      .dropdown:hover {
        background-color: white;
        color: black;
      }
      .dropdown {
        color: white;
        padding: 10px 0px 10px 8px;
      }
      .content a {
        text-decoration: none;
        color: white;
        display: block;
        padding: 10px 0px 10px 20px;
      }
      #logo {
        height: 50px;
        width: 50px;
        padding-left: 10px;
      }
      #head {
        color: white;
        font-size: 25px;
        font-family: algerian;
        text-align: center;
      }
      i:hover {
        color: black;
        background-color: white;
        height: 15px;
        width: 30px;
      }
      i {
        color: white;
        text-align: center;
        padding-bottom: 30px;
        height: 20px;
        width: 30px;
      }
      .content a:hover {
        background-color: white;
        color: black;
      }
      .btn {
        color: white;
      }
      .form-group {
        padding: 20px;
      }
      .sell {
        padding: 50px;
        box-shadow: 2px 2px 5px black;
      }
      h1 {
        padding: 30px;
      }
    </style>
  </head>""")

print("""
  <body>
    <div class="row">
      <div class="col-md-2">
        <div class="sidenav">
          <div id="head">
            <i
              class="fa-solid fa-user fa-2xl"
              style="height: auto; width: auto"
            ></i>
            <br />User
          </div>
          <div class="content">
            <a href="user_sell.py?id=%s"><i class="fa-solid fa-shop"></i> Sell Products</a>
            <a href="buy_products.py?id=%s"><i class="fa-solid fa-cart-shopping"></i> Buy Products</a>
            <a href="#?id=%s"><i class="fa-solid fa-list-check"></i> My Orders</a>
            <a href="home.py"><i class="fa-solid fa-right-from-bracket"></i> Logout</a>
          </div>
        </div>
      </div>

      <div class="col-md-10">
        <center>
          <h1>Order Summary</h1>
        </center>
                """ % (uid, uid, uid))

for i in res:
    print("""   
    <div class="sell">
        <form method="post" enctype="multipart/form-data">   
            <h4>Delivery Address</h4>
            <textarea name="delivery" rows="5" cols="30" required>
            Name: %s
            Mobile: %s
            Address: %s
            Pincode: %s</textarea>
            <hr>

            <h4>Payment Option: </h4>
            <input type="radio" value="cash" name="payment" id="payment" required>
            <label for="payment">Cash on Delivery</label>
            <input type="radio" value="Card" name="payment" id="payment" required>
            <label for="payment">Card</label>
            <input type="radio" value="upi" name="payment" id="payment" required>
            <label for="payment">UPI</label><hr>""" % (i[1], i[5], i[6], i[7]))

s = """Select * from user_sell where id='%s' """ % cartid
cur.execute(s)
rec = cur.fetchall()
for j in rec:
    print("""
    <h4>Product Description</h4>
    <div class="row">
    <div class="col-md-2">
    <img src="./images/%s" style="height:100px; width:100px;">
    </div>
        
        </div>
        <label for ="title">Title</label>
        <input type="text" value="%s" name="title"><br>
        <label for ="description">Description</label>
        <input type="text" value="%s" name="description"><br>
        <label for ="price">Price</label>
        <input type="text" value="%s" name="price">
        
        
    """ % (j[6],j[3],j[4],j[5]))


print(""" 
        <hr>   
        <input type="submit" class="btn btn-primary" name="buynow" value="BUY NOW">
        <button class="btn btn-primary" name="cancel"><a href="home.py" style="text-decoration: none; color:white">Cancel</a></button>
          </form>
        </div>
      </div>
    </div>
  </body>
</html>
""")
Title=form.getvalue("title")
Description=form.getvalue("description")
Price=form.getvalue("price")
Payment = form.getvalue("payment")
Product = form.getvalue("product")
Buynow = form.getvalue("buynow")
if Buynow != None:
    q = """INSERT INTO my_orders(uid,payment,title,description,price)values('%s','%s','%s','%s','%s')"""%(uid,Payment,Title,Description,Price)
    cur.execute(q)
    con.commit()
    print("""
        <script>
        alert('Ordered Successfully');
        window.location.href="buy_products.py";
        </script>
        """)

