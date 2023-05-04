# import requests
# import json
#
#
# def language(text):
#     url = "https://whats-language.p.rapidapi.com/languagedetection/detecting"
#
#     sentance = text
#
#     querystring = {"text": sentance}
#
#     headers = {
#         "text": "How to Identify the Language of any Text",
#         "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
#         "X-RapidAPI-Host": "whats-language.p.rapidapi.com"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#
#     json_data = json.loads(response.text)
#     detect_language = json_data['languages'][0]
#
#     with open('iso_639_1codes.csv', 'r', encoding='utf-8') as f:
#         line = f.readline()
#         while line:
#             line = f.readline().split(',')
#             if line[0] == detect_language:
#                 return line[1]
#                 break
#
#
# def countries(language):
#     language_name = language
#     url = f'https://restcountries.com/v3.1/lang/{language_name}'
#     responce = requests.get(url)
#     json_data = json.loads(responce.text)
#     for country in json_data:
#         return country['name']['common']
#
#
#
#
#
# def stopwords(text, language):
#     input_lan = language.lower()
#
#     count = 0
#     with open(f'./stopword/{input_lan}.txt', 'r', encoding='utf-8') as f:
#         file = f.read().split('\n')
#
#         input_text = text.split(' ')
#         # remove punctuation
#         new_text = ''
#         for word in input_text:
#             for char in word:
#                 if char.isalpha():
#                     new_text += char
#             new_text += ' '
#
#         new_splited_text = new_text.split(' ')
#         for stopword in file:
#             for word in new_splited_text:
#                 if word == stopword:
#                     count += 1
#
#     return f'{count} stopwords found'
#
#
# def population():
#     url = f'https://restcountries.com/v3.1/name/common/Dominican Republic'
#     response = requests.get(url)
#     json_data = json.loads(response.text)
#     population = json_data['maps']['population']
#     return population
#
#
# def sentiment(text):
#
#     sentance = text
#
#     # detect language_code
#     url1 = "https://whats-language.p.rapidapi.com/languagedetection/detecting"
#     querystring = {"text": sentance}
#
#     headers1 = {
#         "text": "How to Identify the Language of any Text",
#         "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
#         "X-RapidAPI-Host": "whats-language.p.rapidapi.com"
#     }
#
#     response1 = requests.request("GET", url1, headers=headers1, params=querystring)
#
#     json_data1 = json.loads(response1.text)
#     detect_language = json_data1['languages'][0]
#     # print(detect_language)
#
#     # translate
#     url2 = "https://text-translator2.p.rapidapi.com/translate"
#
#     payload2 = {
#         "source_language": detect_language,
#         "target_language": "en",
#         "text": sentance
#     }
#     headers2 = {
#         "content-type": "application/x-www-form-urlencoded",
#         "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
#         "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
#     }
#
#     response2 = requests.post(url2, data=payload2, headers=headers2)
#     json_data2 =json.loads(response2.text)
#     # translated_text = (json_data2['data'])
#     # v = translated_text['translatedText']
#     print(json_data2)
#
#     # sentiment
#     url3 = "https://sentiment-analysis40.p.rapidapi.com/api/sentiment"
#
#     payload3 = {
#         "language": "en",
#         "text":sentance
#     }
#     headers3 = {
#         "content-type": "application/json",
#         "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
#         "X-RapidAPI-Host": "sentiment-analysis40.p.rapidapi.com"
#     }
#
#     response3 = requests.post(url3, json=payload3, headers=headers3)
#
#     json_data3 = json.loads(response3.text)
#     sentiment = json_data3['result']
#     m = sentiment['label'].lower()
#     return f'The text is {m}'
#
#
# def main():
#     languages = language()
#     print(languages)
#     populations = population()
#     print(populations)
#     sentiments = sentiment()
#     print(sentiments)
#     stopword = stopwords()
#     print(stopword)
#     country = countries()
#     print(country)
#
# if __name__ == "__main__":
#     main()
#

#
import requests
import json
#
# language = 'Indonesian'
# url = f'https://restcountries.com/v3.1/lang/{language}'
# response = requests.get(url)
#
# if response.status_code == 200:
#     json_data = json.loads(response.text)
#     max_population = 0
#     max_population_country = ''
#     for country in json_data:
#         name = country['name']['common']
#         population = country['population']
#         if population > max_population:
#             max_population = population
#             max_population_country = name
#     print(f"The majority of people who speak {language.capitalize()} live in {max_population_country}")
# else:
#     print(f"Error {response.status_code}: {response.reason}")
#
#

# url2 = "https://text-translator2.p.rapidapi.com/translate"
#
# payload2 = {
#     "source_language": 'nl',
#     "target_language": "en",
#     "text": 'Ik ben echt ontzettend teleurgesteld en boos met de slechte kwaliteit die ik heb ontvangen van de klantenservice!'
# }
# headers2 = {
#     "content-type": "application/x-www-form-urlencoded",
#     "X-RapidAPI-Key": "ae7fcf262emshc009e7fab12649ap148aabjsndf480cb51087",
#     "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
# }
#
# response2 = requests.post(url2, data=payload2, headers=headers2)
# json_data2 =json.loads(response2.text)
# translated_text = (json_data2['data'])
# en_text = translated_text['translatedText']
# print(en_text)
sentance = "Ik ben echt ontzettend teleurgesteld en boos met de slechte kwaliteit die ik heb ontvangen van de klantenservice!"

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
    print(f'The text is {s}')

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
    print(f'The text is {s}')

