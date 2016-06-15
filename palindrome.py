#name = raw_input("What is your name?\n")
name="aaa aaa"
mylist=list()
reverselist=list()
mylist.extend(name)

print len(mylist)
for i in range(-(len(mylist)-1),1):
    reverselist.extend(mylist[-i])
print reverselist

if mylist == reverselist:
    print "yes"
else:
    print "no"