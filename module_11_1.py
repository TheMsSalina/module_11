import matplotlib.pyplot as plt
import pandas as pd
import requests

#Requests — это библиотека, которая позволяет взаимодействовать с веб-ресурсами и интернет
#(для работы со всеми видами HTTP-запросов)

response = requests.get('https://api.github.com')
print(response.json())
print("\n код requests \n")

#Pandas — это библиотека для анализа уже структурированных данных
#Сортировака строк и выделение подмножеств, вычисление сводной статистики

Data = [11, 13, 17, 19, 23]
s = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e']
si = pd.Series(Data, Index)
print(si)
print("\n код pandas  \n")

#Matplotlib — это библиотека для визуализации данных, для создания графиков

x = [1, 3, 5, 7]
y = [2, 4, 6, 8]

plt.plot(x, y, marker='1')

plt.title('График')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()
print("\n код matplotlib  \n")