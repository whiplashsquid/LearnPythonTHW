from sys import argv

script, filename = argv

txt = open(filename)

print(f"This is the contents of {filename}")
print(txt.read())
print(f"If you want to close {filename}, press RETURN. If not use CTRL-C to end the script. (You should always close the file!)")
input("?")
txt.close()
print("We have now closed the file.")
