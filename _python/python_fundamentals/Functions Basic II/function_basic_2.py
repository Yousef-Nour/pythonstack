#1
def countdown(num):
    for i in range(num, 0, -1):
        print(i)
print (countdown(5))

#2
def print_and_return(arr):
    print(arr[0])
    return arr[1]

#3
def first_plus_length(arr):
    return arr[0] + len(arr)

#4
def values_greater_than_second(arr):
    temp = []
    if len(arr) <= 1:
        return False
    for i in arr:
        if arr[i] > arr[1]:
            temp.append(arr[i])
            print(len(temp))
            return temp

#5
def lengthAndValue(size, value):
    temp = []
    for i in range(0, size):
        temp.append(value)
        return temp