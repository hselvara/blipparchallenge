'''
Created on Jun 14, 2016

@author: hselvara
'''

    
def calcprime(num):
    bln=False
    for nos in range(2, num):
        if num % nos == 0:
            bln= True
    
    if bln:
        print False
    else:
        print True
    
num=int(raw_input("Enter the number:"))
if num == 0 or num>1000:
    print 'Enter the input in the range 1 to 1000'
elif num == 1:
    print False
else:
    calcprime(num)