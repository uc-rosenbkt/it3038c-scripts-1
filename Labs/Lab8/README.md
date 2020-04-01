# Lab 8
This is a lab scraping the price, colorway, and prodcut name of a shoe on nike.com.

## Code to scrape nike.com for the information.
```
data = requests.get("https://www.nike.com/t/lebron-17-low-basketball-shoe-fHcqqM/CD5007-001").content
soup = BeautifulSoup(data, 'html.parser')

span = soup.find("h1", {"data-test":"product-title"})
product = span.text

span = soup.find("div", {"data-test":"product-price"})
price = span.text

span = soup.find("li", {"class":"description-preview__color-description ncss-li"})
color = span.text

print("The %s (%s) has a price of %s." % (product, color, price))
```

## Expected output:
```
python .\C:\it3038c-scripts\Labs\Lab8\Lab8.py
The Lebron 17 Low (Shown: Black/Dark Grey/University Red) has a price of $160.
```
