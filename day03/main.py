print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age < 21:
        bill = 12
        print("Please pay $12.")
    elif age > 45 or age < 55:
        bill = 0
        print("Free rialercoaster!!")

    wants_photo = input("Do you want a photo taken? Y or N. ")
   
    if wants_photo == "Y":
        bill = 3 + bill
       
    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

# ##################################################################
number = int(input("Wich number do you want to check?"))

#Write your code below this line

check = number % 2

if check > 0:
     print("é impar")
else:
    print("é par")

##################################################################

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight) / (height ** 2)

print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight!")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("obese")
elif bmi > 35:
    print("clinically obese")


#########################################################    

year = int(input("Which year do you want to check?"))

if year % 4 != 0:
    print("não é um ano bissexto")
elif year % 100 != 0:
    print("ano é bissexto")
elif year % 400 != 0:
    print("nao e bissexto")
else:
    print("é bisexto")

########################################################## 
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizza = 0

if size == "S":
    pizza = 15
elif size == "M":
    pizza = 20
else: 
    pizza = 25

if extra_cheese == "Y":
    pizza = (pizza + 1)
    
if size == "S" and add_pepperoni == "Y":
    pizza = pizza + 2

if add_pepperoni == "Y" and size != "S":
    pizza = pizza + 3

print(f"Preço total da pizza {pizza}")

###########################################################
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
lower_names = lower_name1 + lower_name2

count_names_t = lower_names.count("t")
count_names_r = lower_names.count("r")
count_names_u = lower_names.count("u")
count_names_e = lower_names.count("e")
check_true = count_names_t + count_names_r + count_names_u + count_names_e


count_names_l = lower_names.count("l")
count_names_o = lower_names.count("o")
count_names_v = lower_names.count("v")
count_names_e = lower_names.count("e")
check_love = count_names_l + count_names_o + count_names_v + count_names_e

score_final = str(check_true) + str(check_love) 
score_final = int(score_final)

if score_final < 10 and score_final > 90:
    print("Your score is x, you go together like coke and mentos!")
elif score_final <= 40 and score_final >= 50:
    print("Your score is y, you are alright together.")
else:
    print("You score is z.")
