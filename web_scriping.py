def explain(text):
    import requests
    from bs4 import BeautifulSoup
    planat = text
    url = "https://spaceplace.nasa.gov/glossary/en/"

    response = requests.get(url)
    text = response.text

    soup = BeautifulSoup(text, 'html.parser')

    p_tags = soup.findAll('p')

    # print(h3tags.get_text())
    # h3tags = soup.find('div')
    # print(h3tags)
    store = []
    for element in p_tags:
       store.append(element.get_text())


    for explain in store:
        word = explain.split(':')
        if word[0] ==  planat.capitalize():
            return word[1]

def related(text):
    import requests
    from bs4 import BeautifulSoup
    name = text
    url = f"https://relatedwords.io/{name}"

    response = requests.get(url)
    all_text = response.text

    soup = BeautifulSoup(all_text, 'html.parser')
    h3tags = soup.findAll('div',{'class':'word-ctn'})
    related_words = ''
    count = 0
    for a in  h3tags:
        related_words += a.get_text().replace('\n','') + '\n'
        count +=1
        if count == 5:
            break
    return related_words

def book(text):
    import requests
    from bs4 import BeautifulSoup
    import re

    url = f"https://childhood101.com/space-books-for-kids/"

    response = requests.get(url)
    all_text = response.text

    soup = BeautifulSoup(all_text, 'html.parser')
    tr_tags = soup.find('tr')


    related_words = []
    count = 0
    for a in tr_tags:
        related_words.append(a.get_text())



    return related_words


def coloring(text):
    import requests
    from bs4 import BeautifulSoup
    import re


    url = f"https://www.ultracoloringpages.com/s/{text}-coloring-pages"
    try:
        response = requests.get(url)
        all_text = response.text

        soup = BeautifulSoup(all_text, 'html.parser')
        tr_tags = soup.find('div', {'class': 'item-title'})

        related_words = []
        count = 0
        for a in tr_tags:
            return 'Dwnloaded ' + (a.get_text()).replace(' Coloring Page', '.png')
    except:
        return "No related terms!"




    # return related_words

def main():
    text = input('Enter a space-related term: ')
    explain_term = explain(text.capitalize())
    print(explain_term)
    related_words = related(text)
    print(related_words)
    related_book = book(text)
    print(related_book)
    image = coloring(text)
    print(image)

if __name__ == "__main__":
    main()