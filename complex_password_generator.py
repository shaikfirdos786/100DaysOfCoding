print("Welcome To Password Generator!")

letters_S=['a','b','c','d','e','f','g','h','i',
           'j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z']


letters_C=['A','B','C','D','E','F','G','H','I',
           'J','K','L','M','N','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z']

digits=['0','1','2','3','4','5','6','7','8','9']


symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

capital_letters=int(input("How many Capital letters would you like in your Password ? "))
small_letters=int(input("How many small letters would you like in your Password ? "))
nr_symbols=int(input("How many symbols would you like in your Password ? "))
nr_digits=int(input("How many numbers would you like in your Password ? "))

temp_password=[]

for char in range(1,capital_letters+1):
    temp_password.append(random.choice(letters_C))

for char in range(1,small_letters+1):
    temp_password.append(random.choice(letters_S))

for symbol in range(1,nr_symbols+1):
    temp_password.append(random.choice(symbols))

for num in range(1,nr_digits+1):
    temp_password.append(random.choice(digits))

random.shuffle(temp_password)

password=""
for char in temp_password:
    password+=char

print()
print(f"Your password is: {password}")
