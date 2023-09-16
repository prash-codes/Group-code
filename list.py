list1= ["item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8"]
print(list1)
len_list = len(list1)
print(len_list)
print(list1[0])
print(list1[len_list - 3] )
find_index_of_item = input("enter any item name in the above list: \n")
print ("the index number of item you entered is ")
print(list1.index(find_index_of_item))