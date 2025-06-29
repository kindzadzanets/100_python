
def is_leap(year):
	"""Функция определения високосности года, если год високосный, функция возвращает True."""
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False


def days_in_month(year, month):
	"""Функция вычисления количества дней в месяце: если год високосный, к февралю будет прибавлен один день."""
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if month in range(1, len(month_days) +1):
		if is_leap(year):
			month_days[1] += 1
		return month_days[month - 1]
	else:
		return f"Месяцев всего 12, введи значение от 1 до 12!"


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)