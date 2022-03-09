def leap_year(year):
	if year % 4 != 0:
		print('平年')
	elif year % 4 == 0 and year % 100 != 0:
		print('閏年')
	elif year % 100 == 0 and year % 400 != 0:
		print('平年')
	elif year % 400 == 0 and year % 3200 != 0:
		print('閏年')
	else:
		print('我也不知道')

leap_year(int(input('查詢是否為閏年，您要查詢的年份是:')))