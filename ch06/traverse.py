import os

with os.scandir('./chat')  as files:
    for file in files:
        print(file.name)