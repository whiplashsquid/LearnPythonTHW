import sys
script, input_encoding, error = sys.argv

# defines function main as taking parameters language_file, encoding and errors and assigning a line of text (read from file assigned to language_file) as a string to variable name 'line'
def main(language_file, encoding, errors):
    line = language_file.readline()
# if-statement tests truth of a variable and decides whether to run a piece of code if true or not if false. When line returns an empty string (e.g. at the end of the file) then the if statement will be false and will skip lines 10 & 12
    if line:
        # if true the function calls another function print_line using the parameters line, encoding and errors to print the line according to a set pattern
        print_line(line, encoding, errors)
        # then we return the same function main in a loop in order to read and print the next line - this will continue until line is empty and the if statement is false so we get out of the loop
        return main(language_file, encoding, errors)

# defines the function print_line which encodes each line from the languages.txt file and prints it to the screen
def print_line(line, encoding, errors):
    # strips the trailing \n on the line string and assigns the line without it to variable name next_lang
    next_lang = line.strip()
    # takes next_lang string and encodes it to get bytes using parameters assigned to variables encoding and errors
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # assign the inverse (by decoding raw_bytes using the same parameters) to the variable name cooked_string
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # prints both raw_bytes and cooked_string so we can see what they look like
    print(raw_bytes, "<===>", cooked_string)

# opens languages.txt file using encoding (set as utf-8) and assigns it to variable name languages
languages = open("languages.txt", encoding="utf-8")
# runs the main function with the correct parameters to get the loop kick started (i.e. the utf-8 encoded string assigned to variable languages, the encoding you passed to the script in the command line assigned to variable input_encoding, and the error handling you passed to the script in the command line assigned to variable error)
main(languages, input_encoding, error)
