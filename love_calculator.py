# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1=name1.lower()
lower_name2=name2.lower()

count_t=int(lower_name1.count("t"))+int(lower_name2.count("t"))
count_r=int(lower_name1.count("r"))+int(lower_name2.count("r"))
count_u=int(lower_name1.count("u"))+int(lower_name2.count("u"))
count_e=int(lower_name1.count("e"))+int(lower_name2.count("e"))

total_true=count_t+count_r+count_u+count_e

count_l=int(lower_name1.count("l"))+int(lower_name2.count("l"))
count_o=int(lower_name1.count("o"))+int(lower_name2.count("o"))
count_v=int(lower_name1.count("v"))+int(lower_name2.count("v"))


total_love=count_l+count_o+count_v+count_e

love_score=str(total_true)+str(total_love)
loved_score=int(love_score)

if loved_score<10 or loved_score>90:
    print(f"Your score is {loved_score},you go together like coke and mentos.")
elif loved_score >40 and loved_score<50:
    print(f"Your score is {loved_score},you are alright together.")
else:
    print(f"Your score is {loved_score}.")

