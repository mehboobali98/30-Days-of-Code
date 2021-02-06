# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

def get_input():
    lines = fileinput.input()
    n = int(lines[0])
    strings = list()
    
    for i in range(1, n+1):
        strings.append(lines[i])
    
    return strings

def get_strings(strings):
    new_strings = list()
    
    for string in strings:
        even_str = ""
        odd_str =""
        for i in range(len(string)):
            if string[i] == "\n":
                continue
            elif i%2==0:
                even_str = even_str+string[i]
            else:
                odd_str = odd_str+string[i]
        new_strings.append(even_str + " " + odd_str)
    return new_strings

def print_strings(strings):
    for string in strings:
        print(string)
    
if __name__ == '__main__':
    strings = get_input()
    new_strings = get_strings(strings)
    print_strings(new_strings)