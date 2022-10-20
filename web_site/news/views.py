from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

# Create your views here.

def news(request):
    return render(request, 'news/news.html')


def page_finance(request):
    data = []
    url = 'https://rg.ru/tema/ekonomika/finansy'
    get = requests.get(url)
    soup = BeautifulSoup(get.text, 'lxml')
    states = soup.find_all('div', class_='PageRubricContent_listItem__rjCcF')
    for stat in states:
        text = stat.find('a', class_='ItemOfListStandard_title__eX0Jw').text
        time = stat.find('a', class_='ItemOfListStandard_datetime__1tmwG').text
        web = 'https://rg.ru/' + stat.find('a', class_='ItemOfListStandard_title__eX0Jw').get('href')
        try:
            img = stat.find('img', class_='ItemOfListStandard_image___sWCo').get('src')
        except AttributeError:
            img = ''
        data.append([time, text, web, img])
    return render(request, 'news/page_finance.html', {'data': data})


def page_europa(request):
    data = []
    url = 'https://rg.ru/tema/mir/Evropa'
    get = requests.get(url)
    soup = BeautifulSoup(get.text, 'lxml')
    states = soup.find_all('div', class_='PageRubricContent_listItem__rjCcF')
    for stat in states:
        text = stat.find('a', class_='ItemOfListStandard_title__eX0Jw').text
        time = stat.find('a', class_='ItemOfListStandard_datetime__1tmwG').text
        web = 'https://rg.ru/' + stat.find('a', class_='ItemOfListStandard_title__eX0Jw').get('href')
        try:
            img = stat.find('img', class_='ItemOfListStandard_image___sWCo').get('src')
        except AttributeError:
            img = ''
        data.append([time, text, web, img])
    return render(request, 'news/page_finance.html', {'data': data})


def page_dayli(request):
    data = []
    url = 'https://rg.ru/tema/obshestvo/prazdniki'
    get = requests.get(url)
    soup = BeautifulSoup(get.text, 'lxml')
    states = soup.find_all('div', class_='PageRubricContent_listItem__rjCcF')
    for stat in states:
        text = stat.find('a', class_='ItemOfListStandard_title__eX0Jw').text
        time = stat.find('a', class_='ItemOfListStandard_datetime__1tmwG').text
        web = 'https://rg.ru/' + stat.find('a', class_='ItemOfListStandard_title__eX0Jw').get('href')
        try:
            img = stat.find('img', class_='ItemOfListStandard_image___sWCo').get('src')
        except AttributeError:
            img = ''
        data.append([time, text, web, img])
    return render(request, 'news/page_dayli.html', {'data': data})


def page_nature(request):
    data = []
    url = 'https://rg.ru/tema/obshestvo/priroda'
    get = requests.get(url)
    soup = BeautifulSoup(get.text, 'lxml')
    states = soup.find_all('div', class_='PageRubricContent_listItem__rjCcF')
    for stat in states:
        text = stat.find('a', class_='ItemOfListStandard_title__eX0Jw').text
        time = stat.find('a', class_='ItemOfListStandard_datetime__1tmwG').text
        web = 'https://rg.ru/' + stat.find('a', class_='ItemOfListStandard_title__eX0Jw').get('href')
        try:
            img = stat.find('img', class_='ItemOfListStandard_image___sWCo').get('src')
        except AttributeError:
            img = ''
        data.append([time, text, web, img])
    return render(request, 'news/page_nature.html', {'data': data})


def page_power(request):
    data = []
    url = 'https://rg.ru/tema/gos/vlast'
    get = requests.get(url)
    soup = BeautifulSoup(get.text, 'lxml')
    states = soup.find_all('div', class_='PageRubricContent_listItem__rjCcF')
    for stat in states:
        text = stat.find('a', class_='ItemOfListStandard_title__eX0Jw').text
        time = stat.find('a', class_='ItemOfListStandard_datetime__1tmwG').text
        web = 'https://rg.ru/' + stat.find('a', class_='ItemOfListStandard_title__eX0Jw').get('href')
        try:
            img = stat.find('img', class_='ItemOfListStandard_image___sWCo').get('src')
        except AttributeError:
            img = ''
        data.append([time, text, web, img])
    return render(request, 'news/page_power.html', {'data': data})


def page_sport(request):
    data = []
    url = 'https://sportrg.ru/tema/sport/raznoe'
    get = requests.get(url)
    soup = BeautifulSoup(get.text, 'lxml')
    states = soup.find_all('div', class_='PageRubricContent_listItem__rjCcF')
    for stat in states:
        text = stat.find('a', class_='ItemOfListStandard_title__eX0Jw').text
        time = stat.find('a', class_='ItemOfListStandard_datetime__1tmwG').text
        web = 'https://rg.ru/' + stat.find('a', class_='ItemOfListStandard_title__eX0Jw').get('href')
        try:
            img = stat.find('img', class_='ItemOfListStandard_image___sWCo').get('src')
        except AttributeError:
            img = ''
        data.append([time, text, web, img])
    return render(request, 'news/page_sport.html', {'data': data})
