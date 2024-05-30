data = [
    {
        "userName": "sadikturan",
        "firstName": "Sadık",
        "lastName": "Turan"
    },
     {
        "userName": "cinarturan",
        "firstName": "Çınar",
        "lastName": "Turan"
    }
]

import json

# with open("users.json", "w") as file:
#     json.dump(data, file, ensure_ascii= False, indent=2)

user = {
    "userName": "betülturan",
    "firstName": "Betül",
    "lastName": "Turan"
}
with open("users.json") as file:
    users = json.load(file)
for user in users:
    if user["userName"] == "sadikturan":
        user["userName"] = "ali_turan"
        user["firstName"] = "Ali"

users.remove(users[1])

   
#users.append(user)

with open("users.json", "w") as file:
    json.dump(users, file, ensure_ascii=False,indent=2)
