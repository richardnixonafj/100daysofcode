# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#156 178 165 171 187

#Write your code below this row 👇
# count_heights = 0
# for student_height in student_heights:
#     count_heights += 1
# #print(count_heights)
# sum_height = 0
# for student_height in student_heights:
#     sum_height += student_height

# mean_height = round(sum_height / count_heights)

# print(f"your mean: {mean_height}")

# max_note_student = 0
# for student_height in student_heights:
#     if max_note_student < student_height:
#         max_note_student = student_height
            
# print(f"your max score: {max_note_student}")

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

#Write your code below this row 👇
# even_sum = 0
# for number in range(2, 101, 2):
#   # print(number)
#   even_sum += number
# print(even_sum)

# FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        #divisible by 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:
        #divisible by 3
        print("Fizz!")
    elif number % 5 == 0:
        #divisible by 5
        print("Buzz!")
    else:
        #undivisible by 3 and 5
        print(number)
