from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

data = []

url = "https://www.lajornadamaya.mx/k'iintsil/archivo"
data  = requests.get(url).text

soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'
target_a = soup.select('a[href*="2023"]')

for link in target_a:
    print("----------------------------------------------------------------")
    print(link.get('href'))
    new_url = link.get('href')
    new_data  = requests.get(new_url).text
    soup = BeautifulSoup(new_data,"html5lib")
    targets_year = soup.find_all("a", class_="post-headline")
    
    for tag in targets_year:
        new_url = link.get('href')
        new_data  = requests.get(new_url).text
        soup = BeautifulSoup(new_data,"html5lib")

        print('******')
        print(tag.get('href'))
        title = soup.find("a", class_="post-headline").get_text()
        print(title)

        date_p = soup.select(".post-meta p:nth-child(2)")
        print(date_p[0].get_text())

        string = ""  
        content = soup.select(".single-blog-content > p")
        print(content)  # Imprimir título y fech
        for item in content:
            print("item:", item.get_text())  
            string += item.get_text() + "\n"  

        print(string)

df = pd.DataFrame(data, columns=['title', 'date', 'content'])