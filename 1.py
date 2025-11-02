def swap_list(lst,num1,num2):
    lst[num1],lst[num2] = lst[num2],lst[num1]

#lst=[4,0,5,0,3,0,0,5]

lst = list(map(int,input("Введите список чисел: ").split()))
non_zero_index = 0


for i in range(len(lst)):
    if lst[i] != 0:
        swap_list(lst,non_zero_index,i)
        non_zero_index += 1
        
        
print(lst)