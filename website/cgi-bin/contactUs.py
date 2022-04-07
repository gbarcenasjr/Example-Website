#!/usr/bin/python
# Import modules for CGI handling
import cgi
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
name = form.getvalue('name')
regarding = form.getvalue('regarding')
phone_number = form.getvalue('phone_number')
email_address = form.getvalue('email_address')
message = form.getvalue('message')

# HTTP Header
print ("Content-type:text/html\r\n\r\n")
#HTTP Body
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Acme Adventure Travel </title>
    <link rel="stylesheet" href="/styles/main.css">
    <meta name="robots" content="noindex">
</head>
<body>
<header>
    <div class="logo">
        <a href="/index.html"><img src="/images/logo_transparent.png" alt="Acme Adventure Logo" width="200"></a>
    </div>
    <nav class="site-nav grid">
        <h1>Acme Adventure Travel</h1>
        <button class="button"
                onclick="window.location.href = '/index.html';">
            Home Page
        </button>
        <button class="button"
                onclick="window.location.href = '/why-travel-with-us.html';">
            Why Travel With Us
        </button>
        <button class="button"
                onclick="window.location.href = '/our-trips.html';">
            Our Trips
        </button>
        <button class="button"
                onclick="window.location.href = '/catalog-request.html';">
            Catalog Requests
        </button>
    </nav>
</header>

<main>
    <hr>
    <article id="mission-statement-result">
        <h2>We'll get back to you soon!</h2>
        <div><strong>Name:</strong> {name}</div>
        <div><strong>Regarding:</strong> {regarding}</div>
        <div><strong>Phone Number:</strong> {phone_number}</div>
        <div><strong>Email Address:</strong> {email_address}</div>
        <div><strong>Message:</strong><br> {message}</div>
        </form>
    </article>
    
</main>

<footer>
    <hr>
    <div id="copyright">
        <p>Copyright © 2021 Acme Adventure Travel, Inc.</p>
    </div>
    <div id="footer-links">
        <button class="button"
                onclick="window.location.href = '/privacy-policy.html';">
            Privacy Policy
        </button>
        <button class="button"
                onclick="window.location.href = '/contact-us.html';">
            Contact Us
        </button>
    </div>
</footer>
</body>
</html>
"""
)