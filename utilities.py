import random
import string
import math

# 1- get_lower()
# 2- shift_string(s,n,d)
# 3- get_B6Code()
# 4- bin_to_dec(b)
# 5- is_binary(b)
# 6- dec_to_bin(decimal,size)
# 7- xor(a,b)
# 8- get_undefined(text,base)
# 9- insert_undefinedList(text, undefinedList)
# 10- remove_undefined(text,base)
#-----------------------------------------------------------
# Parameters:   None 
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
#-----------------------------------------------------------
def get_lower():
    return "".join([chr(ord('a')+i) for i in range(26)])

#-------------------------------------------------------------------
# Parameters:   s (string): input string
#               n (int): number of shifts
#               d (str): direction ('l' or 'r')
# Return:       s (after applying shift
# Description:  Shift a given string by n shifts (circular shift)
#               as specified by direction, l = left, r= right
#               if n is negative, multiply by 1 and change direction
#-------------------------------------------------------------------
def shift_string(s,n,d):
    if d != 'r' and d!= 'l':
        print('Error (shift_string): invalid direction')
        return ''
    if n < 0:
        n = n*-1
        d = 'l' if d == 'r' else 'r'
    n = n%len(s)
    if s == '' or n == 0:
        return s

    s = s[n:]+s[:n] if d == 'l' else s[-1*n:] + s[:-1*n]
    return s

#-----------------------------------------------------------
# Parameters:   None
# Return:       B6Code (str)
# Description:  Generates all symbols in the B6 Encoding Scheme
#               This includes 64 symbols arranged as follows:
#               Digits 0 to 9
#               26 lower case alphabet
#               26 upper case alphabet
#               space
#               newline, i.e. '\n'
#               All punctuations and special sybmols are not represented in this encoding
# Error:        None
#-----------------------------------------------------------
def get_B6Code():
    nums = ''.join([str(i) for i in range(10)]) #10 sybmols
    alphabet = get_lower() # 26 symbols
    return nums+ alphabet + alphabet.upper() + ' ' + '\n' #64 symbols

#-----------------------------------------------------------
# Parameters:   b (str): binary number
# Return:       decimal (int)
# Description:  Converts any binary number into corresponding integer
# Error:        if not a valid binary number: 
#                   print('Error(bin_to_dec): invalid input'), return ''
#-----------------------------------------------------------
def bin_to_dec(b):
    if not is_binary(b):
        print('Error(bin_to_dec): invalid input')
        return ''
    value = 0
    exponent = len(b)-1
    for i in range(len(b)):
        if b[i] == '1':
            value+= 2**exponent
        exponent-=1
    return value

#-----------------------------------------------------------
# Parameters:   b (str): binary number
# Return:       True/False
# Description:  Checks if given input is a string that represent a valid
#               binary number
#               An empty string, or a string that contains other than 0 or 1
#               should return False
# Error:        None
#-----------------------------------------------------------
def is_binary(b):
    if not isinstance(b,str) or b == '':
        return False
    for i in range(len(b)):
        if b[i]!= '0' and b[i]!='1':
            return False
    return True

#-----------------------------------------------------------
# Parameters:   decimal (int)
#               size (int)
# Return:       binary (str)
# Description:  Converts any integer to binary and fit in size bits
#               if number is too small to occupy size bits --> pre-pad with 0's 
# Error:        if decimal or size is not integer:
#                   print('Error(dec_to_binary): invalid input'), return ''
#               if size is too small to fit binary number:
#                   print('Error(dec_to_binary): integer overflow'), return ''
#-----------------------------------------------------------
def dec_to_bin(decimal,size):
    if not isinstance(decimal,int) or not isinstance(size,int):
        print('Error(dec_to_binary): invalid input')
        return ''
    if size <1:
        print('Error(dec_to_binary): invalid size')
        return ''
    binary = ''
    q = 1
    r = 0
    while q!=0:
        q = decimal//2
        r = decimal%2
        decimal = q
        binary = str(r)+binary
    if len(binary) > size:
        print('Error(dec_to_binary): integer overflow')
        return ''
    while len(binary)!= size:
        binary = '0'+binary
    return binary

#-----------------------------------------------------------
# Parameters:   a (str): binary number
#               b (str): binary number
# Return:       decimal (int)
# Description:  Apply xor operation on a and b
# Error:        if a or b is not a valid binary number 
#                   print('Error(xor): invalid input'), return ''
#               if a and b have different lengths:
#                    print('Error(xor): size mismatch'), return ''
#-----------------------------------------------------------
def xor(a,b):
    if not is_binary(a) or not is_binary(b):
        print('Error(xor): invalid input')
        return ''
    if len(a)!= len(b):
        print('Error(xor): size mismatch')
        return ''
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c+='0'
        else:
            c+='1'
    return c

#-----------------------------------
# Parameters:   text (str)
#               base (str)
# Return:       undefinedList (2D List)
# Description:  Analyzes a given text
#               Returns a list of all characters of text which are undefined
#               in base, along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#-----------------------------------
def get_undefined(text,base):
    undefinedList = []
    for i in range(len(text)):
        if text[i] not in base:
            undefinedList.append([text[i],i])
    return undefinedList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------
def insert_undefinedList(text, undefinedList):
    modifiedText = text
    for item in undefinedList:
        modifiedText = modifiedText[:item[1]]+item[0]+modifiedText[item[1]:]
    return modifiedText

#-----------------------------------
# Parameters:   text (string)
#               base (string)
# Return:       modifiedText (string)
# Description:  Removes all characters in text which are not found in base
#-----------------------------------
def remove_undefined(text,base):
    modifiedText = ''
    for c in text:
        if c in base:
            modifiedText += c
    return modifiedText

#--------------------------
# Your Name and ID   <--------------------- Change this -----
# CP460 (Fall 2019)
# Midterm Student Utilities File
#--------------------------

#-----------------------------------------------
# Remember to change the name of the file to:
#               utilities.py
# Delete this box after changing the file name
# ----------------------------------------------

#----------------------------------------------
# You can not add any library other than these:
import math
import string
import random
ASCII_SIZE = 256
#----------------------------------------------

#-----------------------------------------------------------
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
#-----------------------------------------------------------
def file_to_text(fileName):
    inFile = open(fileName,'r')
    contents = inFile.read()
    inFile.close()
    return contents

#-----------------------------------------------------------
# Parameters:   None
# Return:       baseString (str)
# Description:  Returns base string for substitution cipher
#-----------------------------------------------------------
def get_baseString():
    #generate alphabet
    alphabet = ''.join([chr(ord('a')+i) for i in range(26)])    
    symbols = """.,; #"?'!:-"""     #generate punctuations
    return alphabet + symbols

#-----------------------------------------------------------
# Parameters:   key (str)
# Return:       key (str)
# Description:  Utility function for Substitution cipher
#               Exchanges '#' wiht '\n' and vice versa
#-----------------------------------------------------------
def adjust_key(key):
    if '#' in key:
        newLineIndx = key.index('#')
        key = key[:newLineIndx]+'\n'+key[newLineIndx+1:]
    else:
        newLineIndx = key.index('\n')
        key = key[:newLineIndx]+'#'+key[newLineIndx+1:]
    return key

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext (str)
#               baseString (str)
# Return:       None
# Description:  A debugging tool for substitution cipher
#---------------------------------------------------------------------------------------
def debug_substitution(ciphertext,baseString):
    subString = ['-' for i in range(len(baseString))]
    plaintext = ['-' for i in range(len(ciphertext))]
    print('Ciphertext:')
    print(ciphertext[:200])
    print()
    command = input('Debug Mode: Enter Command: ')
    description = input('Description: ')
    print()
    
    while command != 'end':
        subChar = command[8].lower()
        baseChar  = command[15].lower()

        if subChar == '#':
            subChar = '\n'
        if baseChar == '#':
            baseChar = '\n'
            
        if baseChar in baseString:
            indx = baseString.index(baseChar)
            subString[indx] = subChar
        else:
            print('(Error): Base Character does not exist!\n')

           
        print('Base:',end='')
        for i in range(len(baseString)):
            if baseString[i] == '\n':
                print('# ',end='')
            else:
                print('{} '.format(baseString[i]),end='')
        print()
        print('Sub :',end='')
        for i in range(len(subString)):
            if subString[i] == '\n':
                print('# ',end='')
            else:
                print('{} '.format(subString[i]),end='')
        print('\n')

        print('ciphertext:')
        print(ciphertext[:200]) # <---- you can edit this if you need to show more text
        for i in range(len(plaintext)):
            if ciphertext[i].lower() == subChar:
                if subChar == '#' or subChar == '\n':
                    plaintext[i] == '\n'
                else:
                    plaintext[i] = baseChar
        print('plaintext :')
        print("".join(plaintext[:200])) # <---- you can edit this if you need to show more text
        print('\n_______________________________________\n')
        command = input('Enter Command: ')
        description = input('Description: ')
        print()
    return

# you can add any utility functions as you like
#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (str,int,double)
# Return:       empty matrix (2D List)
# Description:  Create an empty matrix of size r x c
#               All elements initialized to pad
#               Default row and column size is 2
#-----------------------------------------------------------
def new_matrix(r,c,pad):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[pad] * c for i in range(r)]

#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of strings, each pertaining to a dictionary word
#-----------------------------------------------------------
def load_dictionary(dictFile):
    dictList = []
    # your code here
    fv = open(dictFile, "r", encoding="mbcs")
    line = fv.readline()
    while line != "":
        dictList.append(line.strip('\n'))
        line = fv.readline()
    return dictList

#-------------------------------------------------------------------
# Parameters:   text (string)
# Return:       list of words (list)
# Description:  Reads a given text
#               Each word is saved as an element in a list. 
#               Returns a list of strings, each pertaining to a word in file
#               Gets rid of all punctuation at the start and at the end 
#-------------------------------------------------------------------
def text_to_words(text):
    wordList = [x.strip(string.punctuation) for x in text.split()]
    return wordList

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
#-----------------------------------------------------------
def analyze_text(text, dictFile):
    matches = 0
    mismatches = 0
    # your code here
    dictList = load_dictionary(dictFile)
    wordList = text_to_words(text)
    for word in wordList:
        if word.lower() in dictList:
            matches += 1
        else:
            mismatches += 1
    return(matches,mismatches)

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
#-----------------------------------------------------------
def is_plaintext(text, dictFile, threshold):
    # your code here
    if text == '':
        return False
    
    if not (threshold >= 0.0 and threshold <= 1.0):
        threshold = 0.9
    (matches, mismatches) = analyze_text(text, dictFile)
    
    total_words = matches + mismatches
    if (matches / total_words) >= threshold:
        return True
    return False
    
#-----------------------------------------------------------
# Parameters:   None 
# Return:       squqre (list of strings)
# Description:  Constructs Vigenere square as list of strings
#               element 1 = "abcde...xyz"
#               element 2 = "bcde...xyza" (1 shift to left)
#-----------------------------------------------------------
def get_vigenereSquare():
    alphabet = get_alphabet()
    return [shift_string(alphabet,i,'l') for i in range(26)]

#-------------------------------------------------------------------
# Parameters:   s (string): input string
#               n (int): number of shifts
#               d (str): direction ('l' or 'r')
# Return:       s (after applying shift
# Description:  Shift a given string by n shifts (circular shift)
#               as specified by direction, l = left, r= right
#               if n is negative, multiply by 1 and change direction
#-------------------------------------------------------------------
def shift_string(s,n,d):
    if d != 'r' and d!= 'l':
        print('Error (shift_string): invalid direction')
        return ''
    if n < 0:
        n = n*-1
        d = 'l' if d == 'r' else 'r'
    n = n%len(s)
    if s == '' or n == 0:
        return s

    s = s[n:]+s[:n] if d == 'l' else s[-1*n:] + s[:-1*n]
    return s

#-------------------------------------------------------------------
# Parameters:   str (string): input string
#               
# Return:       c (most occuring char)
# Description:  Finds the most occuring character
#-------------------------------------------------------------------
def getMaxOccuringChar(ciphertext, combined): 
    c = 0
    temp = 0

    for i in range(len(combined)):
        if ciphertext.count(combined[i]) > c:
            c = ciphertext.count(combined[i])
            temp = i

    return temp
  
    return c

#-----------------------------------------------------------
# Parameters:   None
# Return:       alphabet (str)
# Description:  Returns alphabet
#-----------------------------------------------------------
def get_alphabet():
    #generate alphabet
    alphabet = ''.join([chr(ord('a')+i) for i in range(26)])    
    return alphabet

#-----------------------------------------------------------
# Parameters:   None
# Return:       alphabet (str)
# Description:  Returns alphabet reversed
#-----------------------------------------------------------
def get_alphabet_reversed():
    return get_alphabet()[::-1]
#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters upper case
#-----------------------------------
def remove_nonalpha(text):
    modifiedText = ''

    for c in text:
        if c.isalpha():
            modifiedText += c

    return modifiedText

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
#---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    k = 1
    matches = []

    for i in range(1, 21):
        total_matches = 0
        shift = ''
        shift += ciphertext[i:] + ciphertext[:i]
        for j in range(i, len(ciphertext)):
            if ciphertext[j] == shift[j]:
                total_matches += 1
        matches.append(total_matches)
    
    k = matches.index(max(matches)) + 1
    return k

#-----------------------------------------------------------
# Parameters:   text (string)
# Return:       double
# Description:  Calculates the Chi-squared statistics
#               chiSquared = for i=0(a) to i=25(z):
#                               sum( Ci - Ei)^2 / Ei
#               Ci is count of character i in text
#               Ei is expected count of character i in English text
#               Note: Chi-Squared statistics uses counts not frequencies
#-----------------------------------------------------------
def get_chiSquared(text):
    freqTable = get_freqTable()
    charCount = get_charCount(text)

    result = 0
    for i in range(26):
        Ci = charCount[i]
        Ei = freqTable[i]*len(text)
        result += ((Ci-Ei)**2)/Ei
    return result

#-----------------------------------------------------------
# Parameters:   None 
# Return:       list 
# Description:  Return a list with English language letter frequencies
#               first element is frequency of 'a'
#-----------------------------------------------------------
def get_freqTable():
    freqTable = [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
                 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    return freqTable

#-----------------------------------------------------------
# Parameters:   text (str) 
# Return:       list: wordCount 
# Description:  Count frequency of letters in a given text
#               Returns a list, first element is count of 'a'
#               Counts both 'a' and 'A' as one character
#-----------------------------------------------------------
def get_charCount(text):
    return [text.count(chr(97+i))+text.count(chr(65+i)) for i in range(26)]

#-----------------------------------------------------------
# Parameters:   key_length (int) 
# Return:       periods (list)
# Description:  Gets the periods
#-----------------------------------------------------------
def get_periods(key_length):
    return [''] * key_length