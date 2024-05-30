import json
data = {
    "sevimKaya":{
        "firstName": "Sevim",
        "lastName": "Kaya"
    },
    "eceBulut":{
        "firstName": "Ece",
        "lastName": "Bulut"
    }
}

with open("users2.json", "w") as file:
    json.dump(data, file, ensure_ascii= False, indent=2)

with open("users2.json") as file:
    users = json.load(file)

print(users["sevimKaya"])

users.update(
   { "emelBulut": 
    {
    "firstName": "Emel",
    "lastName": "Bulut",
    "age": 30
  }}
)

with open("users2.json", "w") as file:
    json.dump(users, file, ensure_ascii= False, indent=2)