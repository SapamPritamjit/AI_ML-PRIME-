# break :- Terminate loop 
# Continue :- skip current iteration

i = 1

while (i <= 10):
    if(i % 6 == 0):
        break

    if(i == 4):
        i+=1
        continue

    print(i)
    i+=1

print("Outside loop....")