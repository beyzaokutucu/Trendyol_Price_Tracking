import requests
from bs4 import BeautifulSoup
from send_email import sendMail
import time

url1="https://www.trendyol.com/mavi/miav-baskili-beyaz-tisort-regular-fit-normal-kesim-1610622-620-p-225019134?boutiqueId=61&merchantId=773357"



def checkPrice(url,paramPrice):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"
    }

    page = requests.get(url, headers=headers)

    htmlPage = BeautifulSoup(page.content,'html.parser')

    productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

    price = htmlPage.find("span",class_="prc-dsc").getText()

    image = htmlPage.find("img", class_="base-product-image")

    convertedPrice = float(price.replace(",",".").replace(" TL",""))

    if(convertedPrice <= 200):
        print("Ürün fiyatı düştü")
        htmlEmailContent= """\
            <html>
            <head></head>
            <body>
            <h3>{0}</h3>
            <br/>
            {1}
            <br/>
            <p>Ürün linki: {2}</p>
            </body>
            </html>
            """.format(productTitle, image, url)
        sendMail("KIME_EMAIL","Ürünün fiyatı düştü👍👍", htmlEmailContent)
    else:
        print("ürün fiyatı düşmedi")

while(True):
    checkPrice(url1,150)
    time.sleep(3)