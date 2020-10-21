num = int(input())
num_list = []
for i in range(num): 
    ele = int(input()) 
    num_list.append(ele)

sorted_list = []
while num_list:
    minimum = num_list[0]
    for i in num_list:
        if i < minimum:
            minimum = i
    sorted_list.append(minimum)
    num_list.remove(minimum)

print (sorted_list)
print (num_list)

