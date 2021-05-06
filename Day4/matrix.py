def matrix_run():
  # 🚨 Don't change the code below 👇
  row1 = ["⬜️","⬜️","⬜️"]
  row2 = ["⬜️","⬜️","⬜️"]
  row3 = ["⬜️","⬜️","⬜️"]
  map = [row1, row2, row3]
  print(f"{row1}\n{row2}\n{row3}")
  position = input("Where do you want to put the treasure? ")
  # 🚨 Don't change the code above 👆

  #Write your code below this row 👇

  num1 = list(position)
  map[(int(num1[1])-1)][(int(num1[0])-1)] = "X"

  # 공백없이 문자열구분할때 ex) 31 234 pizza와 같은 문자열
  # 해당문자열을 다시한번 list에 넣는다 ex) [3,1] [2,3,4] [p,i,z,z,a]와 같이 변한다

  # instructor's answer
  # print(position)

  # horizontal = int(position[0])
  # vertical = int(position[1])

  # selected_row = map[vertical-1]
  # selected_row[horizontal -1] = "X"


  #Write your code above this row 👆

  # 🚨 Don't change the code below 👇
  
  print(f"{row1}\n{row2}\n{row3}")