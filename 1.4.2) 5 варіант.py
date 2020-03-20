'''Інформація про вироби на складі містить дані про кількість в залежності від
розміру деталі і її кольору. Скласти програму, яка дозволить заносити і корегувати дані
про наявність деталей на складі при надходженні нової партії деталей. При цьому
повинна фіксуватися дата надходження деталей.'''

name_list = [] # задаємо пусті списки для наших даних
quantity_list = []
size_list = []
color_list = []
date_list = []

for i in range(1, int(input('Введіть кількість різних деталей: '))+1): # користувач вводить дані
    name_list.append(input(f'Введіть найменування {i}-ї деталі: '))
    quantity_list.append(input(f'Введіть кількість {i}-ї деталі: '))
    size_list.append(float(input(f'Введіть розмір {i}-ї деталі: ')))
    color_list.append(input(f'Введіть колір {i}-ї деталі: '))
    date_list.append(input(f'Введіть дату надходження на склад {i}-ї деталі: '))

print()
print('Дані про всі деталі:') # виводимо таблицю про всі деталі
for i in range (len(name_list)):
    print(f'Назва: {name_list[i]}; Кількість: {quantity_list[i]}; Розмір: {size_list[i]}; Колір: {color_list[i]}; Дата надходження: {date_list[i]};')

while True: # створюємо цикл з умовою для повторення питання щодо корегування даних
    print()
    print('Бажаєте корегувати дані?')
    question = input('(Так/Ні): ') # якщо користувач обирає "так", то ми корегуємо дані
    if (
            question == 'Так' or question == 'так' or question == 'Yes' or question == 'yes' or question == 'y' or question == '+'):
        name = input('Введіть назву деталі, яку потрібно змінити: ') # користувач вводить назву деталі, що потрібно корегувати
        for i in range(len(name_list)):
            if(name == name_list[i]): # за допомогою циклу for перевіряємо кожну назву, і якщо є співвпадіння - корегуємо дані по назві деталі
                copy_name = name_list[i] # створюємо копію даних про деталь, щоб повернути її у разі, якщо користувач залишить пусте поле (тобто дані не потрібно змінювати)
                copy_quantity = quantity_list[i]
                copy_size = size_list[i]
                copy_color = color_list[i]
                copy_date = date_list[i]
                name_list[i] = input('Введіть нову назву цієї деталі, якщо необхідно (інакше - залиште поле пустим): ') # питаємо нові дані про деталь та змінюємо їх, якщо поле - не пусте
                if(len(name_list[i]) == 0):
                    name_list[i] = copy_name
                quantity_list[i] = input('Введіть нову кількість цих деталей, якщо необхідно (інакше - залиште поле пустим): ')
                if (len(quantity_list[i]) == 0):
                    quantity_list[i] = copy_quantity
                size_list[i] = input('Введіть новий розмір цієї деталі, якщо необхідно (інакше - залиште поле пустим): ')
                if(len(size_list[i]) == 0):
                    size_list[i] = copy_size
                color_list[i] = input('Введіть новий колір цієї деталі, якщо необхідно (інакше - залиште поле пустим): ')
                if (len(color_list[i]) == 0):
                    color_list[i] = copy_color
                date_list[i] = input('Введіть нову дату надходження цієї деталі, якщо необхідно (інакше - залиште поле пустим): ')
                if (len(date_list[i]) == 0):
                    date_list[i] = copy_date
                print()
                print('Нові дані про всі деталі:') # виводимо оновлені дані про всі деталі
                for i in range(len(name_list)):
                    print(
                        f'Назва: {name_list[i]}; Кількість: {quantity_list[i]}; Розмір: {size_list[i]}; Колір: {color_list[i]}; Дата надходження: {date_list[i]};')
            else:
                print()
    elif (
            question == 'Ні' or question == 'ні' or question == 'No' or question == 'no' or question == 'n' or question == '-'): # якщо користувач не хоче корегувати дані про деталі, виводимо їх і припиняємо програму
        print()
        print('Дані про всі деталі:')
        for i in range(len(name_list)):
            print(
                f'Назва: {name_list[i]}; Кількість: {quantity_list[i]}; Розмір: {size_list[i]}; Колір: {color_list[i]}; Дата надходження: {date_list[i]};')
        exit(0)
    else: # якщо користувач вводить незрозумілу відповідь, перепитуємо його до тих пір, поки не буде "так" або "ні"
        print()
        print('Бажаєте корегувати дані?')