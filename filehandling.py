# firstText = open("first-text.txt",'r')

# content = firstText.read()

# print(content)

# firstText.close()


with open("first-text.txt",'r') as firstText:
    content=firstText.read()
    print(content)

secondText = open("newfile.txt",'w+')

second_content="""Hello guys
this is some text
another text
123412345r234523
"""

secondText.write(second_content)
secondText.seek(0)
print("-----",secondText.read())

secondText.close()

try:
    thirdText = open("newfile.txt",'r')
    thirdcontent = "Hello guys 1234565"
    thirdText.write(thirdcontent)
    print(thirdText.tell())
    thirdText.seek(0)
    mytext = thirdText.read()
    mytext = "Writing in first position"+mytext
    thirdText.write(mytext)
    print("-------------------------------------")
    print(thirdText.read())
except:
    print("There is an issue in file operation. Please report")

thirdText.close()

try:
    mytextlines = open("newfile4534.txt",'r')

    print(len(mytextlines.readlines()))
except FileNotFoundError:
    print("The file is not found")


try:
    a =10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("There is zero division error, the denominator is zero")
except:
    print("There are some other issues")

print(dir(locals()['__builtins__']))