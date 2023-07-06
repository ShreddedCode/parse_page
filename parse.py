import requests
from bs4 import BeautifulSoup

url = 'https://travel.yandex.ru/avia/routes/saint-petersburg--moscow/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
company = soup.find_all('div', class_='EhCXF a-NCA Wu8GK')
price = soup.find_all('span', class_='bQcBE nb3uL')

number_of_companies = 8


def parse():
    for i in range(len(company[:number_of_companies])):
        print(f'{company[i].text} - {price[i].text}')


if __name__ == "__main__":
    parse()
