import requests
from bs4 import BeautifulSoup
import pdfkit
from PIL import Image,ImageFilter
import io
import random
import json
import datetime

def seasonal():
    # Determine the current season
    current_month = datetime.datetime.now().month
    if 3 <= current_month <= 5:  # Spring (March, April, May)
        current_season = "spring"
    elif 6 <= current_month <= 8:  # Summer (June, July, August)
        current_season = "summer"
    elif 9 <= current_month <= 11:  # Autumn (September, October, November)
        current_season = "autumn"
    else:  # Winter (December, January, February)
        current_season = "winter"

    # Define a dictionary of specific foods for each season
    seasonal_foods = {
        "spring": ["calamar-grille-de-tulear", "achard-de-mangue", "mi-xao-aux-crevettes"],
        "summer": ["crevettes-panees", "solovolo"],
        "autumn": ["macaroni-aux-sardines", "tongotromby-sy-tsaramaso", "ragout-de-porc"],
        "winter": ["macaroni-aux-sardines", "henabaolina-sy-tsaramaso-lena", "henomby-ritra-sy-sakamalaho"]
    }

    # Get a random food from the current season's list
    random_cuisine = random.choice(seasonal_foods[current_season])


    url = f'https://voyage-madagascar.org/{random_cuisine}/'
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
    image.save(f'{random_cuisine}.png', 'PNG')

    output += f'<img src="E:/Python/Final Project/{random_cuisine}.png" width="410" height="234" style="display:block;"><br><br>'


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
    pdfkit.from_string(output, f'{random_cuisine}.pdf', options=options)