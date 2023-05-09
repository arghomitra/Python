from datetime import datetime
from dateutil import parser


def zodiac(day, month):
    date = f"{day} {month}"
    birthDay = datetime.strptime(date, "%d %B")
    if datetime.strptime("21 March","%d %B")<birthDay< datetime.strptime("19 April","%d %B"):
        print("Aries")
    elif datetime.strptime("20 April","%d %B")<birthDay< datetime.strptime("20 May","%d %B"):
        print("Taurus ")
    elif datetime.strptime("21 May","%d %B")<birthDay< datetime.strptime("21 June","%d %B"):
        print("Gemini")
    elif datetime.strptime("22 June","%d %B")<birthDay< datetime.strptime("22 July","%d %B"):
        print("Cancer")
    elif datetime.strptime("23 July","%d %B")<birthDay< datetime.strptime("22 August","%d %B"):
        print("Leo ")
    elif datetime.strptime("23 August","%d %B")<birthDay< datetime.strptime("22 September","%d %B"):
        print("Virgo  ")
    elif datetime.strptime("23 September","%d %B")<birthDay< datetime.strptime("23 October","%d %B"):
        print("Libra ")
    elif datetime.strptime("24 October","%d %B")<birthDay< datetime.strptime("21 November","%d %B"):
        print("Scorpius ")
    elif datetime.strptime("22 November","%d %B")<birthDay< datetime.strptime("21 December","%d %B"):
        print("Sagittarius ")
    elif datetime.strptime("22 December","%d %B")<birthDay< datetime.strptime("19 January","%d %B"):
        print("Capricornus ")
    elif datetime.strptime("20 January","%d %B")<birthDay< datetime.strptime("18 February","%d %B"):
        print("Aquarius ")
    elif datetime.strptime("19 February","%d %B")<birthDay< datetime.strptime("20 March","%d %B"):
        print("Pisces ")


    return
def percentage(day, month):
    return
def historical(day, month):
    return
def one(day, month, year):
    return
def wikipedia(day, month):
    return
def age(day, month, year):
    return

def main():

    date_input  = 'March 14, 2002'
    date = parser.parse(date_input)


    formatted_date = date.strftime("%d %B %Y")
    birth_day = datetime.strptime(formatted_date,"%d %B %Y")

    day = datetime.strftime(birth_day, '%d')
    month = datetime.strftime(birth_day, '%B')
    year = datetime.strftime(birth_day, '%Y')



    zodiac_output =zodiac(day, month.capitalize())


    return

if __name__ == "__main__":
    main()
