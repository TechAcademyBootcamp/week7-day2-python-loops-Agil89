array = input("ENter the numbers: ")

odd = 0
even = 0
for x in array.split(' '):
    if int(x)%2==0:
            even = even + 1
    else:
        odd = odd + 1
print('Count of even numbers: ',even)
print("Count of odd numbers: ",odd)