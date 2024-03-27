# простые числа до 500:
# 2	 3	5	7	11	13	17	19	23	29	31	37	41	43	47	53	59	61	67	71
# 73 79	83	89	97	101	103	107	109	113	127	131	137	139	149	151	157	163	167	173
# 179 181	191	193	197	199	211	223	227	229	233	239	241	251	257	263	269	271	277	281
# 283 293	307	311	313	317	331	337	347	349	353	359	367	373	379	383	389	397	401	409
# 419 421	431	433	439	443	449	457	461	463	467	479	487	491	499

# Проверялка на простоту числа
# Write your code below this line 👇
def prime_checker(number):
	count = 0
	for divider in range(1, n +1):
		if n % divider == 0:
			count +=1
			print(count)
	if count == 2:
		print(f"{n} - простое число")
	else:
		print(f"{n} - составное число")

# изящное решение:
# def prime_checker(number):
# 	prime = True
# 	for divider in range(2, n):
# 		if n % divider == 0:
# 			prime = False
# 	if prime:
# 		print(f"{n} - простое число")
# 	else:
# 		print(f"{n} - составное число")




# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


