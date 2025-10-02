#Уроки Python с нуля / #6 – Циклы и операторы в них (for, while)
# for i in range(4):
#     print(i)

#############################################################

# for i in range(1, 4):
#     print(i)

#############################################################
# for i in range(1,12,2):
#     print(i)

#############################################################
# word = "Hello World!"
# for i in word:
#     if i == "!":
#         print("Yes")
#     #else: print("No")


#############################################################
# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "l":
#         count += 1
# print("Count is: ", count)

#############################################################
# i = 5
# while i < 15:
#     print(i)
#     i += 2
#
# isHasCar = True
#
# while isHasCar:
#     if input("Enter data: ") == "Stop":
#         isHappy = False

#############################################################
#break
for i in range(1,11):
    print(i)

for i in range(1,11):
    if i == 5:
        break
    #break will lead to stop the loop

    if i % 2 == 0:
        continue
    #will stip iteration. in our case 2 and 4 will be stipped and not printed

    print(i)



#############################################################

#############################################################

#############################################################