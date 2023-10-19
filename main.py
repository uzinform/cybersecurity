result = None
operand = None
operator = None
wait_for_number = True

while True: 
  operand = input("Введіть число: ")  
  try:
     operand = int(operand)  
  except Exception:
    print("Введений вами символ - це не число!")   
  else: 
   while True: 
    operator = input("Введіть знак +, -, * або /: ")  
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
      print(operator)
      break
    elif operator == "=":
      break
    else:
      print("Ви ввели не вірний знак!")
  finally:
    if operand == "=" or operator == "=":      
      print("Ваш результат: ")
      break    