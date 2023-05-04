def explain(text):
    import requests
    from bs4 import BeautifulSoup
    planat = text.lower()

    url = "https://spaceplace.nasa.gov/glossary/en/"
    response = requests.get(url)
    text_data = response.text

    soup = BeautifulSoup(text_data, 'html.parser')

    p_tags = soup.findAll('p')

    # print(h3tags.get_text())
    # h3tags = soup.find('div')
    # print(h3tags)

    store = []
    for element in p_tags:
        store.append(element.get_text())
    defination = ''
    for item in store:
        word = item.split(':')
        if word[0]:
            if word[0] == planat.capitalize():
                defination = word[1]
    if defination:
        print(defination)
    else:
        print('No definition found!')


def related(text):
    import requests
    from bs4 import BeautifulSoup
    name = text
    url = f"https://relatedwords.io/{name}"

    response = requests.get(url)
    all_text = response.text

    soup = BeautifulSoup(all_text, 'html.parser')
    h3tags = soup.findAll('div', {'class': 'word-ctn'})
    related_words = ''

    count = 0
    for a in h3tags:
        related_words += a.get_text().replace('\n', '') + '\n'
        count += 1
        if count == 5:
            break
    if count > 0:
        print(related_words)
    else:
        print('No related terms!')


def book(text):
    import requests
    from bs4 import BeautifulSoup
    input_word = text

    url = f"https://childhood101.com/space-books-for-kids/"
    response = requests.get(url)
    all_text = response.text

    soup = BeautifulSoup(all_text, 'html.parser')
    tr_tags = soup.findAll('td')
    related_book = ''
    for item in tr_tags:
        words = item.get_text()

        if input_word.capitalize() in words or input_word.lower() in words:
            related_book = words
            break
    if related_book:
        print(related_book.splitlines()[0])
    else:
        print('No book found!')





def coloring(text):
    import requests
    from bs4 import BeautifulSoup
    import re

    url = f"https://www.ultracoloringpages.com/s/{text.lower()}-coloring-pages"
    try:
        response = requests.get(url)
        all_text = response.text

        soup = BeautifulSoup(all_text, 'html.parser')
        tr_tags = soup.find('div', {'class': 'page-thumb'})
        img_tag = tr_tags.find('img')
        img_src = img_tag.get('src')
        image_name = img_src.split('/')[-1]

        image = requests.get(img_src)
        with open(image_name, 'wb') as f:
            f.write(image.content)
            output = ((img_tag.get('alt')).replace(' Coloring Page', '.png')).lower().replace('\n', '')
            print(f'Downloaded {output}')

    except:
        print('Failed to download image!')

    # return related_words


def normal():
    return


def main():
    text = input().strip()
    explain_term = explain(text.capitalize())
    # print(explain_term)
    related_words = related(text)
    # print(related_words)
    image = coloring(text)
    # print(image)
    related_book = book(text)
    # print(related_book)


if __name__ == "__main__":
    main()
