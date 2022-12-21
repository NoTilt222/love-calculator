print("Welcome to the love calculator")

name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

final_name = name1 + name2

T = final_name.count('t')
R = final_name.count('r')
U = final_name.count('u')
E = final_name.count('e')
total1 = str(T + R + U + E)
L = final_name.count('l')
O = final_name.count('o')
V = final_name.count('v')
E = final_name.count('e')
total2 = str(L + O + V + E)

love_score = int(total1 + total2)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
