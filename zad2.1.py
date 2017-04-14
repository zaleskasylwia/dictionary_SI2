import csv

dictionary = {"FUNCTION": ("A series of statements which returns some value to a caller. ", "https://docs.python.org/3/glossary.html#term-function"),
                 "PARAMETR": ("co to parametr", "zrodlo p"),"VARIABLE": ("co to variable", "zrodlo v"), "ARGUMENT": ("co to argument", "zrodlo a"), 
                "DICTIONARY": ("co to dictionary", "zrodlo d"), "TUPLE": ("co to tuple", "zrodlo t"), 
                "ASCII table": ("co to ascii", "zrodlo asc"),"MODULE": ("co to module", "zrodlo m"),
                "LIST": ("co to list", "zrodlo l"),"CONDITIONAL": ("co to conditional", "zrodlo c"),
                "LOOPS": ("co to loops", "zrodlo lo"),"BUILT-IN": ("co to built-in", "zrodlo b"),
                "SLOTS": ("co to slots", "zrodlo s"),"GENERATORS": ("co to generators", "zrodlo g"),
                "CLASSES": ("co to classes", "zrodlo cl")}

with open('proba3.csv', 'w') as f:  #tworzy nowy plik i wpisuje zawartosc slownika
    w = csv.writer(f)
    for key, val in dictionary.items():
        w.writerow([key, val])


#add = {}    
    

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
    print(dictionary)
    with open('proba3.csv', 'w') as f:  #tworzy nowy plik i wpisuje zawartosc slownika
        w = csv.writer(f)
        for key, val in dictionary.items():
            w.writerow([key, val])


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

    