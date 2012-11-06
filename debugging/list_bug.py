empty_list = []
list_of_lists = []

for x in range(0, 5):
    list_of_lists.append(empty_list)

for index, list in enumerate(list_of_lists):
    list.append(index)

print list_of_lists