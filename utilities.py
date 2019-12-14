# author Duc Nguyen
import random
import string
import math

# 1- get_lower()
# 2- get_baseString()
# 3- load_dictionary(dictFile)
# 4- analyze_text(text, dictFile)
# 5- text_to_words(text)
# 6- is_plaintext(text, dictFile, threshold)
# 7- new_matrix(r,c,pad)
# 8- shift_string(s,n,d)
# 9- get_B6Code()
# 10- bin_to_dec(b)
# 11- is_binary(b)
# 12- dec_to_bin(decimal,size)
# 13- xor(a,b)
# 14- get_undefined(text,base)
# 15- insert_undefinedList(text, undefinedList)
# 16- remove_undefined(text,base)
# 17- file_to_text(filename)
# 18- text_to_file(text, filename)
# 19- get_chiSquared(text)
# 20- get_freqTable()
# 21- get_charCount(text)
# 22- text_to_blocks(text,size)
# 23- compare_files(file1,file2)
# 24- remove_nonalpha(text)
# 25- get_nonalpha(text)
# 26- insert_nonalpha(text, nonAlpha)
# 27- get_RSA_baseString()

#-----------------------------------------------------------
# Parameters:   None 
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
#-----------------------------------------------------------
def get_lower():
    return "".join([chr(ord('a')+i) for i in range(26)])

#-----------------------------------------------------------
# Parameters:   None 
# Return:       baseString (string)
# Description:  Return a string composed of:
#               alphabet (lower case) (26 symbols)
#               space
#               digits (10 symbols)
#               punctuations (defined in string library) (32 symbols)
#               new line character
#               Total number of characters = 70

#-----------------------------------------------------------
def get_baseString():
    alphabet = get_lower() # 26 symbols
    nums = ''.join([str(i) for i in range(10)]) #10 sybmols
    punctuations = string.punctuation #32 sybmols
    return alphabet + ' '+nums + punctuations + '\n'  #70 symbols


#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of lists, list[0] contains all words starting with 'a'
#               list[1] all words starting with 'b' and so forth.
#-----------------------------------------------------------
def load_dictionary(dictFile):
    alphabet = get_lower()
    inFile = open(dictFile, 'r',encoding=" ISO-8859-15") 
    dictWords = inFile.readlines()
    dictList = [[] for i in range(26)]
    for w in dictWords:
        word = w.strip('\n')
        dictList[alphabet.index(word[0])]+=[word]
    inFile.close()
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
    wordList = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            if line[i] != '':
                line[i] = line[i].strip(string.punctuation)
                wordList+=[line[i]]
    return wordList

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictList (list of lists)
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
#-----------------------------------------------------------
def analyze_text(text, dictList):
    wordList = text_to_words(text)
    alphabet = get_lower()
    matches = 0
    mismatches = 0
    for w in wordList:
        if w.isalpha():
            listNum = alphabet.index(w[0].lower())
            if w.lower() in dictList[listNum]:
                matches+=1
            else:
                mismatches+=1
        else:
            mismatches+=1
    return(matches,mismatches)

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictList (list of lists)
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
#-----------------------------------------------------------
def is_plaintext(text, dictList, threshold):
    if text == '':
        return False
    result = analyze_text(text, dictList)
    percentage = result[0]/(result[0]+result[1])
    if threshold < 0 or threshold > 1:
        threshold = 0.9
    if percentage >= threshold:
        return True
    return False

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

#-----------------------------------------------------------
# Parameters:   text (string)
#               filename (string)            
# Return:       none
# Description:  Utility function to write any given text to a file
#               If file already exist, previous content will be over-written
#-----------------------------------------------------------
def text_to_file(text, filename):
    outFile = open(filename,'w')
    outFile.write(text)
    outFile.close()
    return

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

#-----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
#------------------------------------------------------------------------------
def text_to_blocks(text,size):
    return [text[i*size:(i+1)*size] for i in range(math.ceil(len(text)/size))]

#-----------------------------------------------------------------------------
# Parameters:   file1 (string)
#               file2 (string)
# Return:       Comparison Result
# Description:  Compares contents of file1 against contents of file2
#               if identical --> return 'Identical'
#               if non-identical --> return line number where mismatch occured
#------------------------------------------------------------------------------
def compare_files(file1,file2):
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    counter = 1
    line1 = 'a'
    line2 = 'b'
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if line1 == '' and line2 == '':
            return 'Identical'
        if line1 != line2:
            return 'Mismatch Line '+str(counter)
        counter+=1 
    f1.close()
    f2.close()
    return

#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters
#-----------------------------------
def remove_nonalpha(text):
    modifiedText = ''
    for char in text:
        if char.isalpha():
            modifiedText += char
    return modifiedText

#-----------------------------------
# Parameters:   text (string)
# Return:       nonalphaList (2D List)
# Description:  Analyzes a given string
#               Returns a list of non-alpha characters along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#               Example: get_nonalpha('I have 3 cents.') -->
#                   [[' ', 1], [' ', 6], ['3', 7], [' ', 8], ['.', 14]]
#-----------------------------------
def get_nonalpha(text):
    nonalphaList = []
    for i in range(len(text)):
        if not text[i].isalpha():
            nonalphaList.append([text[i],i])
    return nonalphaList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------
def insert_nonalpha(text, nonAlpha):
    modifiedText = text
    for item in nonAlpha:
        modifiedText = modifiedText[:item[1]]+item[0]+modifiedText[item[1]:]
    return modifiedText

#-----------------------------------
# Parameters:   None
# Return:       baaseString (string)
# Description:  returns a 96-character string to be used in RSA cryptography
#-----------------------------------
def get_RSA_baseString():
    lower = get_lower() # 26 symbols
    upper = lower.upper() # 26 symbols
    nums = ''.join([str(i) for i in range(10)]) #10 sybmols
    punctuations = string.punctuation #32 sybmols
    return lower + upper + ' '+nums + punctuations + '\n'  #96 symbols
