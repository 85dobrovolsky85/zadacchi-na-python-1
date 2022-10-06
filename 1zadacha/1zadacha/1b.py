# bool
# print('X Y Z')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             if not(x or y or z) = not x and not y and not z:
#                 print(x,y,z,)
print('y', 'x', 'z', 'F') #Напечатаем заголовки таблицы
for y in range(2): #Берём все переменные и меняем их в циклах '0' и '1'
	for x in range(2):
		for z in range(2):
			for w in range(2):
				F = not (x or y or z) = not x and not y and not z #Записываем функцию
				print(x, y, z, F) #Выводим результат