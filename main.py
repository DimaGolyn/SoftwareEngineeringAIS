import requests
from bs4 import BeautifulSoup

url_n3ws = 'https://habr.com/ru/all/'
response_n3ws = requests.get(url_n3ws).text
data_n3ws = BeautifulSoup(response_n3ws, 'html.parser')

def search_n3ws():
    lis = []
    for article in data_n3ws.find_all('h2', class_ = 'tm-title tm-title_h2')[:10]:
        title = article.a.span.text
        link = 'https://habr.com' + article.a['href']
        lis.append(title + " " + link)
    return lis



url_company3 = 'https://habr.com/ru/companies/'
response_company3 = requests.get(url_company3).text
data_company3 = BeautifulSoup(response_company3, 'html.parser')

def search_company3():
    lis = []
    for article in data_company3.find_all('div', class_='tm-company-snippet__info')[:10]:
        title = article.a.text
        link = 'https://habr.com' + article.a['href']
        lis.append(title + " " + link)
    return lis



url_kitt3ns = 'https://www.google.com/search?q=%D0%9A%D0%BE%D1%82%D1%8F%D1%82%D0%B0&sca_esv=591861726&tbm=isch&sxsrf=AM9HkKkYSy0U2gAPepqxEVmhA1j0Nrz47A:1702908337528&source=lnms&sa=X&ved=2ahUKEwiVh6z0k5mDAxX1LRAIHbpAAbIQ_AUoAXoECAIQAw&biw=1920&bih=919&dpr=1'
response_kitt3ns = requests.get(url_kitt3ns).text
data_kitt3ns = BeautifulSoup(response_kitt3ns, 'html.parser')

def push_kitt3ns():
    lis = []
    for article in data_kitt3ns.find_all('img', class_='DS1iW')[:10]:
        title = article['src']
        lis.append(title)
    return lis