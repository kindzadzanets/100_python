row1 = ['🟨', '🟨', '🟨']
row2 = ['🟨', '🟨', '🟨']
row3 = ['🟨', '🟨', '🟨']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Give a coordinates as XY:\n")
row_x = int(position[0])
column_y = int(position[1])

if 0 < row_x < 4 and 0 < column_y < 4:
	map[row_x - 1][column_y - 1] = "🕓"
	print(f"{row1}\n{row2}\n{row3}")
else:
	print("Here is 3 rows and 3 columns!")