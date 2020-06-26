import urllib.request
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import time


def scanner(url):
    titles = []

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_='VDXfz')

    news_elems = soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb')

    # pprint(page.content)
    for news_elem in news_elems:
        # print(news_elem, end='\n'*2)
        title_elem = news_elem.find('a', class_='DY5T1d')
        # print(title_elem.text)
        titles.append(title_elem.text)

    return titles


def category_picker(topic):
    switcher = {
        1: 'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE',
        2: 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB',
        3: 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB',
        4: 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB',
        5: 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB',
        6: 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB',
        7: 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB',
        8: 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ',
    }
    return switcher.get(topic, "Wrong topic!")


def input_validator(prompt):
    while True:
        value = input(prompt)
        if value not in ('1', '2', '3', '4', '5', '6', '7', '8'):
            print("Sorry, your input is not from 1 to 8. Pick again:")
            continue
        else:
            break
    return int(value)

categories = {
    1: "Country(Users own country)",
    2: "World",
    3: "Business",
    4: "Technology",
    5: "Entertainment",
    6: "Sports",
    7: "Science",
    8: "Health",
}

print("Welcome to the news analyzer".title().strip())
pprint(categories)
category = input_validator("Which category would you like to analyze (1-8):")
print("You picked the topic " + categories[category])
print("Please wait for the program to crawl the web!")
# time.sleep(3)
pprint(scanner(category_picker(category)))
print("A keyword you want links for:")
