# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# Method 1: Using sorted method
# Python code to check if two strings are anagrams of each other using sorted() 

def find_anagram(word, anagram):
    
    #Unequal Length strings cannot be anagrams
    if len(word) != len(anagram):
        return False
    
    #sort the first string
    first = sorted(word)
    #sort the second string
    second = sorted(anagram)
    
    #check if both the strings are same
    if first == second:
        return True
    else:
        return False
    
#testing
print("Finding anagram using sorted method")
print(find_anagram("listen","silent"))
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))

#Method 2: By counting characters
#Python program to find anagrams by counting characters 
def find_anagram2(word, anagram):
        NUM_CHARS = 256
        count_str1 = [0]*NUM_CHARS
        count_str2 = [0]*NUM_CHARS
        if len(word) != len(anagram):
            return False
        for i in word:
            count_str1[ord(i)] += 1
        for i in anagram:
            count_str2[ord(i)] += 1
        for i in range(NUM_CHARS):
            if count_str1[i] != count_str2[i]:
                return False
        return True
    
#testing
print("Finding anagram by counting characters")
print(find_anagram2("listen","silent"))
print(find_anagram2("hello", "check"))
print(find_anagram2("below", "elbow"))

#Method 3: By Counter function
#Python code to check if two strings are anagrams of each other or not using Counter()
from collections import Counter
def find_anagram3(word, anagram):
    #use counter to count the frequency of characters
    #in each string
    if Counter(word) == Counter(anagram):
        return True
    return False

#testing
print("Finding anagram using Counter function")
print(find_anagram3("listen","silent"))
print(find_anagram3("hello", "check"))
print(find_anagram3("below", "elbow"))

