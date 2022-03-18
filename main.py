from curses import beep, pair_content
from re import T
from time import clock_settime
from tkinter import PAGES
from tkinter.tix import Tree
from urllib import response
import requests
from bs4 import BeautifulSoup
import json


# def get_json(url):
#     """Получения количество страниц"""
#     s = requests.session()
#     response = s.get(url=url)

#     with open('python_rozetka/catalog_json.json', 'w') as file:
#         json.dump(response.json(), file, indent=4, ensure_ascii=False)


# def collection_data():
#     s = requests.session()
#     response = s.get(url='https://xl-catalog-api.rozetka.com.ua/v4/goods/getDetails?front-type=xl&country=UA&lang=ru&with_groups=1&with_docket=1&goods_group_href=1&product_ids=')
#     data = response.json()
#     title = data.get('data')
#     for ti in title:
#         discount = ti.get('title')
#         print(discount)

#         # print(ti.get('title'))
#         # print(ti.get('price'))
        # print('-' * 50)



page_p = {}
count = 1
catalog_list = []

def get_count_page():
    s = requests.session()
    response = s.get(
        url='https://xl-catalog-api.rozetka.com.ua/v4/goods/get?front-type=xl&country=UA&lang=ru&producer=moleskine&sell_status=available&page=1&category_id=2514852')
    data = response.json()
    page_count = int(data.get('data').get('total_pages'))
    for page in range(1, page_count + 1):
        url = f'https://xl-catalog-api.rozetka.com.ua/v4/goods/get?front-type=xl&country=UA&lang=ru&producer=moleskine&sell_status=available&page={page}&category_id=2514852'
        data = response.json()
        
        for pg in data:
            s = requests.session()
            response = s.get(url=url)
            data = response.json()
            page_p[page] = data.get('data').get('ids')


    with open('python_rozetka/j.json','w') as file:
        json.dump(page_p, file, indent=4, ensure_ascii=False)

    return page_count

def get_article():
    with open('python_rozetka/j.json') as file:
        news_dict = json.load(file)
        page_c = get_count_page()


    print(f'[INFO] Waiting...')

    for count in range(1, page_c + 1):
        s = requests.session()
        response = s.get(url=f'https://xl-catalog-api.rozetka.com.ua/v4/goods/getDetails?front-type=xl&country=UA&lang=ru&with_groups=1&with_docket=1&goods_group_href=1&product_ids={",".join(map(str,news_dict[str(count)]))}')
        data = response.json()
        dat = data.get('data')


        
        for key in dat:
            catalog_list.append(
                {
                    'id': key.get('id'),
                    'title' : key.get('title'),
                    'price' : key.get('price'),
                    'old_price' : key.get('old_price'),
                    'discount': key.get('discount'),
                    'link': key.get('href')


                }
            )
        print(f'[INFO] {count}/{page_c}')

    with open(f"python_rozetka/articles_list.json", "w") as file:
        json.dump(catalog_list, file, indent=4, ensure_ascii=False)


    # print(','.join(map(str,news_dict[2])))

    
    
    
    
    
    

    # with open('python_rozetka/j.json','w') as file:
    #     json.dump(page_p, file, indent=4, ensure_ascii=False)




            

    
    # for key,value in page_p.items():
    #     for item in value:
            


def main():
    # get_json('https://xl-catalog-api.rozetka.com.ua/v4/goods/getDetails?front-type=xl&country=UA&lang=ru&with_groups=1&with_docket=1&goods_group_href=1&product_ids=8823725,18574290,311320208,4216881,4202748,93223826,311320258,57248049,4202566,208093081,311320023,20979526,311320198,8823739,4221165,41015824,208093009,208093099,93223694,4195734,311320143,57248151,208093147,93223874,4214165,4200991,311320298,311320283,41008840,8823893,311320278,311320263,4206612,208093159,208093141,18574052,263881961,212242549,212354899,204531151,212351011,204526063,212351221,204528691,204528439,320266042,263881576,214822159,212354947,204533209,204529063,277530813,214822519,212355175,212344981,212344831,212245069,212243239,212242981,212242975')
    # data_param('python_rozetka/articles_urls_list.txt')
    # collection_data()
    get_count_page()
    get_article()



if __name__ == '__main__':
    main()
