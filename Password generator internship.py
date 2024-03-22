import random as rand

bucket='abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+ABCDEFGHIJKLMNOPQRSTUVWXYZ7894561230. '
while 1:
    lenght=int(input("Enter the length of password :"))
    pcount=int(input("Number of password required :"))
    for i in range(0,pcount):
        passwd=""
        for j in range(0,lenght):
            passchar=rand.choice(bucket)
            passwd+=passchar
        print("The passwords are :",passwd)