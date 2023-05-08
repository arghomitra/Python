import json
# string json writing way
# json_data = '{"Name":"Argho Mitra","Age":45,"City":"Antwerpen"}'
# y = json.loads(json_data)
# print(y["Name"])

# json_file = open("books.json")
# # json_data = json.loads(json_file.read())
# # print(json_data)
# # print(json_data["books"][0]["title"])

# python_data = {"Name": "Argho Mitra", "Age": 45, "City": "Antwerpen"}
# json_data = json.dumps(python_data)

# print(python_data)
# print(json_data)

python_data = {}
python_data['people'] = []
python_data['people'].append({
    'Name': 'Argho Mitra',
    'Age': 20
})
python_data['people'].append({
    'Name': 'Sadman',
    'Age': 30
})
python_data['people'].append({
    'Name': 'Faysal',
    'Age': 21
})
python_data['people'].append({
    'Name': 'Asif',
    'Age': 22
})
json_file = open('jason.json', 'w')
json_data = json.dump(python_data, json_file)
json_file.close()

! pip install requests

url = 'https://api.kanye.rest/'
