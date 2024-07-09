import json

arr_date = []

with open ('operations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# создаёю список всех дат и сортирую его по возрастанию
for i in data:
    if i["state"] == "EXECUTED":
        arr_date.append(i["date"])
        sort_arr_date = sorted(arr_date)
    else:
        break

# сравниваю список сортированных дат и вывожу совпадения через f-строку
for j in data:
    for i in range(1, 6):
        if j["date"] == sort_arr_date[i*-1]:
            name = j["from"].rfind(" ")

            print(f'{j["date"][8:10]}.{j["date"][5:7]}.{j["date"][0:4]} {j["description"]}')
            print(f'{j["from"][0:name]}{j["from"][name:name+5]} {j["from"][name+5:name+7]}** **** {j["from"][name+13:name+17]} -> '
                  f'**{j["to"][-5:-1]} ')
            print(f'{j["operationAmount"]["amount"]} {j["operationAmount"]["currency"]["name"]}')
            print()












