# fruit = ["apple", "banana", "cherry", "date", "elderberry"]

# for i in range(1 , 3):
#     print(fruit[i])

# i = 1
# while i < 7:
#     print(i)
#     i += 1

# x = 0
# while not (1 <= x <= 50):
#     x = int(input("Enter a number between 1 and 50: "))
#     print(x)

for i in range(5):
    x = int(input("Enter a number: "))  
    if 1 <= x <= 100:
        print(x)
    else:
        print("Number out of range, please try again.")
        break

