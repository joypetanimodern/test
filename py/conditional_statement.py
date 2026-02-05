


# score = 85
# if score >= 90:
#     grade = "A"
# elif score >=80:
#     grade ="B"
# elif score >=50:
#     grade = "C"
# else:
#     grade = "F"

# print(f"your grade is: {grade}")

# user_age = 45 
# has_lisence = True

# if user_age >=18 and has_lisence:
#     print ("you are allowed to drive")
# else:
#     print ("anda tidak boleh memandu")


# day ='ahad'
# if day == "ahad" or day == 'sabtu':
#     print("yeay boleh cuti")
# else:
#     print("alamak kena kerja")


# weather = "sunny"
# temp = 60

# if weather =="sunny":
#     if temp > 90:
#          print ("its sunny and warm.")
#     else:
#          print("sejuk siot.")



# exersice

# weight = float(input("masukkan berat badan anda dalam kg :"))
# height = float(input("masukkan ketinggian anda dalam cm :"))
# bmi = weight/height**2

# if (bmi<18.5):
#     print("under weight")
# elif (bmi<24.9):
#     print("normal weight")
# else:
#     print("obes")

#loop
# for i in range(5):
#     print(i)
# for i in range (1,6):
#     print (i)


#while loop
# count=0
# while count <5:
#     print(count)
#     count += 1


#loops control
# for i in range(10):
#     if i == 3:
#         continue
#     if i == 7:
#       break
# print(i)

#nested loops
# for i in range(2):
#     for j in range(3):
#         print(f"({i}, {j})")


num = int(input("Enter a number to generate its multiplication table: "))
for i in range(1, 13):
    product = num * i
    print(f"{num} x {i} = {product}")