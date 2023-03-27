list1= (input('Enter the numbers:')).split()
list2= list(map(int,list1))

square= lambda x: x*x
list3=map(square,list2)
print('Input from the user: ',list2)
print('Square of given numbers: ',list(list3))