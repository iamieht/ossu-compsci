number = int(input('Enter a decimal number: '))
num = number
if number < 0:
    isNeg = True
    number = abs(number)
else:
    isNeg = False

result = ''
if number == 0:
    result = '0'
while number > 0:
    result = str(number % 2) + result
    number = number // 2

if isNeg:
    result = '-' + result

print('Decimal number: ' + str(num) + ' is ' + result + ' in binary')