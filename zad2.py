import csv
'''
""dictionary = {"FUNCTION": ("A series of statements which returns some value to a caller. ", "https://docs.python.org/3/glossary.html#term-function"),
                 "PARAMETR": ("co to parametr", "zrodlo p"),"VARIABLE": ("co to variable", "zrodlo v"), "ARGUMENT": ("co to argument", "zrodlo a"), 
                "DICTIONARY": ("co to dictionary", "zrodlo d"), "TUPLE": ("co to tuple", "zrodlo t"), 
                "ASCII table": ("co to ascii", "zrodlo asc"),"MODULE": ("co to module", "zrodlo m"),
                "LIST": ("co to list", "zrodlo l"),"CONDITIONAL": ("co to conditional", "zrodlo c"),
                "LOOPS": ("co to loops", "zrodlo lo"),"BUILT-IN": ("co to built-in", "zrodlo b"),
                "SLOTS": ("co to slots", "zrodlo s"),"GENERATORS": ("co to generators", "zrodlo g"),
                "CLASSES": ("co to classes", "zrodlo cl")}""'''


'''with open('dictionary.csv', 'w') as f:  
    w = csv.DictWriter(f, dictionary.keys())
    w.writeheader()
    w.writerow(dictionary)
    '''

datafile = open('dictionary.csv')   #otwiera i zczytuje dane z pliku csv
database = datafile.readlines() 
datafile.close()

database_list = [line.split(' | ') for line in database] #dzieli je przez znak
dictionary = {line[0]:(line[1],line[2]) for line in database_list}   #zamienia string i wpisuje do slownika
    
    

#1
def search():
    print("Enter the name of the definition")
    name = input().upper()
    if dictionary.get(name):
        print(dictionary.get(name))
    else:
        print("Dictionary don't have this definition")

#2
def add():
    new_dict= []
    definition = input("Tell me a definition: " '\n').upper()
    new_dict.append(definition)
    explanation = input("Type explanation of definition: " '\n')
    new_dict.append(explanation)
    source = input('Type source of information: ') + '\n'
    new_dict.append(source)
    dictionary[new_dict[0]] = (new_dict[1], new_dict[2]) #dodaje nowa definicje do slownika
    datafile = open('dictionary.csv', 'a')  #wrwpisuje do csv
    datafile.write(' | '.join(new_dict))
    datafile.close()
    #print(dictionary)



#3
def show_all():
    for definition in sorted(dictionary.items()):
        print(definition[0])

#4
def show_available():
    print("Tell me first letter of a word")
    key_first_letter = input().upper() 
    if len(key_first_letter) == 1:
        for definition, explanation in sorted(dictionary.items()):
            if definition[0] == key_first_letter:
                print(definition,explanation)
    else:
        print("Tell me just one")


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
            add()
        elif input_read == 3:
            show_all()
        elif input_read == 4:
            show_available()
        elif input_read == 0:
            return
        else:
            print("In menu no such a number, try again'\n") #zeby wracało???

        #else:
            #print("Type a number from 0 to 4")

        ask = ""
        while not (ask == 'YES' or ask== 'NO'):                                     #ask about game again
            ask = input("Do you want to try again? (YES/NO) ").upper()
        if ask == 'NO':
            break

main()

    
