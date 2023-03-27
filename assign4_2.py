list_inp= input('Enter the numbers for list: ').split() #taking input from user
#print(list_inp)
list_int= map(int, list_inp) #converting the string to integers
list1= list(list_int)
print('Input user: ',list1)
list2=[]
for i in list1:
    list2.append(i*3)

print('Multiplied by 3: ',list2)