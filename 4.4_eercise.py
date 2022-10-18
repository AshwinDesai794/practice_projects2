

row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]

map= [row1,
      row2,
      row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure ?")
#pos = position.split()

row_pos = int(position[0])    #column
col_pos = int(position[1])      #row

map[row_pos-1][col_pos-1] = "X"

# print(map)
print(f"\n{row1}\n{row2}\n{row3}")