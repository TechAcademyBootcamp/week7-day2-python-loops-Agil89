number = input('Enter the number: ')
while not  number.isdigit() or int(number)<0:
    number = input("Enter again:")
splitting = input('Enter the split number: ')
while not  splitting.isdigit() or int(splitting)<0 or len(number)%int(splitting)!=0:
    splitting = input("Enter again:")
splitting = int(splitting)
l = []
while len(number)>=0:
    l.append(number[:splitting])
    if len(number)<=splitting:
        break
    number = number[splitting:]
for x in l:
    print(x,end=' ')
l2=sorted(l)
if l==l2:
    print('\nARTANDIR')
else:
    print('\nArtan deil')