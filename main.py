#Чистая доска для развелечений. Поехали!
simvol = int(input('Введите цифру:'))

simvol2 = input('Выберите действие:+-/*:')

simvol3 = int(input('Введите цифру:'))

result = ''

if simvol2 =='+':
    result = simvol + simvol3
elif simvol2=='-':
    result = simvol - simvol3
elif simvol2=='/':
    result = simvol / simvol3
elif simvol2 =='*':
    result = simvol * simvol3
else:
    print('такого действия нету в калькуляторе')

print('Ответ:', result)

