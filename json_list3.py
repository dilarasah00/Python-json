db = {
    "users":{
        "dilaraKaya": {
            "firstName": "Dilara",
            "lastName": "Kaya"
        },
        "elifGiray": {
            "firstName": "Elif",
            "lastName": "Giray"
        }
    },
    "products":{
        "1":{
            "productName": "Iphone 8",
            "price":  5000
        },
        "2":{
            "productName": "Iphone 12",
            "price":  9000
        }
    }
}

import json

# with open("db.json", "w") as file:
#     json.dump(db, file, ensure_ascii= False, indent=2)

with open("db.json")  as file:
    db = json.load(file)

#print(db["users"]["elifGiray"])

db["products"].update({
    "3":{
        "productName": "Iphone 9",
        "price": 6500
    }
})

with open("db.json", "w") as file:
    json.dump(db, file, ensure_ascii= False, indent=2)