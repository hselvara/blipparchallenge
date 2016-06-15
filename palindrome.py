name = raw_input("Enter the input string: ")
reverselist=list()

for i in range(-(len(name)-1),1):
    reverselist.append(name[-i])

reverseString = "".join(map(str,reverselist))
print reverseString

