# #Уроки Python с нуля / #7 – Списки (list). Функции и их методы
# nums = [5,7, "apple", -1, 2.4]
# print(nums)
#
# #to change a value of element us index to point it
# nums[2] = 333
# print(nums)
#
# #to print element from list point to index of it
# print(nums[2])
#
# #list can include a list in it
# listInlist = [1,2,3, [4,4,4],[True, False, True]]
# print(listInlist)
# print(listInlist[4]) #or other syntax
# print(listInlist[-1])
# print(listInlist[4][1])
# print(listInlist[-1][1])

# #list's usefull functions
# #add value to list after it's created. it will add new value at the end of list
num = [1,2,3]
# print(num)
# num.append(4)
# print(num)
#
# #add value to a speacal index
# num.insert(1,4)
# print(num)

#add several values to list
num.extend([16,7,True,False])
# print(num)
# num.sort()
# print(num)
# num.reverse()
# print(num)
#
#to delete last element use pop()
# num.pop()
# print(num)
# #to remove element with special value
# num.remove(True)
# print(num)
# #to delete element by index
# num.pop(0)

# print(num)
#
# #clear() will clean the list
# #num.clear()
# #print(num)
#
# #count will retrieve the number of how many 'true' values are there in the list
# print(num.count(True))
# #len will retrieve the length of the list
# print(len(num))

#writing loop for list
# nums = [5,2,7,"50", False]
#
# for element in nums:
#     print(element)

n = int(input("enter length for the list: "))

user_list = []

i = 0
while i < n:
    string = "enter element number " + str(i+1) + ": "
    user_list.append(input(string))
    i += 1
    print(user_list)

print(user_list)
