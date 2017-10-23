from sys import argv

script, from_file, to_file = argv

in_file = open(from_file)
indata = in_file.read()
out_file = open(to_file, 'w')
out_file.write(indata)

print(f"Copied from {from_file} to {to_file}.")

out_file.close()
in_file.close()
