from bs4 import BeautifulSoup
import requests
from bottle import route, run, template

@route('/')
def index():
    page = requests.get("http://steamcommunity.com/market/search?appid=730#p1")
    soup = BeautifulSoup(page.content, 'html.parser')

    nome_itens = soup.find_all('span', class_='market_listing_item_name')
    qntd_itens = soup.find_all('span', class_='market_listing_num_listings_qty')
    vn_itens = soup.find_all('span', class_='normal_price')
    vv_itens = soup.find_all('span', class_='sale_price')
    img_itens = soup.find_all('img', class_='market_listing_item_img')

    print vv_itens

    itens = {}
    n, q, vv, vn, im = [], [], [], [], []
    for i in range(10):
            n.append(nome_itens[i].string)
            q.append(qntd_itens[i].string)
            vv.append(vv_itens[i].string)
            vn.append(vn_itens[i].string)
            im.append(img_itens[i]['src'])

    itens['nome'] = n
    itens['quantidade'] = q
    itens['valor_normal'] = vn
    itens['valor_venda'] = vv
    itens['imagem'] = im


    return itens

run(host='localhost', port=8080)
