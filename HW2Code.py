from turtle import goto


usersList = []
usersCount = int(input("users count : "))

for i in range(usersCount):
    name  = input(" name : ")
    age = int(input(" age : "))
    user = {'name':name,'age':age}
    usersList.append(user)   

searchedName = input("enter name to search : ")

f = True

for U in usersList:
    if searchedName == U['name']:
        print(U['age'])
        f = False
if(f==True): print("not found")
