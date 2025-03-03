from bs4 import BeautifulSoup
from utils.scraping_helpers import get_html_parser, get_date, get_content, get_title, create_csv

def main (): 
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
    url = "https://www.lajornadamaya.mx/k'iintsil/";
    year = "-2023";
    data = [];
    for month in months:
        url_aux = url + month + year
        soup: BeautifulSoup = get_html_parser(url_aux)
        blogs_url= soup.select(".post-headline")

        for blog_url in blogs_url: 
            blog_url_href = blog_url.get('href')
            print(blog_url_href)
            blog = get_html_parser(blog_url_href)
            title = get_title(blog);
            date = get_date(blog);
            content = get_content(blog);
            data.append([title, date, content]);

    create_csv(data, file_name='data-blog-2023.csv')
    
main()