import random
ran=random.randrange(1000,9999)
while(True):
    print(ran)
    b=''
    c='1'
    num=input("enter a guess : ")
    l=len(num)
    if l!=4 or num.isalpha():
        print("invalid input")
    elif str(num)==str(ran):
        b='z'
        print("<<<<<___winner___>>>>>")
        print("system generated number : ",ran)
    else :
        count=0
        count2=0
        for i in range(4):
            if str(num)[i]==str(ran)[i]:
                count = count+1
            for j in range(4):
                if str(num)[i]==str(ran)[j] and str(num)[j]!=str(ran)[j]:
                    count2 = count2+1
        print("rabbit",count)
        print("tortois",count2)
    while(c=='1'):
        a=input("do you want to continue ? ")
        if a=='n' or a=='N':
            c='0'
            break
        elif a=='y' or a=='Y':
            break
        else:
            print("invalid input")
    if c=='0':
        break
    if b=='z':
        ran=random.randrange(1000,9999)
        print("new random number has been generated")
