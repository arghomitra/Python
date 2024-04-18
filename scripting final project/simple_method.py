import requests
from bs4 import BeautifulSoup
import pdfkit
from PIL import Image,ImageFilter
import io
import random
import json
import datetime

def simple():
    # Set the desired font and color
    font = 'Arial'
    color = 'purple'
    simple_cuisines = ['madagascar-chicken', 'madagascar-tofu','malagasy-fruity-clafouti', 'malagasy-mofo-sakay', 'malagasy-lasary-avocat', 'malagasy-lasopy',
                       'malagasy-romazava']
    random_cuisine = random.choice(simple_cuisines)
    cuisine_name = random_cuisine.replace('-', ' ').title()
    if random_cuisine == 'madagascar-chicken' or  random_cuisine == 'madagascar-tofu':
        url = f'https://kitchen.kidsandcompany.com/recipe/{random_cuisine}/'

        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        # Photo
        div_tags = soup.find('div', {'class': 'medium-5 small-12 columns'})


        img_tag = div_tags.find('img')
        src = img_tag.get('src')
        photo = requests.get(src)

        # Convert the image to PNG format
        image = Image.open(io.BytesIO(photo.content))
        image.save(f'{cuisine_name}.png', 'PNG')



        # Initialize a string to hold the output
        output = ''
        output += f'<strong style="color: {color}; font-family: {font};">{cuisine_name}</strong><br><br>'

        output += f'<img src="E:/Python/Final Project/{cuisine_name}.png" width="410" height="234" style="display:block;"><br><br>'  # Adjust image width and add styling

        output += f'<strong style="color: {color}; font-family: {font};">Ingredients</strong><br>'
        # Recipe and ingredients
        div_tags = soup.find('div', {'class': 'medium-7 small-12 columns'})
        ingredients_div = div_tags.find('div', class_='ingredients')
        ul_tag = ingredients_div.find('ul')

        li_tags = ul_tag.find_all('li')
        output += f'<ul style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.get_text()
            output += f'<li>{text}</li>'
        output += '</ul>'

        output += '<br><br>'

        #Instructions
        output += f'<strong style="color: {color}; font-family: {font};">Instructions</strong><br>'
        instructions_div = div_tags.find('div', class_='instructions')
        ol_tag = instructions_div.find('ol')

        li_tags = ol_tag.find_all('li')
        output += f'<ol style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.get_text()
            output += f'<li>{text}</li>'
        output += '</ol>'

        # Save output as PDF
        options = {
            'enable-local-file-access': '',
            'no-outline': None,
            'quiet': '',
        }
        pdfkit.from_string(output, f'{cuisine_name}.pdf', options=options)

    else:
        url = f'https://www.internationalcuisine.com/{random_cuisine}/'

        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        # photo
        div_tags = soup.find('div', {'class': 'wprm-container-float-right'})
        img_tag = div_tags.find('img')
        src = img_tag.get('data-lazy-src')
        photo = requests.get(src)

        # Convert the image to PNG format
        image = Image.open(io.BytesIO(photo.content))
        image.save(f'{cuisine_name}.png', 'PNG')

        output = ''
        output += f'<strong style="color: {color}; font-family: {font};">{cuisine_name}</strong><br><br>'

        output += f'<img src="E:/Python/Final Project/{cuisine_name}.png" width="410" height="234" style="display:block;"><br><br>'

        output += f'<strong style="color: {color}; font-family: {font};">Ingredients</strong><br>'

        # ingredient
        div_tags = soup.find('div', {'class': 'wprm-recipe-ingredient-group'})
        ingredients_ul = div_tags.find('ul', class_='wprm-recipe-ingredients')
        li_tags = ingredients_ul.find_all('li', class_='wprm-recipe-ingredient')
        output += f'<ul style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.get_text()
            output += f'<li>{text}</li>'
        output += '</ul>'

        output += '<br><br>'
        # instruction
        output += f'<strong style="color: {color}; font-family: {font};">Instruction</strong><br>'
        div_tags = soup.find('div', {'class': 'wprm-recipe-instruction-group'})
        ingredients_ul = div_tags.find('ul', class_='wprm-recipe-instructions')
        li_tags = ingredients_ul.find_all('li', class_='wprm-recipe-instruction')
        output += f'<ol style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.get_text()
            output += f'<li>{text}</li>'
        output += '</ol>'

        # Save output as PDF
        options = {
            'enable-local-file-access': '',
            'no-outline': None,
            'quiet': '',
        }
        pdfkit.from_string(output, f'{cuisine_name}.pdf', options=options)
