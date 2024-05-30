class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price



p1 = Product("Lale", 50)
p2 = Product("Nergis", 80)

products = [p1.__dict__, p2.__dict__]
#urunler = {p1.id: p1.__dict__, p2.id: p2.__dict__}

import json

with open("cicekler.json", "w") as file:
    json.dump(products, file)


with open("cicekler.json") as file:
    data = json.load(file)

urunler = []

for p in data:
    urunler.append(Product(p["name"],p["price"]))
print(urunler[0].name)
