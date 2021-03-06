"""
Simple Operations and Calculations - Exercise
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1160#0

06. Charity Campaign

Условие:
В сладкарница се провежда благотворителна кампания за събиране на средства, в която могат да се включат сладкари
от цялата страна. Първоначално прочитаме от конзолата броя на дните, в които тече кампанията и броя на сладкарите,
които ще се включат. След това на отделни редове получаваме количеството на тортите, гофретите и палачинките,
които ще бъдат приготвени от един сладкар за един ден. Трябва да се има предвид следния ценоразпис:
Торта - 45 лв.
Гофрета - 5.80 лв.
Палачинка – 3.20 лв.
1/8 от крайната сума ще бъде използвана за покриване на разходите за продуктите по време на кампанията.
Да се напише програма, която изчислява сумата, която е събрана в края на кампанията.
Вход
От конзолата се четат 5 реда:
1.	Броят на дните, в които тече кампанията – цяло число;
2.	Броят на сладкарите – цяло число;
3.	Броят на тортите – цяло число;
4.	Броят на гофретите – цяло число;
5.	Броят на палачинките – цяло число.
Изход
Да се отпечата на конзолата едно число:
парите, които са събрани, форматирани до втория знак след десетичната запетая
"""

days = int(input())
chefs = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cakes_1_day_total = cakes * 45.0
waffles_1_day_total = waffles * 5.80
pancakes_1_day_total = pancakes * 3.20

total_1_day = (cakes_1_day_total + waffles_1_day_total + pancakes_1_day_total) * chefs
total = total_1_day * days

money_left = total - (total / 8)

print(f"{money_left:.2f}")
