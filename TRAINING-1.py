#TRAINING-1
#length = "2.75"
#width = "1.75"
#area = float(length) *  float(width)
#show = f"With width {float(width)} and length {float(length)} of the room,its area is equal {area}"
#print(f"{show}")

#Training-2
#import math

#radius = 6371.01
#Coordinates of Kyiv
#lat1 = 50.45
#lon1 = 30.523
#Coordinates of London
#lat2 = 51.5072
#lon2 = -0.1275
#lat1r = math.radians(lat1)
#lon1r = math.radians(lon1)
#lat2r = math.radians(lat2)
#lon2r = math.radians(lon2)

#distance = 6371.01 * math.acos(math.sin(lat1r) * math.sin(lat2r) + math.cos(lat1r) * math.cos(lat2r) * math.cos(lon1r - lon2r))
#print(f"Distance between Kyiv and London is {distance}")

#Training-2-1
#import math

#RADIUS = 6371.01
#Coordinates of Kyiv
#lat1 = 50.45
#lon1 = 30.523
#Coordinates of London
#lat2 = 51.5072
#lon2 = -0.1275
#lat1r = math.radians(lat1)
#lon1r = math.radians(lon1)
#lat2r = math.radians(lat2)
#lon2r = math.radians(lon2)

#distance = RADIUS * math.acos(math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon1) - math.radians(lon2)))
#print(f"Distance between Kyiv and London is {distance}")

# Trainig-3

# name = input("Name: ")
# email = input("Email: ")
# age = int(input("Age: "))
# height = float(input("Height: "))
# is_active = bool(input("Whould you like to receive messages? True or False?  ")) 


# is_active = bool(input("Is the user active? ")) 
# is_admin = bool(input("Is the user administrator? "))
# is_permission = bool(input("Does the user have access? "))
# #two versions of code
# #access = True if is_admin else is_active and is_permission
# access = is_admin or is_active and is_permission

# work_experience = int(input("Enter your full work experience in years: "))
# if work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"


# num = int(input("Введіть число: "))

# if num > 0:
#     if num >= 100:
#         result = "Додатне більше 100"
#     else:
#         result = "Додатне менше 100"
# elif num < 0:
#     result = "Число від'ємне"
# else:
#     result = "Це ноль"

# print(result)

# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 >= 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
#     print(result)

# import math

# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c

# if D > 0:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a) 
#     if D % 2 == 0:
#         result = x1
#     else:
#         result = x2
# elif D < 0:
#     result = "D is nagative"
# else:
#     result = "It's zero"
# print(result)

# num = bool(int(input("Enter an integer number: ")) % 2)

# is_even = not num or False
# print(is_even)

# num = int(input("Put a number from 0 - 10: "))
# count = 0 + num
# i = 1
# while i <= count:
#     print(f"Number {i}")
#     i = i + 1 
# print ("Done")

# num = int(input("Enter the integer (0 to 100): "))
# sum = num / 2 * num + num / 2
# i = 1
# while i <= sum:
#     print(f"Number {i}")
#     i = i + 1
# print ("FINISH")

# for variable in range(5):
#     print(variable)  # 0 1 2 3 4

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
     if char == search:
        result +=1

print (result)
            
    
    
