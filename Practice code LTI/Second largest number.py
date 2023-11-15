
# # second largest numbers

# def second_largest(given_list):
#     largest = None
#     second_largest =None
#     for current_number in given_list:
#         if largest == None:
#             largest = current_number
#         elif current_number>largest:
#             second_largest = largest
#             largest = current_number
#         elif second_largest == None:
#             second_largest = current_number
#         elif current_number > second_largest:
#             second_largest = current_number
#     return second_largest

# print("The seecond largest number in [1,3,4,5,0,2]")
# print(second_largest([1,3,4,5,0,2]))
                                        ###### OR #######
#  for single list 
list1 = [1,3,4,5,0,2]
new_list = set(list1)
new_list.remove(max(new_list))
print(max(new_list))

#  for Multiple list
list1 = [1,3,4,5,0,2]
list2 = [8,9,4,5,6,7,23]
new_list = set(list1+list2)
new_list.remove(max(new_list))
print(max(new_list))