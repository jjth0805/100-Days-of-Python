def treasure_game():
  from Day3.art import logo
  print(logo)
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.") 

  #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
  answer1 = input('Do you want to go "left" or "right"?\n').lower()
  if answer1 == "right":
    print("You fall into a hole game over")
  else:
    answer2 = input("Do you want to swim or wait for a boat? Please make sure you type either swim or wait\n").lower()
    if answer2 == "swim":
      print("You are attacked by a trout. Game over")
    else: 
      answer3 = input("You now have reached to the door. Which color do you choose red, yellow or blue\n").lower()
      if answer3 == "yellow":
        print("you win!")
      elif answer3 == "red":
        print("Burned by fire. Game over")
      else:
        print("eaten by beasts")