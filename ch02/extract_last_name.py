email = "John.Smith@uky.edu"
pos1 = email.find(".")
print(pos1)
pos2 = email.find("@")
print(pos2)
last_name = email[(1 + pos1):pos2]
print(last_name)

