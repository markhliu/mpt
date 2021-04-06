import wikipedia

qs = input("What do you want to know?\n")
answer = wikipedia.summary(qs)
print(answer)

