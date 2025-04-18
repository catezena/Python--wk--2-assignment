my_list = []
# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)      
my_list.append(40)
print("my list after appending",my_list)

# Insert elements to the list

my_list.insert(1, 15)
print("my list after inserting 15",my_list)
# Extend the list
my_list.extend([50, 60, 70])
print("my list after extending",my_list)
# Remove elements from the list
my_list.pop()
print("my list after popping",my_list)
# sort the list
my_list.sort()
print("my list after sorting",my_list)

print("finding index of 30: ",my_list.index(30))