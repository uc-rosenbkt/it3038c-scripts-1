import requests, re
from bs4 import BeautifulSoup

#The website that is being scraped
data = requests.get("https://www.nike.com/t/lebron-17-low-basketball-shoe-fHcqqM/CD5007-001").content
soup = BeautifulSoup(data, 'html.parser')

#Finding and creating variable for the product title
span = soup.find("h1", {"data-test":"product-title"})
product = span.text

#Finding and creating variable for the price
span = soup.find("div", {"data-test":"product-price"})
price = span.text

#Finding and creating variable for the color shown
span = soup.find("li", {"class":"description-preview__color-description ncss-li"})
color = span.text

#Output of information gathered
print("The %s (%s) has a price of %s." % (product, color, price))
