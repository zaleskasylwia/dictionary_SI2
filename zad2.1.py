import csv
'''dictionary = {"FUNCTION": ("A series of statements which returns some value to a caller. ", "https://docs.python.org/3/glossary.html#term-function"),
                 "PARAMETR": ("A named entity in a function definition that specifies an argument that the function can accept", "https://docs.python.org/3/glossary.html#term-parameter"),
                 "VARIABLE": (" A variable is a location in memory used to store some data (value). ", "https://www.programiz.com/python-programming/variables-datatypes"), 
                 "ARGUMENT": ("A value passed to a function (or method) when calling the function", "https://docs.python.org/3/glossary.html#term-argument"), 
                "DICTIONARY": ("An associative array where arbitrary keys are mapped to values.", "https://docs.python.org/3/glossary.html#term-dictionary"), 
                "TUPLE": ("Object similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas in a list  elements can be changed.", "https://www.programiz.com/python-programming/tuple"), 
                "ASCII table": ("ASCII stands for American Standard Code for Information Interchange. ASCII code is the numerical representation of a characters.", "http://www.asciitable.com/"),
                "MODULE": ("An object that serves as an organizational unit of Python code", "https://docs.python.org/3/glossary.html#term-module"),
                "LIST": ("A built-in Python sequence.", "https://docs.python.org/3/glossary.html#term-list"),
                "STRING": (" A string is a sequence of characters.", "https://www.programiz.com/python-programming/string"),
                "METHOD": ("A function which is defined inside a class body.", "https://docs.python.org/3/glossary.html#term-method"),
                "LOOP": ("Loops are used in programming to repeat a specific block of code.", "https://www.programiz.com/python-programming/while-loop"),
                "IMMUTABLE": ("An object with a fixed value. Immutable objects include numbers strings and tuples.", "https://docs.python.org/3/glossary.html#term-immutable"),
                "ITERABLES": ("An object capable of returning its members one at a time.", "https://docs.python.org/3/glossary.html#term-iterable"),
                "VCS": ("A component of software configuration management version control system also known as revision control or source control", "https://en.wikipedia.org/wiki/Version_control")}'''

'''with open('data.csv', 'w') as csv_file:  #tworzy nowy plik i wpisuje zawartosc slownika
    w = csv.writer(csv_file)
    for key, val in dictionary.items():
        w.writerow([key, val])'''





with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    dictionary = dict(reader)

#1
def search():
    print("Enter appellation of the definition")
    name = input().upper()
    if dictionary.get(name):
        print(dictionary.get(name))
    else:
        print("Dictionary don't have this definition")




#1
def search():
    print("Enter appellation of the definition")
    name = input().upper()
    if dictionary.get(name):
        print(dictionary.get(name))
    else:
        print("Dictionary don't have this definition")

#2
def adding():
    print("Tell me a definition")
    definition = input().upper()
    print("Tell me explanation")
    explanation = input()
    print("Tell me source")
    source = input()
    dictionary[definition] = (explanation, source) #dodaje do slownika moja nowa definicje
    #print(dictionary)
    with open('data.csv', 'w') as csv_file:                        
        writer = csv.writer(csv_file)
        for key, value in dictionary.items():
            writer.writerow([key, value])


#3
def show_all():
    for definition in sorted(dictionary.items()):
        print(definition[0])

#4
def show_available():
    print("Type me first letter of a word")
    key_first_letter = input().upper() 
    if len(key_first_letter) == 1:
        for definition, explanation in sorted(dictionary.items()):
            if definition[0] == key_first_letter:
                print(definition,explanation)
    else:
        print("Type me just one letter")


def main():
    while True:
        # read_from_csv("nazwa.csv")
        print("Dictionary for a little programmer:")
        print("1 - search")
        print("2 - add")
        print("3 - show all appellations alphabetically")
        print("4 - show all by first letter")
        print("0 - exit")
        print("Tell me a number from 0 to 4")

        #input_read = int(input()) #nie odporny na dupa
        input_read = input()
        #yes = input_read.isdigit()
        if input_read.isdigit():
            #print ("ok")
            input_read = int(input_read)
        else: 
            print("It's not a number from 0 to 4")
        

        
        #while yes:
        if input_read == 1:
            search()
        elif input_read == 2:
            adding()
        elif input_read == 3:
            show_all()
        elif input_read == 4:
            show_available()
        elif input_read == 0:
            return
        else:
            print("In menu no such a number, try again'\n") 



        ask = ""
        while not (ask == 'YES' or ask== 'NO'):                                     #ask about game again
            ask = input("Do you want to try again? (YES/NO) ").upper()
        if ask == 'NO':
            break

main()

    