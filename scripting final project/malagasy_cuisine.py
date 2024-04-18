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

def breakfast():
    # Set the desired font and color
    font = 'Arial'
    color = 'purple'

    breakfast = ['HOT BANANAS IN COCONUT MILK', 'Ramanonaka', 'Coconut Chicken']
    random_cuisine = random.choice(breakfast)

    if random_cuisine == 'HOT BANANAS IN COCONUT MILK':
        url = 'https://www.food.com/recipe/hot-bananas-in-coconut-milk-134854'
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data,'html.parser')

        #photo
        photo_div = soup.find('div', class_='primary-image svelte-wgcq7z')
        img_tag = photo_div.find('img')
        src = img_tag.get('src')
        photo = requests.get(src)
        image = Image.open(io.BytesIO(photo.content))
        image.save('HOT BANANAS IN COCONUT MILK.png', 'PNG')

        output = ''
        output += f'<strong style="color: {color}; font-family: {font};">HOT BANANAS IN COCONUT MILK</strong><br><br>'
        output += '<img src="E:\Python\Final Project\HOT BANANAS IN COCONUT MILK.png" width="410" height="234" style="display:block;"><br><br>'

        #ingredients
        output += f'<strong style="color: {color}; font-family: {font};">Ingredients</strong><br>'
        ingredients_div = soup.find('section', class_='layout__item ingredients svelte-ovaflp')
        ul_tag = ingredients_div.find('ul', class_='ingredient-list svelte-ovaflp')

        li_tags = ul_tag.findAll('li')

        output += f'<ul style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.text.strip().replace('\n','')
            output += f'<li>{text}</li>'
        output += '</ul>'

        output += '<br><br>'
        #instruction
        output += f'<strong style="color: {color}; font-family: {font};">Instruction</strong><br><br>'
        instruction_div = soup.find('section', class_='layout__item directions svelte-ovaflp')
        ul_tag = instruction_div.find('ul', class_='direction-list svelte-ovaflp')

        li_tags = ul_tag.findAll('li', class_='direction svelte-ovaflp')

        output += f'<ol style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.text.strip()
            output += f'<li>{text}</li>'
        output += '</ol>'
        options = {
                'enable-local-file-access': '',
                'no-outline': None,
                'quiet': '',
            }
        pdfkit.from_string(output, f'HOT BANANAS IN COCONUT MILK.pdf', options=options)

    elif random_cuisine == 'Ramanonaka':
        url = 'https://www.spyceez.com/en/recette/ramanonaka-le-beignet-sale-de-madagascar/'
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data,'html.parser')

        #photo
        photo_div = soup.find('div', class_='single-recipe')
        img_tag = photo_div.find('img')
        src = img_tag.get('nitro-lazy-src')
        photo = requests.get(src)
        image = Image.open(io.BytesIO(photo.content))
        image.save('Ramanonaka.png', 'PNG')
        output = ''
        output += f'<strong style="color: {color}; font-family: {font};">Ramanonaka, the salty fritter of Madagascar</strong><br><br>'
        output += '<img src="E:\Python\Final Project\Ramanonaka.png" width="410" height="234" style="display:block;"><br><br>'


        # Recipe and ingredients
        output += f'<strong style="color: {color}; font-family: {font};">Ingredients</strong><br>'
        div_tags = soup.find('div', {'class': 'dr-ingredients-list'})
        ul_tag = div_tags.find('ul', {'class': 'dr-unordered-list'})
        li_tags = ul_tag.find_all('li')
        output += f'<ul style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.get_text()
            output += f'<li>{text}</li>'
        output += '</ul>'

        output += '<br><br>'
        # Recipe
        output += f'<strong style="color: {color}; font-family: {font};">Instruction</strong><br>'
        div_tags = soup.find('div', {'class': 'dr-instructions'})
        ul_tag = div_tags.find('ol', {'class': 'dr-ordered-list'})
        li_tags = ul_tag.find_all('li')
        output += f'<ol style="font-family: {font};">'
        for li_tag in li_tags:
            text = li_tag.get_text()
            output += f'<li>{text}</li>'
        output += '</ol>'


        options = {
            'enable-local-file-access': '',
            'no-outline': None,
            'quiet': '',
        }
        pdfkit.from_string(output, 'Ramanonaka.pdf', options=options)
    elif random_cuisine == 'Coconut Chicken':
        url = f'https://www.slofoodgroup.com/blogs/recipes-stories/coconut-chicken-akoho-sy-voanio'

        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

            # Photo
        div_tags = soup.find('div', {'class': 'main_content_area content container'})
        ul_tag = div_tags.find('ul', {'class': 'slides'})
        img_tag = ul_tag.find('source')

        src = img_tag.get('srcset')

        photo = requests.get('http:'+src)

        # Convert the image to PNG format
        image = Image.open(io.BytesIO(photo.content))
        image.save('Coconut Chicken.png', 'PNG')
        output = ''
        output += f'<strong style="color: {color}; font-family: {font};">Coconut Chicken (Akoho Sy Voanio)</strong><br><br>'
        output += '<img src="E:\Python\Final Project\Coconut Chicken.png" width="410" height="234" style="display:block;"><br><br>'

        #ingredients
        output += f'<strong style="color: {color}; font-family: {font};">Ingredients</strong><br>'
        ul_tag = div_tags.findAll('ul')
        for ul in ul_tag:
            li_tags = ul.findAll('li', {'style': 'font-weight: 400;'})
            output += f'<ul style="font-family: {font};">'
            for li_tag in li_tags:
                text = li_tag.get_text()
                output += f'<li>{text}</li>'
            output += '</ul>'

        output += '<br><br>'
        output += f'<strong style="color: {color}; font-family: {font};">Instruction</strong><br>'
        ul_tag = div_tags.findAll('ol')
        for ul in ul_tag:
            li_tags = ul.findAll('li', {'style': 'font-weight: 400;'})
            output += f'<ol style="font-family: {font};">'
            for li_tag in li_tags:
                text = li_tag.get_text()
                output += f'<li>{text}</li>'
            output += '</ol>'

        options = {
            'enable-local-file-access': '',
            'no-outline': None,
            'quiet': '',
        }
        pdfkit.from_string(output, 'Coconut Chicken.pdf', options=options)

def lunch():
    # Set the desired font and color
    font = 'Arial'
    color = 'purple'

    simple_cuisines = ['malagasy-fruity-clafouti', 'malagasy-mofo-sakay', 'malagasy-lasary-avocat', 'malagasy-lasopy',
                       'malagasy-romazava']
    random_cuisine = random.choice(simple_cuisines)
    cuisine_name = random_cuisine.replace('-', ' ').title()

    url = f'https://www.internationalcuisine.com/{random_cuisine}/'

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    # photo
    div_tags = soup.find('div', {'class': 'wprm-container-float-right'})
    img_div = div_tags.find('div', class_='wprm-recipe-image wprm-block-image-normal')
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
def dinner():
    dinnars = ['foie-de-boeuf-sauce-aux-oignons', 'salade-de-riz', 'crevettes-panees','trondro-sy-ravitoto','hom-bao-na-brioche-chinois','macaroni-aux-sardines','lelanomby-saosy','ragout-de-porc']
    random_cuisine = random.choice(dinnars)

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
    output += '</ul>'

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

    # Save output as PDF
    options = {
        'enable-local-file-access': '',
        'no-outline': None,
        'quiet': '',
    }
    pdfkit.from_string(output, f'{random_cuisine}.pdf', options=options)


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


def main():
    seasonal()


if __name__ == "__main__":
    main()