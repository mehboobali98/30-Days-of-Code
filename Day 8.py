# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

def read_input():
    lines = fileinput.input()
    n = int(lines[0])
    input_list = list()
    output_list = list()
    
    for i in range(1, n+1):
        input_list.append(lines[i])
        
    for line in lines:
        output_list.append(line)
    
    return input_list, output_list

def create_phonebook(input_list):
    phone_book = {}
    for line in input_list:
        line = line.split()
        phone_book.update({line[0]:line[1]})
    return phone_book

def find_contact(phone_book, output_list):
    for line in output_list:
        if line[-1:] == "\n":
            line = line[:-1]
        if line in phone_book:
            number = phone_book.get(line)
            print(line+"="+number)
        else:
            print("Not found")

if __name__ == '__main__':
    # function calls
    input_list, output_list = read_input()
    phone_book = create_phonebook(input_list)
    find_contact(phone_book, output_list)