nums = [1, 2, 435, 8, 657, 67]

i = 0

tar = int(input("ENter target number: "))
for val in nums:
    if(tar == val):
        print(f"{tar} found in {i} position.")
        break

print("Not found")