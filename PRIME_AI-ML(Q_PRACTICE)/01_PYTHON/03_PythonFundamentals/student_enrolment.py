# Given a list of tuples with info(name, subject):
#     list all unique course
#     list student enrolled in english
#     create dictionary(student, set of course)

info = [
    ("alice" , "math"),
    ("bob" , "Science"),
    ("alice" , "science"),
    ("charlie" ,"math"),
    ("bob" , "math"),
    ("alice" , "english"),
    ("charlie" , "english")
]

# list all unique course

unique_cource = set()
# for tup in info:
#     unique_cource.add(tup[1])

for name, course in info:
    unique_cource.add(course)

print(unique_cource)

# list student enrolled in english

for tup in info:
    if tup[1] == "english":
        print(tup[0])

# create dictionary(student, set of course)

dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
    

print(dict)