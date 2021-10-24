#Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7

number =int(input("Введите число для операции"))
number_ver1 =number**3
number_ver2 =sum(map(int, str(number_ver1)))
number_ver3 =number_ver2%7
if number_ver3== 0:
    print(f'Ваше число в кубе {number_ver1}, сумма всех цифр ровна {number_ver2u} и оно нацело делиться на 7')
else:
    print("Число не входит в условие")