lst=[[1,2,3],[2,6,4],[3,4,5],[6,3,7]]

lst_unique = list()

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst_unique.count(lst[i][j])<1:
            lst_unique.append(lst[i][j])
            
print(lst_unique)

full_list = list()
lst_duplicates = list()
for i in range(len(lst)):
    for j in range(len(lst[i])):
        full_list.append(lst[i][j])
        
for i in full_list:
    if full_list.count(i)>1 and lst_duplicates.count(i)==0:
        lst_duplicates.append(i)
        
        
        
print(lst_duplicates)