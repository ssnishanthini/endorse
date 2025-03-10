#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe
print("content-type: text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()
form = cgi.FieldStorage()
uid=form.getvalue("id")
q="""Select * from business_reg where id='%s' """%(uid)
cur.execute(q)
res=cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
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
        height: 120vh;
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
        # text-align: center;
    }
    .card{
      box-shadow: 2px 2px 5px black;
      margin: 10px;
    }
    .dropdown .btn:hover{
        background-color: lightgray;

    }
    table,th,td{
            border: 1px solid;
            padding: 5px;
        }
</style>
</head>""")
print("""
<body>
<div class="menu-toggle"></div>
<div class="sidebar">
<ul style="text-decoration: none;">
<div id="head">
<i class="fa-solid fa-user fa-2xl" style="height: auto; width: auto;"></i> <br>User
</div> 
<ul>
<li><a href="user_sell.py?id=%s"><i class="fa-solid fa-shop"></i> Sell Products</a></li>
<li><a href="buy_products.py?id=%s"><i class="fa-solid fa-cart-shopping"></i> Buy Products</a></li>
<li><a href="cart.py?id=%s"><i class="fa-solid fa-list-check"></i> My Orders</a></li>
<li><a href="home.py"><i class="fa-solid fa-right-from-bracket"></i> Logout </a></li>
</ul>
</div>
<div class="content">
<div class="container mt-4">
<div class="row">

""" % (uid, uid, uid))

print("""
    <div class="col-md-10">

        <center>
            <h1>Sell Your Products</h1>
        </center>
        <div class="sell">
            <form method="post" enctype="multipart/form-data">
            <h4><label for="Category">Select Category</label></h4>
            <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" name="category" id="category">
                  <optgroup label="select Category">
                  <option value="mobile">Mobile</option>
                  <option value="electronics">Electronics</option>
                  <option value="home appliances">Home Appliances</option>
                  <option value="kids">Kids</option>
                  <option value="sports">Sports</option>
                  <option value="books">Books</option>
              </optgroup>
              </select>
            <h4><label for="Brand">Select Brand</label></h4>
                      <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" name="brand" id="brand">
                            <optgroup label="Mobiles">
                            <option selected>Select Category</option>
                            <option value="redmi">Redmi</option>
                            <option value="samsung">samsung</option>
                            <option value="oppo">oppo</option>
                            <option value="vivo">vivo</option>
                            <option value="iphone">iPhone</option>
                        </optgroup>
                        <optgroup label="Electronics">
                            <option value="laptop">Laptop</option>
                            <option value="tv">Tv</option>
                            <option value="camera">Camera</option>
                        </optgroup>
                      <optgroup label="Home Appliances">
                        <option value="washing machine">Washing Machine</option>
                        <option value="refridgerator">Refridgerator</option>
                        <option value="air conditionar">Air Conditionar</option>
                      </optgroup>
                      <optgroup label="kids">
                        <option value="tricycle">Tricycle</option>
                        <option value="toy vehicles">Toy Vehicles</option>
                        <option value="soft toys">Soft Toys </option>
                        <option value="games puzzle">Games puzzle</option>
                      </optgroup>
                      <optgroup label="Sports">
                        <option value="cricket">Cricket</option>
                        <option value="batmiton">Batmiton</option>
                        <option value="football">Football</option>
                      </optgroup>
                      <optgroup label="Books">
                        <option value="biography">Biography</option>
                        <option value="fantasy">fantasy</option>
                        <option value="hystorical fiction">Hystorical fiction</option>
                      </optgroup>
                      </select>
                      <div class="form-group">
                        <h4><label for="title">Add Title</label></h4>
                        <input type="text" class="form-control" placeholder="Title" id="title" name="title" required autofocus>
                    </div> 
                    <div class="form-group">
                      <h4><label for="Description">Add Description</label></h4>
                      <textarea class="form-control" placeholder="Description" id="description" name="description" required></textarea>
                    </div>
                    <div class="form-group">
                        <h4><label for="price">Price</label></h4>
                        <input type="text" class="form-control" placeholder="Price" id="price" name="price" required autofocus>
                    </div>
                    <div class="form-group">
                      <h4><label for="photo">Add Image</label></h4>
                      <input type="file" class="form-control" id="photo" name="photo" required >
                    </div> 
                    <br>
                    <center>
                    <button input type="submit" class="btn btn-primary" name="submit">Submit</button>
                    <button class="btn btn-primary" name="cancel"><a href="home.py" style="text-decoration: none; color:white">Cancel</a></button>
                    </center>  
                  </div>
                </form>
                </div>
                </div>
                </body>
                </html>
                """)

Category = form.getvalue("category")
Brand = form.getvalue("brand")
Title = form.getvalue("title")
Description = form.getvalue("description")
Price = form.getvalue("price")
Submit = form.getvalue("submit")

if Submit != None:
    photo = form['photo']
    fn = os.path.basename(photo.filename)
    open("./documents/" + fn, "wb").write(photo.file.read())
    q="""INSERT INTO user_sell(category, brand, title, description, price, photo,sellid)values('%s','%s','%s','%s','%s','%s','%s')"""%(Category, Brand, Title, Description, Price, fn,uid)
    cur.execute(q)
    con.commit()
    print("""
    <script>
    alert('Submitted successfully');
    location.href="user_sell.py?id=%s";
    </script>
    """%(uid))
