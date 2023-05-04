import requests
import json


def language(text):
    url = "https://whats-language.p.rapidapi.com/languagedetection/detecting"

    sentance = text

    querystring = {"text": sentance}

    headers = {
        "text": "How to Identify the Language of any Text",
        "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
        "X-RapidAPI-Host": "whats-language.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = json.loads(response.text)
    detect_language = json_data['languages'][0]

    with open('iso_639_1codes.csv', 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            line = f.readline().split(',')
            if line[0] == detect_language:
                return line[1]
                break


def countries(language):
    language_name = language
    url = f'https://restcountries.com/v3.1/lang/{language_name}'
    responce = requests.get(url)
    json_data = json.loads(responce.text)
    for country in json_data:
        output = country['name']['common']
        return output


def stopwords(text, language):
    input_lan = language.lower().split(' ')

    texts = text.lower().split(" ")
    count = 0
    for word in texts:
        # print(word)
        files = f"{input_lan[0]}.txt"
        with open(files, "r", encoding="utf-8") as reader:
            storage = reader.readline()
            while storage:
                storage = reader.readline().split()
                if word in storage:
                    count += 1

    return count


def population(country):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)
    json_data = json.loads(response.text)

    return json_data[0]['population']


def sentiment(text):
    sentance = text

    # detect language_code
    url1 = "https://whats-language.p.rapidapi.com/languagedetection/detecting"
    querystring = {"text": sentance}

    headers1 = {
        "text": "How to Identify the Language of any Text",
        "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
        "X-RapidAPI-Host": "whats-language.p.rapidapi.com"
    }

    response1 = requests.request("GET", url1, headers=headers1, params=querystring)

    json_data1 = json.loads(response1.text)
    detect_language = json_data1['languages'][0]
    # print(detect_language)

    # translate
    if not detect_language == 'en':

        url2 = "https://text-translator2.p.rapidapi.com/translate"

        payload2 = {
            "source_language": detect_language,
            "target_language": "en",
            "text": sentance
        }
        headers2 = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
            "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
        }

        response2 = requests.post(url2, data=payload2, headers=headers2)
        json_data2 = json.loads(response2.text)

        translated_text = (json_data2['data'])
        en_text = translated_text['translatedText']
        # print(en_text)

        # sentiment
        url3 = "https://sentiment-analysis40.p.rapidapi.com/api/sentiment"

        payload3 = {
            "language": "en",
            "text": en_text
        }
        headers3 = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
            "X-RapidAPI-Host": "sentiment-analysis40.p.rapidapi.com"
        }

        response3 = requests.post(url3, json=payload3, headers=headers3)

        json_data3 = json.loads(response3.text)
        sentiment = json_data3['result']
        s = sentiment['label'].lower()
        return s

    else:
        # sentiment
        url3 = "https://sentiment-analysis40.p.rapidapi.com/api/sentiment"

        payload3 = {
            "language": "en",
            "text": sentance
        }
        headers3 = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
            "X-RapidAPI-Host": "sentiment-analysis40.p.rapidapi.com"
        }

        response3 = requests.post(url3, json=payload3, headers=headers3)

        json_data3 = json.loads(response3.text)
        sentiment = json_data3['result']
        s = sentiment['label'].lower()
        return s


def majority_population(lang):
    import requests
    import json
    language = lang
    url = f'https://restcountries.com/v3.1/lang/{language}'
    response = requests.get(url)


    json_data = json.loads(response.text)
    max_population = 0
    max_population_country = ''
    for country in json_data:
        name = country['name']['common']
        population = country['population']
        if population > max_population:
            max_population = population
            max_population_country = name
    return f"The majority of people who speak {language.capitalize()} live in {max_population_country}"






def main():
    text = input()
    try:
        languages = language(text).replace('\n','')
        print(f'The detected language is {languages}')
        stopword = stopwords(text, languages)
        print(f'{stopword} stopwords found')
        sentiments = sentiment(text)
        print('The text is ',sentiments)
        population = majority_population(languages)
        print(population)

        # country = countries()
        # print(country)
    except :
        print('Something went wrong with the language detection!')


if __name__ == "__main__":
    main()