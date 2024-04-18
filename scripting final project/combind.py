import requests
from bs4 import BeautifulSoup
import pdfkit
from PIL import Image,ImageFilter
import io
import random
import json
import datetime

def season():
    # Determine the current season
    current_month = datetime.datetime.now().month
    if 3 <= current_month <= 5:  # Spring (March, April, May)
        return "spring"
    elif 6 <= current_month <= 8:  # Summer (June, July, August)
        return "summer"
    elif 9 <= current_month <= 11:  # Autumn (September, October, November)
        return "autumn"
    else:  # Winter (December, January, February)
        return "winter"

def breakfast():
    current_season = season()
    if current_season == 'spring':
        scrap('gateau-sale')
    elif current_season == 'summer':
        scrap('henakisoa-sy-anamadinika')
    elif current_season == 'autumn':
        scrap('fromage-de-tete')
    elif current_season == 'winter':
        scrap('flan-patissier-fait-maison')

def lunch():
    current_season = season()
    if current_season == 'spring':
        scrap('hom-bao-na-brioche-chinois')
    elif current_season == 'summer':
        scrap('bol-renverse-sy-pilons-de-poulet')
    elif current_season == 'autumn':
        scrap('trondro-sy-ravitoto')
    elif current_season == 'winter':
        scrap('saosisy-sy-sosety')

def dinner():
    current_season = season()
    if current_season == 'spring':
        scrap('trondro-frity')
    elif current_season == 'summer':
        scrap('tongotromby-sy-tsaramaso')
    elif current_season == 'autumn':
        scrap('salade-de-riz')
    elif current_season == 'winter':
        scrap('lelanomby-saosy')

def scrap(cuisine):
    url = f'https://voyage-madagascar.org/{cuisine}/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    font = 'verdana'
    color = 'purple'

    output = ''

    # title
    h1_tag = soup.find('h1', {'class': 'entry-title'})
    title = h1_tag.get_text()

    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": title,
        "source": "fr",
        "target": "en"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
        "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = json.loads(response.text)
    translated_title = data['data']['translations']['translatedText']

    output += f'<strong style="color: {color}; font-family: {font};">{translated_title}</strong><br><br>'

    div_tags = soup.find('div', {'class': 'entry-content'})

    # print(div_tags.prettify())
    # photo
    img_tag = div_tags.find('img')
    image_src = img_tag['data-src']
    photo = requests.get(image_src)

    # Convert the image to PNG format
    image = Image.open(io.BytesIO(photo.content))
    image.save(f'{cuisine}.png', 'PNG')

    output += f'<img src="E:/Python/Final Project/{cuisine}.png" width="410" height="234" style="display:block;"><br><br>'

    try:
        output += f'<strong style="color: {color}; font-family: {font};">Ingredients</strong><br>'
        ul_tag = div_tags.find('ul')
        li_tag = ul_tag.findAll('li')
        output += f'<ul style="font-family: {font};">'
        for li in li_tag:
            text = li.get_text()

            url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

            payload = {
                "q": text,
                "source": "fr",
                "target": "en"
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
                "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
            }

            response = requests.post(url, json=payload, headers=headers)

            data = json.loads(response.text)
            translated_text = data['data']['translations']['translatedText']
            output += f'<li>{translated_text}</li>'
    except Exception as e:
        pass
    output += '</ul>'

    try:
        output += f'<strong style="color: {color}; font-family: {font};">Instruction</strong><br>'
        ol_tag = div_tags.findNext('ol')
        li_tag = ol_tag.findAll('li')
        output += f'<ol style="font-family: {font};">'
        for li in li_tag:
            text = li.get_text()

            url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

            payload = {
                "q": text,
                "source": "fr",
                "target": "en"
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
                "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
            }

            response = requests.post(url, json=payload, headers=headers)

            data = json.loads(response.text)
            translated_text = data['data']['translations']['translatedText']
            output += f'<li>{translated_text}</li>'
        output += '</ol>'
    except Exception as e:
        pass

    # Save output as PDF
    options = {
        'enable-local-file-access': '',
        'no-outline': None,
        'quiet': '',
    }
    pdfkit.from_string(output, f'{cuisine}.pdf', options=options)
