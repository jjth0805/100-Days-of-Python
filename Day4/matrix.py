def matrix_run():
  # ๐จ Don't change the code below ๐
  row1 = ["โฌ๏ธ","โฌ๏ธ","โฌ๏ธ"]
  row2 = ["โฌ๏ธ","โฌ๏ธ","โฌ๏ธ"]
  row3 = ["โฌ๏ธ","โฌ๏ธ","โฌ๏ธ"]
  map = [row1, row2, row3]
  print(f"{row1}\n{row2}\n{row3}")
  position = input("Where do you want to put the treasure? ")
  # ๐จ Don't change the code above ๐

  #Write your code below this row ๐

  num1 = list(position)
  map[(int(num1[1])-1)][(int(num1[0])-1)] = "X"

  # ๊ณต๋ฐฑ์์ด ๋ฌธ์์ด๊ตฌ๋ถํ ๋ ex) 31 234 pizza์ ๊ฐ์ ๋ฌธ์์ด
  # ํด๋น๋ฌธ์์ด์ ๋ค์ํ๋ฒ list์ ๋ฃ๋๋ค ex) [3,1] [2,3,4] [p,i,z,z,a]์ ๊ฐ์ด ๋ณํ๋ค

  # instructor's answer
  # print(position)

  # horizontal = int(position[0])
  # vertical = int(position[1])

  # selected_row = map[vertical-1]
  # selected_row[horizontal -1] = "X"


  #Write your code above this row ๐

  # ๐จ Don't change the code below ๐
  
  print(f"{row1}\n{row2}\n{row3}")