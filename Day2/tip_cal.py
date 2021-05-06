def tip_calculate():
  #If the bill was $150.00, split between 5 people, with 12% tip. 
  #Each person should pay (150.00 / 5) * 1.12 = 33.6
  #Format the result to 2 decimal places = 33.60
  #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
  #HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
  #HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
  initialBill = input("Welcome to the tip calculator.\nwhat was the total bill? $")
  percentage = input("What percentage tip would you like to give? 10,12 or 15? ")
  split = input("how many people to split the bill? ")
  newBill = float(initialBill)
  newPercentage = int(percentage)
  newSplit = int(split)
  bill_per_person = newBill*(1+ newPercentage/100)/newSplit
  # result = round(float(newBill + (newBill*newPercentage/100))/newSplit,2)
  result = "{:.2f}".format(bill_per_person)
  print(f"Each person should pay: ${result}")