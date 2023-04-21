import re

while True:
  a = input("Enter a password : ")
  v = False

  if (len(a)<16):
    print("Your password is too small! Total characters should be greater than 16")
    continue

  elif not re.search("[A-Z]",a):
    print("Your password do not have capital letters ! It should contain at least one letter between [A-Z]")
    continue

  elif not re.search("[a-z]",a):
    print("Your passwords do not have small letters ! It should contain at leat one letter between [a-z]")
    continue

  elif not re.search("[1-9]",a):
    print("Your passwords do not have digits ! It should contain at leat one digit between [0-9]")
    continue

  elif not re.search("[~!@#$%^&*]",a):    
    print("Your password do not have special character ! It should contain at least one character in [~!@#$%^&*]")
    continue

  elif re.search("[\s]",a):
    print("Your password contains spaces ! It should not contain any space")
    continue

  else:
    v = True
    break

if(v):
  print("Password is strong and valid")

