from lexer import Lexer
import sys

def main():

    #get input and output file from command line. If there are no command line
    #arguments, use defaults
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = "input.txt"
    
    try:
        output_file = sys.argv[2]
    except IndexError:
        output_file = "output.txt"


    lex = Lexer()

    #read and parse input file line by line
    with open(input_file, "r") as f:
        line = f.readline()

        while line:
            lex.parse(line)
            line = f.readline()
    
    lex.write_to_file(output_file)

if __name__ == '__main__':
    main()
