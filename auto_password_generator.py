import random

lower=['a','b','c','d','e','f','g','h','i',
           'j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z']


upper=['A','B','C','D','E','F','G','H','I',
           'J','K','L','M','N','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z']

digits=['0','1','2','3','4','5','6','7','8','9']


symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

max_len=12

combined=upper+lower+digits+symbols

rand_upper=random.choice(upper)
rand_lower=random.choice(lower)
rand_digit=random.choice(digits)
rand_symbol=random.choice(symbols)

temp_pass=rand_upper+rand_lower+rand_symbol+rand_digit

for char in range(max_len-4):
    temp_pass+=random.choice(combined)

    temp_pass_list=list(temp_pass)
    random.shuffle(temp_pass_list)

password=""
for x in temp_pass_list:
    password+=x 

print(f"Your password is: {password}")