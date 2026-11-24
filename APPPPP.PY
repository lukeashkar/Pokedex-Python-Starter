print("pirate token pirate token i will get the pirate token pirate token pirate token i will get the pirate token searching chests all day searching chests all night pirate token pirate token i will get the pirate token")



users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]



for user in users:
    try:
        if user["role"] == "admin":
            print(user["name"])
    except KeyError:
        continue