import bs4 as bs
import urllib

sauce = urllib.urlopen('https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%204814%20601201888%20601203793%20601204369%20601296707%20601301599&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2').read()

soup = bs.BeautifulSoup(sauce, 'lxml')
containers = soup.findAll("div",{"class":"item-container"})

filename = "Products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:

    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print ("brand:" + brand)
    print ("product_name:" + product_name)
    print ("shipping:" + shipping)

    f.write(brand.replace(",", " ") +","+ product_name.replace(",", "|") +","+ shipping +"\n")

f.close()
