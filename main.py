import requests
from bs4 import BeautifulSoup
import datetime as dt
import smtplib

EMAIL = "example@gmail.com"
PASSWORD = "password"

# Find a product on Amazon that you want
AMAZON_LINK = "https://www.amazon.ae/link_to_your_item"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
}
# Request the HTML page of the Amazon
response = requests.get(AMAZON_LINK, headers=headers)
# Soup with the web page HTML
amazon_data = BeautifulSoup(response.text, "lxml")
# Get hold of the price of the item
price = amazon_data.find("span", class_="a-offscreen")
float_price = float(price.text[3:])
print(float_price)


# Sending when the price of our product is below a certain value
def send_email(address):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="your_email@yahoo.com", msg=f"Subject:Time to buy item"
                                                                 f"\n\n Hurry up, it's nice price now\n\n")


# set your expected price
if float_price < 149:
    send_email(EMAIL)
