import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','w','s','t','u'
         ,'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
         'R','W','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','*','+']
print("Wellcome to password generator")
n_letters=int(input("How many number of letters you want in your password\n"))
n_numbers=int(input("How many number of numbers you want in your password\n"))
n_symbols=int(input("How many numbers of symbols you want in your password\n"))
password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password=password+char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password=password+char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password=password+char
print("The random password is\n",password)


