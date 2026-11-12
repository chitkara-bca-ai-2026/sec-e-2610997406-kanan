sen=input("enter a sentence:")

ind=int(input("enter index to print"))
print(f"char at {sen} = {sen[ind]}")

st=int(input("enter start index"))
en=int(input("enter end index"))
print(f"slcie from{st} to {en} is {sen[st:en]}")

print(f"uppercase: {sen.upper()}")
print(f"lowercase: {sen.lower()}")

key=input("enter word to replace:")
repl=input("enter replacement word:")
repstr=sen.replace(key,repl)
print(f"replaced: {repstr}")

print(f"length: {len(repstr)}")