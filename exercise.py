# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import pandas as pd

data = pd.read_csv('titanic.csv')
#data[:1]
print("Проверка на случайной серии")
l = [1,3,5,6,8]
s =  pd.Series(l)
print(s)
print("Информация о наборе данных: ")
print(s.describe())
print(s[1])
print(data.index)
print(data.columns)
print(data['Age'])
print("Медиана: ")
print(data['Age'].median())
print("Среднее: ")
print(data['Age'].mean())
