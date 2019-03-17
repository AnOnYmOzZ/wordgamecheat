'''
Program name: wordsgamecheat.py
Author: Jcliff - Tinkatek
Contact: cliffordolawaiye@gmail.com
Desc: This is program is to create all the possible words from
    a set of inputted letters and search for it in a dictionary and return the
    found words.
    This program works fine
    I BELIEVE IT WORKS BETA THAN THE FIRST IN TERMS OF RUNTIME
'''
import itertools
import os

dictdir = str(os.getcwd())+"\\69kwordlist.txt"
dictfile = open(dictdir)
#dictfile = open('C:\\Users\\J.cliff\\Documents\\#PROGRAMMING-\\python\\#MyPython\\dictwords\\69kwordlist.txt')

def all_possible_combination (letters, r):
        #letters --> the letters to form words from
        #r --> how many letter words e.g. 3,2,4 e.t.c

    #letterlist = list(letters) #converts 'letter' to list
    wordslist = itertools.permutations(letters, r)
        #generates all possible words with 'r' length and stores them in 'wordlist'
        #NB: This 'wordlist' would be an embedded list i.e its elements are also a list
        #so i convert it to a list with strings as elements in the following steps
    allcombo = [] #all possible combinations as a list
    for i in wordslist:
        a = ''.join(i)
        allcombo.append(a)
    return allcombo
         
def dictscan(allcombo): #function to scan a dictionary file
    #this fn opens the dict file, create a list to check each line for the
    #element of the list in the dictionary file
    dictfile.seek(0,0)
    
    foundwords =[]
    sfoundwords=[]
    allcombo_mod = []
    
    for i in allcombo:
        b = i +'\n'
        allcombo_mod.append(b)
        
    for eachline in dictfile:
        if any( i == eachline for i in allcombo_mod):
            foundwords.append(eachline)
    
    for i in foundwords: #strips foundwords of '\n' and stores in sfoundwords
        sfoundwords.append(i.strip())
    
    return sfoundwords


print('----------*welcome to the Cliff Word links game*----------')

test = 'y'

while test == 'y':
    print('\n')
    letters = input("\n----------Enter the letters to check all its possible words: ")
    rawinput = input("\n----------How many letter words do you want: ")

    
    if len(rawinput) == 1:
        r = int(rawinput)

        #using first function
        allcombo = all_possible_combination(letters, r)

        #using second function
        sfoundwords = dictscan(allcombo)
        print('\n----------Here is your final correct words: ')
        for i in sfoundwords:
            print(i)

    else:
        liststr = list(rawinput)
        r = []
        
        for i in liststr:
            r = int(i)
            
            #using first function
            allcombo = all_possible_combination(letters, r)
            
            #using second function
            sfoundwords = dictscan(allcombo)
            print('\n---------- Here are correct {0} letter words: '.format(r))
            
            for j in sfoundwords:
                print(j)


#Prompts to either carry out the program again or end the program
    msgprompt = input('----------continue? yes or no: ')
    test = msgprompt[0].lower()
    if test == 'y':
        continue
    else :
        ans = input('\n----------are you sure you want to quit? ')
        if ans[0].lower() == 'y' :
            test = 'n'
            continue
        else :
            test = 'y'
            continue

else :    
        quit
