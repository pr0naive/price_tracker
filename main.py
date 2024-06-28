
import requests
from lxml import html
import smtplib, ssl
import getpass
import time

def get_price():

    #url of the amazon product
    url= "https://www.amazon.in/product_url"
    #Enter your browsers user agent
    headers = {
        'User-Agent':'User-Agent', 'Accept-Encoding': None
    }
    response = requests.get(url, headers= headers)
    tree = html.fromstring(response.content)
    price = tree.xpath('//span[@class="a-price-whole"]/text()')[0]  #Check the name of the price class or id
    return price
    
def send_email(price, password):
    

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "my@gmail.com"  #Sender's email
    reciever_email = "my@gmail.com"
    

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        msg= f'The price of your desired product has dropped to {price}'
        # TODO: Send email here
        server.sendmail(sender_email, sender_email, msg )
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
    
if __name__ == "__main__":
    password = getpass.getpass()
    while(True):
        price = get_price()
        if float(price) < 700:
            send_email(price, password)
        time.sleep(60)