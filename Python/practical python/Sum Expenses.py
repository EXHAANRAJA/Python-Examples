# To find expenses of all 12 months
expense = []
sum = 0
for i in range(0,12,3):
    exp = int(input("Enter the Expeses of Month " + str(i) + ":"))
    expense.append(exp)
    sum = sum + exp

print("The total expeses is :" + str(sum))
