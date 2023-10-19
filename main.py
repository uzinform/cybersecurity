result = 0
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
     operator = input("Знак: ")    
     if operator == '+':
      result += operand    
      print(result)
      break
     elif operator == '-':
      result -= operand
      print(result)
      break
     elif operator == '*':
      result *= operand
      print(result)
      break
     elif operator == '/':
       if operand != 0:
          result /= int(operand)
          print(result)
          break
       else:
          print("Ділення на нуль!")
     elif operator == '=':
        print(result)
        break 
     else:
      print("Error!")   
  finally:
    if operand == "=" or operator == "=":    
      break        