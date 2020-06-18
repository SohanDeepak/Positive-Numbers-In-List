num = int(input("Enter the number of elements of list: "))
input_list = []
print("Enter the elements:\n")
for i in range(0,num):
    element = int(input())
    input_list.append(element)
    
final_list = []
num = 0

while (num < len(input_list)):
    if input_list[num] > 0:
        final_list.append(input_list[num])

    num += 1    

print(final_list)    
