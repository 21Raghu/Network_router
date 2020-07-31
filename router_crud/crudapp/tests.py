
num = (input('Enter the number: '))

if sum([int(i) ** len(num) for i in num]) == int(num):
    print (num, 'is a Armstrong number')
else:
    print (num, 'is NOT Armstrong number')

'''testcase = int(input())
input_num=[]
for i in range(testcase):
    x = int(input())
    input_num.append(x)

compa = input_num

for i in range(testcase):
    sum = 0
    p=compa[i]
    while input_num[i]:
        sum += (input_num[i] % 10)**3
        input_num[i] = int(input_num[i] /10)

    if sum == p:
        print("this is armstrong number")
    else:
        print("this is not armstrong number")
'''
