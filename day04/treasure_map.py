row1   = ["o", "o", "o"]
row2   = ["o", "o", "o"]
row3   = ["o", "o", "o"]

map    = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}") 

pos    = (input("enter 2 digit number where you want to place the treasure.\nfirst digit is column and second digit is row"))
column = int(pos[0])-1
row    = int(pos[1])-1

map[row][column] = "x"
print(f"{map[0]}\n{map[1]}\n{map[2]}")
