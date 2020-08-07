import time
import operator
import string


def open_file():
    """
    Opens the file 

    :return: file object to a text file 
    """
    while True:
        try:
            file_name = input("File name: ")
            file_obj = open(file_name.strip())
            break
        except FileNotFoundError:
            print("\nFile not found. Try a different file.")

    return file_obj


def parse_file(file_obj):
    """
    Parses the file and returns a dictionary of chars to ints 

    :param file_obj: file object to be parsed 
    :return: a dictionary of characters to ints by frequency 
    """
    chars_dict = {}

    for line in file_obj:
        for char in line:
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1

    return chars_dict

def pretty_print(chars_dict): 
    """
    Does a pretty print to show how frequent each character is

    :param chars_dict: dictionary of chars to ints of frequency it showed up 
                       in the input file 
    """

    chars = [(key, value) for key, value in chars_dict.items()]
    chars.sort(key = operator.itemgetter(1), reverse=True)

    print("------------------------")
    print("      char | freq  ")
    print("-----------|------------")
    for char, freq in chars: 
        if char == "\n": 
            print("    Return | {}     ".format(freq))
        elif char == "\t": 
            print("       Tab | {}     ".format(freq))
        elif char == " ": 
            print("     Space | {}     ".format(freq))
        else: 
            print("         {} | {}     ".format(char, freq))

    return None 


def main():
    file_obj = open_file()

    start_time = time.time()
    chars_dict = parse_file(file_obj)
    print("\nParsing time: {} seconds".format(time.time() - start_time))

    pretty_print(chars_dict)

    file_obj.close()
    return None

if __name__ == "__main__":
    main()

