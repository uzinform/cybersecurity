first_name = input("First name: ")
middle_name = input("Midle name: ")
last_name = input("Last name: ")

def get_fullname(first_name, middle_name, last_name): 
   empty = ""
   if middle_name == empty:
     return result
   elif first_name == empty:
     return data
   elif last_name == empty or first_name == empty or last_name == empty and first_name == empty:
     return data
   else:
     return fullname
   

fullname = f"{first_name} {middle_name} {last_name}"
result = f"{first_name} {last_name}"
data = f"You miss to input necessary data"

print(get_fullname(first_name, middle_name, last_name))