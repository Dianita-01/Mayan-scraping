from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_html_parser(url: str) -> BeautifulSoup:
    data = requests.get(url).text;
    return BeautifulSoup(data,"html5lib")

def get_title(soup: BeautifulSoup) -> str:
    return soup.find("a", class_="post-headline").get_text()

def get_date(soup: BeautifulSoup) -> str:
    date_p = soup.select(".post-meta p:nth-child(2)")
    return date_p[0].get_text().split("|")[0].strip()

def get_content(soup: BeautifulSoup) -> str:
    content = soup.select(".single-blog-content > p")
    
    return "\n".join(
        item.get_text().strip()
        for item in content
        if item.get_text().strip() 
        and "En español:" not in item.get_text()
        and "Xak'alutskíinsa'an tumen:" not in item.get_text()
    )

def create_csv(data: list, file_name: str) -> None:
    df = pd.DataFrame(data, columns=['title', 'date', 'content'])
    df.to_csv('data.csv', index=False, encoding='utf-8')
