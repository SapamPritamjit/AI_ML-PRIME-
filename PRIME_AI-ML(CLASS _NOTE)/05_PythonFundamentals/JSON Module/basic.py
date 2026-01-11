import json

with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)


d = {
    "name" : "Sapam Pritamjit",
    "course" : "CSE",
    "Year" : "2nd year 3rd sem finish",
    "address" : {
        "city" : "Delhi",
        "COuntry" : "India"
    },
    "subject" : ["python", "AI/ML"],
    "age" : 20
}

with open("data.json", "w") as f:
    json.dump(d, f, indent=4)