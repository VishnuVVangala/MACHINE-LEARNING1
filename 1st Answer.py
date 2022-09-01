ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
a = min(ages)
b = max(ages)
print(a)
print(b)
ages.append(a)
print(ages)
ages.append(b)
print(ages)
length = len(ages)
print(length)
median1 = (length-1)//2
print(median1)
median2 = (ages[median1]+ages[median1+1])/2
print(median2)
sum1 = sum(ages)
print(sum1)
avg = sum1/length
print(avg)
rangelist = b-a
print(rangelist)
