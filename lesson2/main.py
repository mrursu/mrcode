import requests
from bs4 import BeautifulSoup
import json
import csv
import random
import time


url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

# src = req.text
# print(src)

# with open('index.html','w') as file:
#     file.write(src)
    
with open('lesson2/index.html') as file:
    src = file.read()
    
# soup = BeautifulSoup(src, 'lxml')
# all_products_href = soup.find_all(class_='mzr-tc-group-item-href')

# all_catigories_dict = {}

# for item in all_products_href:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#     # print(f"{item_text} : {item_href}")
#     all_catigories_dict[item_text] = item_href
    
# with open('all_catigories.json','w') as file:   
#     json.dump(all_catigories_dict, file, indent=4, ensure_ascii= False )

with open('lesson2/all_catigories.json') as file:
    all_catigories = json.load(file)
    
iteration_count = int(len(all_catigories)) - 1
print(f"Всего итераций : {iteration_count}")


count = 0
for category_name,category_href in all_catigories.items():
    rep = ["-"," ","'"]
    for item in rep:
        if item in category_name:
            categoty_name = category_name.replace(item,'_')
    req = requests.get(url=category_href, headers=headers)
    src = req.text
    with open(f"lesson2/data/{count}_{category_name}.html", "w") as file:
        file.write(src)
    
    with open(f"lesson2/data/{count}_{category_name}.html") as file:
        src = file.read()
    soup = BeautifulSoup(src,'lxml')
    
    # проверка страницы на наличие блока
    alert_block  = soup.find(class_ = 'uk-alert-danger')
    if alert_block is not None:
        continue
    
    
    # собираем заголовки таблицы
    table_head = soup.find(class_ = 'mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    
    with open(f"lesson2/data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    product_data = soup.find(class_ = 'mzr-tc-group-table').find('tbody').find_all('tr')
    
    for item in product_data:
        product_tds = item.find_all('td')
        
        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        
        with open(f"lesson2/data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
        )
    
    count += 1
    
    print(f"# Количество итераций {count}.{category_name} записан ...")
    iteration_count = iteration_count - 1
    
    if iteration_count == 0:
        print("Работа завершина ...")
        break
    
    print(f"# Осталось итераций: {iteration_count}")
    time.sleep(random.randrange(2,4))
        
        