conversionrate = 0.45

x = int(input('Enter the number of Students'))
List = []
for i in range(x):
  List.append(int(input('enter the weight in lbs:')))

  output = [conversionrate*i for i in List]
  print("The list in Kilogram is:", output)


