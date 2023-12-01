print("Hello, please enter your marks below,")

# print("Subject1: ")
# sub1 = int(input())

# print("Subject2: ")
# sub2 = int(input())

# print("Subject3: ")
# sub3 = int(input())

# print("Subject4: ")
# sub4 = int(input())

# print("Subject5: ")
# sub5 = int(input())

# total = sub1 + sub2 +sub3 + sub4 + sub5
# print("Total score:" , total)
# avg = total/5
# print("Average Score: ", avg)

# if avg >= 80:
#     print("Congratulations! Your grade is A")
#     if avg > 90:
#         print("Congratulations again for your distinction!")

# elif avg >= 70:  
#     print("Congratulations! Your grade is B")

# elif avg >= 60:
#     print("Congratulations! Your grade is C")

# elif avg >= 50:
#     print("Congratulations! Your grade is D")

# else:
#     print("Sorry! Your grade is F")

print("==============================================================================")
#Looping: for loop and while loop

fruits = ["mango","orange","apple","banana"]

print(fruits)

for i in fruits:
    print(i)
else:
    print("The list is ended")

sentense = "Welcome to python class"

for i in sentense:
    print(i)

values = range(50,100,5)
print(values)

for i in values:
    print(i)

print("==================================================")

fruits = ["mango","orange","apple","banana"]

while i in fruits:
    print(i)

start = 1

values = 10

while start <= values:
    print(start)
    start += 2
else: 
    print("Loop ended")

print("==================================================")

# greetings = "hello"
# print(f"{greetings} azhar")

for i in range(100):
    if i == 50:
        # break
        continue
    print(i)

