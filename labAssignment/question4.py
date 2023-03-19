number = int(input("Enter the number: "))  
store = [] #an empty list  
for i in range(number):  
  store.append([])  
  store[i].append(1)  
  for j in range(1, i):  
    store[i].append(store[i - 1][j - 1] + store[i - 1][j])  
  if(number != 0):  
    store[i].append(1)  
for i in range(number):  
  print(" " * (number - i), end = " ", sep = " ")  
  for j in range(0, i + 1):  
    print('{0:6}'.format(store[i][j]), end = " ", sep = " ")  
  print() 