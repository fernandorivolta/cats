import requests
import pymongo

client = pymongo.MongoClient("mongodb://mongo:27017/")
client.drop_database('db')
mydb = client["db"]
col_breeds = mydb["breeds"]
col_categories = mydb["categories"]
headers = {'x-api-key': '968f68ea-0fac-43f8-825a-99fed57586ed'}

def get_category_id(categories):
    # Recebe uma lista de categorias e retorna uma lista dos ids dessas categorias
    categories_id = []
    res = requests.get('https://api.thecatapi.com/v1/categories', headers=headers)
    for x in res.json():
        if x['name'] in categories:
            categories_id.append(x['id'])
    return categories_id

res = requests.get('https://api.thecatapi.com/v1/breeds', headers=headers)
for _cat in res.json():
    imgs = []

    #pesquisa 3 imagens de acordo com o id da raça do gato
    img_res = requests.get(f'https://api.thecatapi.com/v1/images/search?breed_id={_cat["id"]}&limit=3', headers=headers)
    for img in img_res.json():
        imgs.append(img['url'])

    cat = {'breed' : _cat['name'], 'origin' : _cat['origin'], 'temperament' : _cat['temperament'].split(', '), 'description' : _cat['description'], 'imgs' : imgs}
    col_breeds.insert_one(cat) 

for _id in get_category_id(['sunglasses', 'hats']):
    res = requests.get(f'https://api.thecatapi.com/v1/images/search?category_ids={_id}&limit=3', headers=headers)
    for _img in res.json():
        img = {'category' : _img['categories'], 'img_url' : _img['url']}
        col_categories.insert_one(img)