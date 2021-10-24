duration = int(input('Ведите время в секуднах: '))
s = duration
m = duration%60
h = duration%3600
d = duration%86400
m_1 = h//60
h_1 = d//3600
d_1 = duration//86400
if duration<60:
    print(f'Ваше число это: {m} секунд')
elif duration<3600:
    print(f'Ваше число это: {m_1} - минут и {m} секунд')
elif duration<=86399:
    print(f'Ваше число это: {h_1} -часов {m_1} - минут и {m} секунд')
elif duration>=86400:
    print(f'Ваше число это: {d_1} - дней {h_1} -часов {m_1} - минут и {m} секунд')