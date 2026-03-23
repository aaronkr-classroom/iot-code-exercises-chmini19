# 3_list.py

my_list = [10, 20, 30, 40]

print(my_list[0])
print(my_list[2])


my_list.append(50)
print(my_list)

my_list.insert(1,15)
print(my_list)

my_list.remove(30)
print(my_list)

del my_list[2]
print(my_list)

print(len(my_list))

for item in my_list:
    print(item)

sub_list = my_list[1:3]
print(sub_list)

for i in range(6, 15, 2):
    my_list.append(i *10)
    
print(my_list)

sub_list_2 = my_list[4:]
sub_list_3 = my_list[:4]
sub_list_4 = my_list[2:7:2]
sub_list_5 = my_list[::]

print(f"s2: {sub_list_2}")
print(f"s3: {sub_list_3}")
print(f"s4: {sub_list_4}")
print(f"s5: {sub_list_5}")
