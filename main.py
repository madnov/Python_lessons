array = [-3, -2, -1, 0, 1, 2, 3]
for j in range(2):
    for i in range(len(array) - 1, 0, -1):
        temp = array[i]
        array[i] = array[i - 1]
        array[i - 1] = temp
        
print(array)

