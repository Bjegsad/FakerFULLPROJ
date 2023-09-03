import re
import enum

import requests
from bs4 import BeautifulSoup as bs


def get_request(url_template):
    response = requests.get(url_template)
    return bs(response.text.encode("utf-8"), "html.parser")


def ria_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('div', class_='article__text')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


def lenta_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p', class_='topic-body__content-text')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


def kp_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p', class_='sc-1wayp1z-16 dqbiXu')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


def tass_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('span',
                               class_='ds_ext_text-tov6w ds_ext_text--serif-gR6vA ds_ext_text--size_large-KlJUR ds_ext_text--font_weight_regular-sLSOt ds_ext_text--color_primary-iFZIj')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


def interfax_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


def gazeta_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        if "© АО «Газета.Ру»" in paragraph:
            return text
        text += paragraph
    return text


def rbc_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


def mk_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        if '\n' in paragraph:
            continue
        text += paragraph
    return text


def rg_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p')
    articles = soup.find_all('div', class_='PageArticleContent_lead__gvX5C')
    for article in articles:
        article = re.sub(r"\<.*?\>", " ", str(article))
        text += article
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        if 'ФГБУ «Редакция «Российской газеты»' in paragraph:
            break
        text += paragraph
    return text


def kommersant_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p', class_='doc__text')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


def meduza_parser(url_template):
    soup = get_request(url_template)
    text = ""
    paragraphs = soup.find_all('p', class_='article-body__paragraph')
    for paragraph in paragraphs:
        paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
        text += paragraph
    return text


news = [
    'lenta.ru',
    'ria.ru',
    'kp.ru',
    'tass.ru',
    'interfax.ru',
    'gazeta.ru',
    'rbc.ru',
    'mk.ru',
    'rg.ru',
    'meduzanews.ru',
    'kommersant.ru'
]


def parser(url_template):
    for n in news:
        if n in url_template:
            if n == news[0]:
                return lenta_parser(url_template)
            elif n == news[1]:
                return ria_parser(url_template)
            elif n == news[2]:
                return kp_parser(url_template)
            elif n == news[3]:
                return tass_parser(url_template)
            elif n == news[4]:
                return interfax_parser(url_template)
            elif n == news[5]:
                return gazeta_parser(url_template)
            elif n == news[6]:
                return rbc_parser(url_template)
            elif n == news[7]:
                return mk_parser(url_template)
            elif n == news[8]:
                return rg_parser(url_template)
            elif n == news[9]:
                return meduza_parser(url_template)
            elif n == news[10]:
                return kommersant_parser(url_template)
            else:
                return None

# def parser(url_template):
#     for news in News:
#         if news.value[0] in url_template:
#             if news.value[2] is None:
#                 soup = get_request(url_template)
#                 text = ""
#                 paragraphs = soup.find_all(news.value[1], class_=news.value[2])
#                 for paragraph in paragraphs:
#                     paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
#                     # print(paragraph)
#                     text += paragraph
#                 print(text)
#                 return text
#             else:
#                 soup = get_request(url_template)
#                 text = ""
#                 paragraphs = soup.find_all(news.value[1])
#                 for paragraph in paragraphs:
#                     paragraph = re.sub(r"\<.*?\>", " ", str(paragraph))
#                     # print(paragraph)
#                     text += paragraph
#                 print(text)
#                 return text

# #print(ria_parser("https://ria.ru/20230629/kramatorsk-1881023201.html"))
# #print(lenta_parser("https://lenta.ru/news/2023/06/28/hummer/"))
# #print(kp_parser('https://www.kp.ru/daily/27521/4784989/'))
# print(kommersant_parser('https://www.kommersant.ru/doc/6070718?from=top_main_7'))
