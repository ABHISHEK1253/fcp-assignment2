import random
content=open("fortune.txt").read()
quotes = content.split("%")
print(random.choice(quotes))
