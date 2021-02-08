#2. Check if the input is a valid integer - Use exception

userInput = 0
while True:
  try:
     userInput = int(input("Enter something: "))       
  except ValueError:
     print("Not an integer!")
     continue
  else:
     print("Yes an integer!")
     break 



