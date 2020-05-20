height = int(input('Enter the height of the tree: '))
speed = int(input('Enter the speed of ilbiz: '))
surus = int(input('Enter the surus of ilbiz: '))

way_of_day = 0
counter_of_days = 0
while way_of_day<height:
    way_of_day = way_of_day + speed
    counter_of_days = counter_of_days + 1
    if way_of_day>=height:
        break
    way_of_day= way_of_day-surus
    print(way_of_day)
print(counter_of_days)