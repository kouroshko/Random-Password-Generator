import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVZXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+=-."

string = lower + upper + numbers + symbols
length = 15

password = "".join(random.sample(string, length))

print("Password : " + password)
