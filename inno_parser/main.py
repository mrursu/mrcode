import requests
from bs4 import BeautifulSoup
import lxml
import math


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}


def get_data(url):
    # s = requests.Session()
    # response = s.get(url=url,headers=headers)
    
    
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text,'lxml')
    #     print(soup)
    # with open('inno_parser/data/index.html','w') as file:
    #     file.write(response.text)
        
    with open('inno_parser/data/index.html') as file:
        src = file.read()
        
    # print(src)
    
    # Поличения информации карточки
    soup = BeautifulSoup(src,'lxml')
    product_info = soup.find_all(class_ = 'product-tile')
    
    # Поличения Количество товаров
    page_count = int(soup.find(id = 'showedProducts').get('max'))
    
    # Получения Количество страниць
    # for item in range(36, page_count + 36, 36):
    #     print(f'https://www.inno.be/fr/marques/adidas-boss-tommyhilfiger/polos-hommes?prefn1=hasNoImagesYet&prefv1=false&start=0&sz={item}')
    
    count = 1
    
    
    
    
    for item in product_info:
        product_title = item.find(class_ = 'product-name').text
        product_price = item.find(class_ = 'personalization_product-price').text.strip()
        product_href = 'https://www.inno.be/' + item.find(class_ = 'product-name').get('href') 
        img_href = item.find(class_ = 'image-container').find('img').get('src')
        
        print(count,product_title,' - ', product_price,'\n',product_href,img_href,'\n')
        
        count += 1
        
    # print(page_count)

        
        


def main():
    get_data('https://www.inno.be/fr/marques/adidas-barbour-boss-tommyhilfiger/polos-hommes?prefn1=hasNoImagesYet&prefv1=false&start=0&sz=180')
  
    count_product = 152
    page_step = 36
    a = math.ceil(count_product / page_step )
    # print(a * page_step)
    
    
    # for item in range(36,152+36,36):
    #     print(f'https://www.inno.be/fr/marques/adidas-boss-tommyhilfiger/polos-hommes?prefn1=hasNoImagesYet&prefv1=false&start=0&sz={item}')
        
if __name__ == '__main__':
    main()
