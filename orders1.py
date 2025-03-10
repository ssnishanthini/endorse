#!C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import cgitb
import pymysql
import smtplib
from email.mime.text import MIMEText

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="endorse")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")

print("Content-type: text/html \r\n\r\n")

# Retrieve business information
q = """SELECT * FROM business_reg WHERE id=%s"""
cur.execute(q, (uid,))
res = cur.fetchall()

# HTML and CSS content
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orders</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
    body, ul {{
        margin: 0;
        padding: 0;
    }}
    body {{
        display: flex;
        justify-content: flex-start;
    }}
    .sidebar {{
      background-color: #111;
      color: white;
        width: 170px;
        overflow-y: auto;
        height: 100vh;
        padding-top: 20px;
    }}
    .sidebar #head{{
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 25px;
        font-family: algerian;
        margin: 0;
    }}
    .sidebar ul {{
        list-style: none;
        padding: 0;
    }}
    .sidebar ul li {{
        padding: 5px;
        text-align: left;
    }}
    .sidebar ul li a {{
        color: white;
        text-decoration: none;
        display: block;
        padding: 10px 0px 10px 20px;
    }}
    .sidebar ul li a:hover {{
        background-color: white;
        color: black;
    }}
    .content {{
        flex-grow: 1;
        padding: 16px;
        transition: 0.3s;
        text-align: center;
    }}
    .card{{
      box-shadow: 2px 2px 5px black;
      margin: 10px;
    }}
    .dropdown .btn:hover{{
        background-color: lightgray;
    }}
    table, th, td {{
        border: 1px solid;
        padding: 5px;
    }}
</style>
</head>
<body>
<div class="menu-toggle"></div>
<div class="sidebar">
<ul>
<div id="head">
<i class="fa-solid fa-user fa-2xl"></i> <br>Business
</div> 
<ul>
<li><a href="business_sell.py?id={uid}"><i class="fa-solid fa-shop"></i> Sell Products</a></li>
<li><a href="business_products.py?id={uid}"><i class="fa-solid fa-list-check"></i> My Products</a></li>
<li><a href="orders.py?id={uid}"><i class="fa-solid fa-cart-shopping"></i> Orders</a></li>
<li><a href="home.py"><i class="fa-solid fa-right-from-bracket"></i> Logout </a></li>
</ul>
</div>
<div class="content">
<div class="container mt-4">
<div class="row">
""")

print("""
<div class="col-md-10">
    <table border="5px">
        <tr>
            <th>Payment</th>
            <th>Title</th>
            <th>Description</th>
            <th>Price</th>
            <th>Buyer Name</th>
            <th>Buyer Mobile</th>
            <th>Buyer Email</th>
            <th>Buyer Address</th>
            <th>Accept</th>
        </tr>
""")

# Retrieve orders
q = """SELECT * FROM my_orders WHERE sellid = %s"""
cur.execute(q, (uid,))
rec = cur.fetchall()
for i in rec:
    print(f"""
    <tr>
        <td>{i[3]}</td>
        <td>{i[4]}</td>
        <td>{i[5]}</td>
        <td>{i[6]}</td>
        <td>{i[8]}</td>
        <td>{i[9]}</td>
        <td>{i[10]}</td>
        <td>{i[11]}</td>
        <td>
            <form action="/cgi-bin/confirm_order.py" method="post">
                <input type="hidden" name="order_id" value="{i[0]}">
                <input type="hidden" name="buyer_email" value="{i[10]}">
                <input type="hidden" name="seller_id" value="{uid}">
                <input type="submit" class="btn btn-primary" value="Accept Order" name="submit">
            </form>
        </td>
    </tr>
    """)

print("""
    </table>
    </div>
    </div>
</div>
</body>
</html>
""")

# If the form is submitted, send the email
submit = form.getvalue("submit")
if submit:
    order_id = form.getvalue("order_id")
    buyer_email = form.getvalue("buyer_email")

    # Email content
    from_address = 'your_email@example.com'
    password = 'your_password'
    to_address = buyer_email
    subject = "Your Order is Confirmed"
    body = f"Your order with ID {order_id} has been confirmed."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
        print("""
            <script>
            alert('Mail sent successfully');
            window.location.href="orders.py?id={uid}";
            </script>
        """)
    except Exception as e:
        print(f"""
            <script>
            alert('Failed to send email: {e}');
            window.location.href="orders.py?id={uid}";
            </script>
        """)
