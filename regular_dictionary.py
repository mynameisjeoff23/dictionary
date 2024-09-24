second = True
DIRECTORY = "dictionary.txt"
def main():
    '''
        Main logic of the dictionary. Calls first_term() to find term definition.
        Calls subsequent() and usage() forever until it is sure there are no more similar terms.
    '''
    global search_term
    found = False
    print("Enter a word to seach in the dictionary: ", end='')
    while found == False:
        search_term = input().lower()
        global definition
        with open(DIRECTORY, "r", encoding='utf8') as definition:    
            found = first_term()
            definition.readline()
            line = definition.readline()
            isUsage = usage(line)
            while True:
                global second
                second = subsequent(isUsage, line)
                definition.readline()
                line = definition.readline()
                isUsage = usage(line)
                if second == False:
                    break
        if found == False:
            print(search_term + " not found, please try another term.")



def usage(line):
    '''Searches for Usage or a duplicate of the term
:line: readline() variable
    '''
    if line[0:5] == 'Usage':
        print('Usage: ' + line[7:].rstrip())
        return True
    return False


def first_term():
    '''
    Works to find the search term in the dictionary file.
    '''
    for line in definition:
        if search_term in line.lower():
            word = tuple(line.split('  '))
            if word[0][-1].isalpha():
                if search_term == word[0].lower():
                    print('\n' + word[0])
                    print(word[1])
                    return True
            if word[0][-1].isnumeric():
                if search_term == word[0][:-1].lower().rstrip():
                    print(word[0])
                    print(word[1])
                    return True
    return False



def subsequent(isUsage, line):
    '''Checks to see if there are similar terms in the next lines.
:isUsage: "is line a usage line?" variable
:line: readline() variable
    '''
    if isUsage == True:
        definition.readline()
        line = definition.readline()
    word = line.split('  ')
    if search_term in word[0].lower():
        if word[0][-1].isalpha():
            if search_term == word[0].lower():
                print(word[0])
                print(word[1])
                return True
        if word[0][-1].isnumeric():
            if search_term == word[0][:-1].lower().rstrip():
                print(word[0])
                print(word[1])
                return True
    else: return False



if __name__ == "__main__":
    main()
    input()