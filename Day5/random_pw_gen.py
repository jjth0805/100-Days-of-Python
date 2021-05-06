import random
def pw_gen():
    #Password Generator Project
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  print("Welcome to the PyPassword Generator!")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  #Eazy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

  # random.choice() 리스트안에 있는 인자들을 랜덤으로 선택함

  # password=""
  # for letter_choice in range(0,nr_letters):
  #   letter_choice = letters[random.randint(0,51)]
  #   password += letter_choice
  # for symbol_choice in range(0, nr_symbols):
  #   symbol_choice = symbols[random.randint(0,8)]
  #   password += symbol_choice
  # for number_choice in range(0, nr_numbers):
  #   number_choice = numbers[random.randint(0,9)]
  #   password += number_choice

  # print(f"your password is {password}")

  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  password = []
  for letter_choice in range(0,nr_letters):
    letter_choice = letters[random.randint(0,51)]
    password.append(letter_choice)
  for symbol_choice in range(0, nr_symbols):
    symbol_choice = symbols[random.randint(0,8)]
    password.append(symbol_choice)
  for number_choice in range(0, nr_numbers):
    number_choice = numbers[random.randint(0,9)]
    password.append(number_choice)

  random.shuffle(password)
  answer = ""
  for pw in password:
    answer += pw
  print(f"your password is {answer}")