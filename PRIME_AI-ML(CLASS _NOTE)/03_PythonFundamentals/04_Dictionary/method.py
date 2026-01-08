info = {
    "name" : "rohit",
    "subject" : ["math", "computer"],
    "mark" : [45, 67]
}

print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
info.update({"result" : "pass"})
print(info)