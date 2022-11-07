#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Maret', 'Magomed-Saleh', 'Petimat', 'Zeid', 'Saifullah']


# список списков приблизителного роста членов вашей семьи
my_family_height = [

    ['Maret', 165],
    ['Magomed-Saleh', 177],
    ['Petimat', 167 ],
    ['Zeid', 40],
    ['Saifullah', 27]
]


print('Рост матери - ', my_family_height[0][1], ' см')
print('Общий рост моей семьи - ', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]+ my_family_height[4][1], ' см')

# Выведите на консоль рост матери в формате
#   Рост матери - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
