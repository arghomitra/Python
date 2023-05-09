from datetime import datetime
from dateutil import parser
from math import trunc
import requests
from bs4 import BeautifulSoup


def zodiac(day, month):
    date = f"{day} {month}"
    birthDay = datetime.strptime(date, "%d %B")
    if datetime.strptime("21 March", "%d %B") < birthDay < datetime.strptime("19 April", "%d %B"):
        print("Aries")
    elif datetime.strptime("20 April", "%d %B") < birthDay < datetime.strptime("20 May", "%d %B"):
        print("Taurus ")
    elif datetime.strptime("21 May", "%d %B") < birthDay < datetime.strptime("21 June", "%d %B"):
        print("Gemini")
    elif datetime.strptime("22 June", "%d %B") < birthDay < datetime.strptime("22 July", "%d %B"):
        print("Cancer")
    elif datetime.strptime("23 July", "%d %B") < birthDay < datetime.strptime("22 August", "%d %B"):
        print("Leo ")
    elif datetime.strptime("23 August", "%d %B") < birthDay < datetime.strptime("22 September", "%d %B"):
        print("Virgo  ")
    elif datetime.strptime("23 September", "%d %B") < birthDay < datetime.strptime("23 October", "%d %B"):
        print("Libra ")
    elif datetime.strptime("24 October", "%d %B") < birthDay < datetime.strptime("21 November", "%d %B"):
        print("Scorpius ")
    elif datetime.strptime("22 November", "%d %B") < birthDay < datetime.strptime("21 December", "%d %B"):
        print("Sagittarius ")
    elif datetime.strptime("22 December", "%d %B") < birthDay < datetime.strptime("19 January", "%d %B"):
        print("Capricornus ")
    elif datetime.strptime("20 January", "%d %B") < birthDay < datetime.strptime("18 February", "%d %B"):
        print("Aquarius ")
    elif datetime.strptime("19 February", "%d %B") < birthDay < datetime.strptime("20 March", "%d %B"):
        print("Pisces ")


def percentage(day, month):
    return


def historical(day, month):
    url = "https://historical-events-by-api-ninjas.p.rapidapi.com/v1/historicalevents"

    querystring = {"month": month, "day": day}

    headers = {
        "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
        "X-RapidAPI-Host": "historical-events-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_data = response.json()
    print('Historical events:')
    for event in json_data:
        print(event['year'], '-', event['event'])


def wikipedia(day, month):
    return


def one(day, month, year):
    url = f"https://www.onthisday.com/date/{year}/{month}/{day}"
    response = requests.get(url)
    all_text = response.text

    soup = BeautifulSoup(all_text, 'html.parser')
    ul_tags = soup.findAll('ul', {'class': 'event-list'})

    for ul_tag in ul_tags:
        li_tags = ul_tag.findAll('li')
        for li_tag in li_tags:
            if '#1' in li_tag.get_text():
                hit = li_tag.get_text()
                print(hit.strip().replace('#1 Song:', 'Number one hit:'))
                break


def wikipedia(day, month):
    url = f"https://en.wikipedia.org/wiki/April_23"
    response = requests.get(url)
    all_text = response.text

    soup = BeautifulSoup(all_text, 'html.parser')
    h2_tags = soup.findAll('h2')
    for item in h2_tags:
        print(item.get_text())
    print(h2_tags)
    # tr_tags = soup.findAll('ul')
    # a = ''
    # for item in tr_tags:
    #     if "probable" in item.get_text() or a == 'start':
    #         a= 'start'
    #         print(item.get_text())

    return


def age(day, month, year):
    today = datetime.now()
    birthDate = f'{day} {month} {year}'
    formated_date = parser.parse(birthDate)
    age = trunc((today - formated_date).days / 365)

    print(f"Today {age} years old!")


def main():
    date_input = input('BirthDate : ')
    date = parser.parse(date_input)

    formatted_date = date.strftime("%d %B %Y")
    birth_day = datetime.strptime(formatted_date, "%d %B %Y")

    day = datetime.strftime(date, '%d')
    month = datetime.strftime(date, '%B')
    year = datetime.strftime(date, '%Y')

    zodiac(day, month.capitalize())
    age(day, datetime.strftime(birth_day, '%m'), year)
    # wikipedia(day,month)
    historical(day, datetime.strftime(date, '%m'))
    one(day, month, year)


if __name__ == "__main__":
    main()
