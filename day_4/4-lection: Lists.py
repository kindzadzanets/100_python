# СПИСОК штатов по дате присоединения, сохраненный в переменную usa - может состоять из разных типов данных. https://docs.python.org/3/tutorial/datastructures.html
usa = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Отобразить элемент списка под номером [индекс] - начинается с 0
print(usa[0]) # отобразить первую позицию в списке
print(usa[1]) # отобразить вторую позицию списка

print(usa[-1]) # отобразить последний элемент (первый с конца)
print(usa[-5]) # отобразить пятый с конца элемент

usa[2] = "Нью Джерси" # изменить конкретный элемент списка
# print(usa)

usa.append("Светланкино Королевство") # добавить один элемент в конец списка
# print(usa)

usa.extend(["Витино", "Жорено", "Дятлово"]) # добавить [несколько элементов] в конец списка (наиболее удобная команда)
print(usa)