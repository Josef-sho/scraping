import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "josefsho90@gmail.com"
password = "oxjwqyefxndqbbuf"

respo = requests.get("https://www.jumia.com.ng/freepods-2-2baba-version-true-wireless-earbuds-oraimo-mpg1634823.html")
respo = respo.text

soup = BeautifulSoup(respo, "html.parser")

price = soup.find(name="span", class_="-b -ltr -tal -fs24")
price = price.text.strip('₦').replace(',', '').strip(' ')



if int(price) < 10000:
    with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="josephshodunke4@gmail.com",
                            msg=f"Subject: price drop \n\nthe price of oarimo pods has dropped to ₦10000 go to this link to"
                                f" purchase  https://www.jumia.com.ng/freepods-2-2baba-version-true-wireless-earbuds-ora"
                                f"imo-mpg1634823.html")
else:
    print('sike')
