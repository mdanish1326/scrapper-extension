from bs4 import BeautifulSoup
import requests
from mailer import send_mail


def get_details(link,wish_price,user_email):
    
    source = requests.get(link).text
    
    soup = BeautifulSoup(source, 'html.parser')
    prd_name = soup.find('span', class_='B_NuCI').text
    prd_price_str = soup.find('div', class_='_30jeq3 _16Jk6d').text
    prd_price =""
    for i in prd_price_str:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            prd_price += i
    
    print("Product Name: ",prd_name)
    print("Product Price: ",prd_price)
    if int(prd_price) <= wish_price:
        # notify send mail
        print(True)
        send_mail(user_email, prd_name, prd_price,link)
