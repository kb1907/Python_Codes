"""Challenges from different website"""

"""Challenge 1"""
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".


# First Way Classic One:
string = "This website is for losers LOL!"


def disemvowel(string):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for x in vowels:
        string = string.replace(x, "")
    return string


disemvowel(string)


# Second Way Newer one with translate method
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")


# Third way list comprehension

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


"""Challenge 2"""


# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).


def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)


"""Challenge 3"""
# You are going to be given a word. Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

# First way
test = "test"


def getMiddle(test):
    if len(test) % 2 == 0:
        x = int(len(test) / 2)
        return (test[x - 1] + test[x])
    else:
        x = int(len(test) / 2)
        return (test[x])


getMiddle(test)


# Best way
def get_middle(s):
    return s[int((len(s) - 1) / 2):int(len(s) / 2 + 1)]


"""Challenge 4"""


# Write a function called repeat_string which repeats the given string str exactly count times.
def repeat_str(repeat, string):
    return (repeat * string)


repeat_str(6, "i")

"""Challenge 6"""


# Simple, remove the spaces from the string,
# then return the resultant string.

def no_space(x):
    return "".join(x.split())


"""Challenge 7"""


# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# One way
def get_count(input_str):
    num_vowels = 0
    # your code here
    for x in input_str:
        if x in ["a", "e", "i", "o", "u"]:
            num_vowels += 1

    return (num_vowels)


# better way
def getCount(s):
    return sum(c in 'aeiou' for c in s)


"""Challenge 8"""


# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible
# containing distinct letters - each taken only once - coming from s1 or s2.
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


"""Challenge 9"""


# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    return s[1: (len(s) - 1)]


# better way
def remove_char(s):
    return s[1:-1]


"""Challenge 10"""


# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    v = [z for z in s.split()]
    x = "asdeffffeöe,fa,ä,efäaä,fäöa,ö,,öaö,äö,va,äe,raävö,,v"
    for y in v:
        if len(y) < len(x):
            x = y
            l = len(y)
    return l  # l: shortest word length


# best way:
def find_short(s):
    return min(len(x) for x in s.split())


# or:
def find_short(s):
    return len(min(s.split()))


"""Challenge 11"""


# In this kata you will create a function that takes a list of non-negative integers and strings
# and returns a new list with the strings filtered out.
# example: filter_list([1,2,'a','b']) == [1,2]

def filter_list(l):
    l = [x for x in l if type(x) != str]
    return l


"""Challenge 12"""


# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.

def add_binary(a, b):
    return '{0:b}'.format(a + b)


"""Challenge 13"""


# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    z = []

    string = string.upper()
    if string == "":
        return True

    for l in range(0, len(string)):
        y = string[l]
        if y in z:
            return False
        elif y not in z:
            z.append(y)
            if l == len(string) - 1:
                return True


# Better way:
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True


# Best way:
def is_isogram(string):
    return len(string) == len(set(string.lower()))


"""Challenge 14"""


# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks
# whether the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    else:
        c = [x * x for x in array1]
        return (bool(sorted(c) == sorted(array2)))


# Best Way:
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


# Clever way:
def comp(a1, a2):
    return None not in (a1, a2) and [i * i for i in sorted(a1)] == sorted(a2)


"""Challenge 15"""


# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
    c = "".join(str(x) for x in arr)
    return int(c, 2)


# Best way using map method

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


"""Challenge 16"""


# You'll have to capitalize each word, check out how contractions are expected to be in the example below.
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    return " ".join(w.capitalize() for w in string.split())


"""Challenge 17"""


# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    s = s.lower()
    if "x" not in s or "o" not in s:
        return True
    else:
        return s.count("x") == s.count("o")


"""Challenge 18"""

# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.

s = "is2 Thi1s T4est 3a"

print(' '.join(sorted(s.split(), key=lambda w: sorted(w))))

"""Challenge 19"""

# The provided code stub reads and integerfrom STDIN. Print the square of each number on a separate line.
n = 9
print(*[x * x for x in range(n)], sep="\n")  # * is arbitrary argument helps us to print out numbers out of the list.

"""Challenge 19"""


# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            leap = False
        else:
            leap = True
    else:
        leap = False

    return leap


year = int(input())


# Best Way:
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


"""Challenge 20"""

# Without using any string methods, try to print the following: n= 5, print the string 12345, without spaces.
print(*[x for x in range(6)], sep="")

"""Challenge 21"""


# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between including them too and return it. If the two numbers are equal return a or b.

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


"""Challenge 22"""


# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).

def DNA_strand(dna):
    x = "ACTG"
    y = "TGAC"
    table = dna.maketrans(x, y)
    return dna.translate(table)


# or
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG", "TAGC"))


"""Challenge 23"""


# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple like so: (index1, index2).
# twoSum [1, 2, 3] 4 === (0, 2)

def two_sum(numbers, target):
    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            if numbers[x] + numbers[y] == target:
                return x, y


# Another Way
def two_sum(numbers, target):
    d = {}
    for i, n in enumerate(numbers):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i


"""Challenge 24"""
# Given an array of integers, remove the smallest value. Do not mutate the original array/list.
# If there are multiple elements with the same value, remove the one with a lower index.
# If you get an empty array/list, return an empty array/list.
# remove_smallest([1,2,3,4,5]) = [2,3,4,5]

num = [1, 2, 1, 3, 4, 5]
z = []
y = []
for x in num:
    if x is min(num) and x not in z:
        z.append(x)
    elif x is not min(num) or x in z:
        y.append(x)
print(y)


# Best Way:
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return (a)


"""Challenge 25"""


# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
# For example:
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


"""Challenge 26"""
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".


import string


def rot13(message):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    lookup = str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
    return message.translate(lookup)


rot13("Text")

"""Challenge 27"""
# Write a program that; Finds out the most frequent number in the given list.
# Calculates its frequency.

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
a = max(numbers, key=numbers.count)
b = numbers.count(a)

"""Challenge 28"""
# You need to write regex that will validate a password to make sure it meets the following criteria:
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.

from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)

# or

regex = (
    '^'  # start line
    '(?=.*\d)'  # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'  # permitted characters (alphanumeric only)
    '{6,}'  # length at least 6 chars
    '$'  # end line
)

# or
regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"

"""Challenge 29"""

# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
# A= [1,2,3,4]
# Print 4 3 2 1. Each integer is separated by one space.
# n = int(input())
#
arr = list(map(int, input().rstrip().split()))

print(" ".join(map(str, (arr[::-1]))))   #First we took reverse by -1, then
# with map function we changed number in the list to string
# then we joined them into string

"""Challenge 30"""
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
# Example: Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for x in range(len(nums)):
#             for y in range(x + 1, len(nums)):
#                 if nums[x] + nums[y] == target:
#                     return x, y
# Better way:
nums = [2,7,11,15]
target = 9
myHash = {}

def find_target(nums, target):
    for index, value in enumerate(nums):
        if target - value in myHash:
            return [myHash[target-value], index]
        myHash[value] = index

"""Challenge 31"""
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}
for word in words:
    sortedWord = "".join(sorted(word))
    if sortedWord in anagrams:
        anagrams[sortedWord].append(word)
    else:
        anagrams[sortedWord] = [word]
print(list(anagrams.values()))

"""Challenge 32"""
# ask
# Given a base- integer, , convert it to binary (base-10).
# Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.
# When working with different bases, it is common to show the base as a subscript.
# n = 125 binary_n = 1111101  max_consecutive 1 = 5

n = '5'

print(max(map(len, f'{int(n):b}'.split('0'))))
# first with f string we turned it to binary
# and then used string split method to split into the list by using '0' as a reference point
# then used map function to get len of the lists
# lastly we used the max function to get maximum length of the list.

"""Challenge 33"""
# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas except for the last two names,
# which should be separated by an ampersand.

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
# returns 'Bart, Lisa & Maggie'
l = []
n = len(names)

if n > 1:
    z = names[n - 1]['name']
    for x in names[:n - 1]:
        l.append(x['name'])
    print(', '.join(l) + ' ' + '&' + ' ' + z)

elif n == 0:
    print('')

else:
    print(names[0]['name'])

# Better way

if len(names) > 1:
    print('{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name']))
elif names:
    print(names[0]['name'])
else:
    print('')

"""Challenge 34"""
# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
# Examples :
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


l = [5, 8, 6, 3, 4]
z = []
y = []
for index, num in enumerate(l):
    if num % 2 != 0:
        z.append(num)
        y.append(index)

for n in range(len(y)):
    l[y[n]] = sorted(z)[n]

print(l)

# Better Way

odds = sorted((x for x in l if x % 2 != 0), reverse=True)
print([x if x % 2 == 0 else odds.pop() for x in l])

"""Challenge 35"""
# You will be given a number and you will need to return it as a string in expanded form
# Examples:
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

num = 70304  # Should return '70000 + 300 + 4'

v = len(str(num)) - 1
z = ''
for x in str(num):
    if x != '0':
        y = int(x) * 10 ** v
        if v >= 1:
            z += str(y) + ' ' + '+' + ' '
        else:
            z += str(y)
        v -= 1
    else:
        v -= 1

print(z.strip('+ '))

"""Challenge 36"""

# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
#  1.  The input string will always be lower case but maybe empty.
#  2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# example = wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

test = "hello"
l = []
for i, x in enumerate(test):  # enumerate count ve index icin oldukca kullanisli bir method
    if x != ' ':
        x = x.upper()
        for y in test[i]:
            y = x
            changed_test_1 = test[i:].replace(test[i], y, 1)  # i index ve sonrasini al ve
            # i indexteki harfi, istedigimiz deger ile degistir ve bu islemi 1 kez yap
            changed_test = test[:i] + changed_test_1  # i indexe kadar olan parcayi
            # yeni olusturdugumuz string ile birlestir.
            l.append(changed_test)
print(l)

# better way
wave = "hello"
print([wave[:i] + wave[i].upper() + wave[i + 1:] for i in range(len(wave)) if wave[i].isalpha()])

"""Challenge 37"""
# Complete the solution so that the function will break up camel casing, using a space between words.
#  Example : ("helloWorld"), "hello World")  ("camelCase"), "camel Case")
s = "camelCase"
import re

z = re.sub(r'([A-Z])', r' \1', s)  # ' 1' keeps both space and the [A-Z]

# other solution
t = ''.join(' ' + c if c.isupper() else c for c in s)

"""Challenge 38"""
# put (-) between the letters in the given string, except the last one
s = 'welcome'
s_1 = ''.join([(w + '-') if w in s[:-1] else w for w in s])

"""Challenge 39"""


# Make a function called encode() to replace all the lowercase vowels in a given string
# with numbers according to the following pattern:
# a -> 1 e -> 2 i -> 3 o -> 4 u -> 5
# 'hello' --> 'h2ll4'
# Step 2: Now  make a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
# 'h2ll4' --> 'hello'

def encode(word):
    transTable = word.maketrans('aeiou', '12345')
    return word.translate(transTable)
    # return decode(word.translate(transTable)) <-- If we want to call following function


def decode(word):
    transTable = word.maketrans('12345', 'aeiou')
    return word.translate(transTable)


encode('hello')


# or another way
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)


def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)


"""Challenge 40"""
# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.

import string


def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())  # very clever


"""Challenge 41"""


# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    return len(set([i for i in text.lower() if text.lower().count(i) > 1]))


"""Challenge 42"""


# Bob is preparing to pass IQ test. The most frequent task in this test is
# to find out which one of the number differs from others
# Keep in mind that your task is to help Bob solve a real IQ test
# and index start from 1 not 0
# Example : iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

def iq_test(numbers):
    z = numbers.split()
    odd = []
    even = []
    t = [odd.append((num, index)) if int(num) % 2 != 0 else even.append((num, index)) for index, num in enumerate(z, 1)]
    if len(odd) > len(even):
        return even[0][1]
    else:
        return odd[0][1]


# better way:
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
    # exercise requires to start index from 1 for that we are adding 1


"""Challenge 43"""


# You are going to be given an array of integers.
# Your job is to take that array and find an index N where the sum of the integers to the left of N
# is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1
# Example: [1,2,3,4,3,2,1] --> 3  [1,2,3,4,5,6] --> -1

def equal_sum(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


"""Challenge 44"""
# You have to extract a portion of the file name as follows:
# Assume it will start with date represented as long number
# Followed by an underscore
# You'll have then a filename with an extension
# it will always have an extra extension at the end

s = '37769163373895732755337422594_N_rOmK-_RrkYhVcvAl-_OP_A-_.3t8.3-7J61Z2sX6-23L2zW6336tK_837n2X9rCr'
reg = r'_([a-zA-Z0-9_.+-]+)\.'
v = re.findall(reg, s)
print(v[0])  # -->  N_rOmK-_RrkYhVcvAl-_OP_A-_.3t8

"""Challenge 45"""
# Task:
# Find out if a given number is an "Armstrong Number".
# An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
# 371 = 3**3 + 7**3 + 1**3;
# 9474 = 9**4 + 4**4 + 7**4 + 4**4;
# 93084 = 9**5 + 3**5 + 0**5 + 8**5 + 4**5
# Write a Python program that;
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values then display a warning message to the user.
# do not use try - except block.
n = input('Please give me a number: ')

if n.isnumeric() == False or int(n) < 0:
    print("It is an invalid entry.Don't use non-numeric,float,or negative values!")
else:
    count = 0
    for num in n:
        count += int(num) ** (len(n))
    if count == int(n):
        print(f'{n} is an Armstrong number')
    else:
        print(f'{n} is not an Armstrong number')

"""Challenge 46"""
# Complete the method which returns the number which is most frequent in the given input array.
# If there is a tie for most frequent number, return the largest number among them.

l = [1, 1, 1, 1, 12, 10, 8, 38, 38, 38, 38, 12, 12, 12, 7, 6, 6, 6, 6, 4, 10, 10, 10]
# normally it is very easy:
num = max(l, key=l.count)
# but, when we have more than one same max freq in the list, get complicates.
from collections import Counter

res = Counter(l)
z = max(res.values())
a = max(k for k, v in res.items() if v == z)

"""Challenge 47"""


# Given a string, return a new string that has transformed based on the input:
# Change case of every character, ie. lower case to upper case, upper case to lower case.
# Reverse the order of words from the input.
# Note: You will have to handle multiple spaces, and leading/trailing spaces.

# "Example Input" ==> "iNPUT eXAMPLE"
# "To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO")

def string_transformer(s):
    v = s.split(' ')
    z = ' '.join(v[::-1])
    d = ''
    for x in z:
        if x == x.upper():
            d += x.lower()
        else:
            d += x.upper()
    return d


# best way:
def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])


"""Challenge 48"""


# Reverse every other word in a given string, then return the string.
# Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word.
# Punctuation marks should be treated as if they are a part of the word in this kata.
# Example : "I really hope it works this time..."), "I yllaer hope ti works siht time...")

def reverse_alternate(string):
    l = string.split(' ')
    string = ' '.join(l)
    l = string.split()
    z = ''
    for index, letter in enumerate(l):
        if index % 2 != 0:
            z += ''.join(reversed(letter)) + ' '
        else:
            z += letter + ' '
    return z.strip()


# better way:
def reverse_alternate(string):
    return " ".join(y[::-1] if x % 2 else y for x, y in enumerate(string.split()))


"""Challenge 49"""
# To find the even count of the number in the given list

l = [2, 3, 4, 12, 11, 2, 3, 5, 12, 2]

z = set([number for number in l if l.count(number) % 2])

"""Challenge 50"""


#  To find the primer numbers
# for the given number find the primer factors of the given number
# for the given number find the all primer number up to the given number
# provide sum of the list of the primer factors of the given number


def prime_factor(n):
    prime_factors = []
    sum = 0
    if not n % 2:
        n = n // 2
        prime_factors.append(2)
    for i in range(3, n):
        if not n % i:
            if len([z for z in prime_factors if not i % z]) < 1:
                prime_factors.append(i)
                sum += i
    return prime_factors


def prime_number(n):
    prime_numbers = [2]
    for i in range(3, n):
        if len([z for z in prime_numbers if not i % z]) < 1:
            prime_numbers.append(i)
    return prime_numbers


# or shorter version


def prime_num(n):
    prime_numbers = [2]
    [prime_numbers.append(i) for i in range(3, n) if len([z for z in prime_numbers if not i % z]) < 1]
    return prime_numbers


"""
interestingly easy method to count the values for the data analysis without using additional lib
l = [True,False, True, False, ]
d = {True:0, False:0}
for x in l:
    d[x]+=1

It counts everything in the given responses, put as a value into defined dictionary.
"""

"""Challenge 51"""


# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 1000.
#

def amicable(n):
    divisors = [i for i in range(1, n) if not n % i]
    return sum(divisors)


l = []
for i in range(2, 1000):
    if amicable(amicable(i)) == i and amicable(i) != i:
        l.append(i)
print(sum(l))

"""Challenge 52"""


# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
#  is formed by starting with 0 and 1 and then adding the latest two numbers to get the next one

def fibonacci():
    l = [0, 1]
    [l.append(l[-1] + l[-2]) for _ in l if l[-1] != 55]
    return l


fibonacci()

"""Challenge 53"""


# From given two list of the numbers , will get new list
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

def reverse_number(x, y):
    str1 = ''.join(map(str, reversed(x)))
    str2 = ''.join(map(str, reversed(y)))
    num = str(int(str1) + int(str2))
    num_list = [*reversed([int(n) for n in num])]
    return num_list


reverse_number([2, 4, 9], [5, 6, 1])

"""Challenge 54"""


# Given a common phrase, return False
# if any individual word in the phrase contains duplicate letters. Return True otherwise.
# no_duplicate_letters("Fortune favours the bold.") ➞ True
# no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
# no_duplicate_letters("Look before you leap.") ➞ False
# # Duplicate letters in "Look" and "before".

def repeated(s):
    v = s.strip('.').split()
    return not bool([x for x in v if len(x) != len(set(x))])


s1 = 'Fortune favours the bold'
repeated(s1)

""" Challenge 55 """
# Given a string s consisting from digits and #, translate s to English lowercase characters as follows:
# Characters ("a" to "i") are represented by ("1" to "9").
# Characters ("j" to "z") are represented by ("10#" to "26#").

# Very very clever solution
print(''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s)))
#  By using re.findall, it creates a list of numbers
# Then iterate in the list by using list comprehension
# By using chr() function it combines values with 96, which base to find out the string
# Also uses i[:2] to eliminate # symbol.


""" Challenge 56 """


# Write a function that selects all words that have all the same vowels (in any order and/or number) as the first word, including the first word.
# Examples same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]
# same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]
# same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
# Notes Words will contain only lowercase letters, and may contain whitespaces. Frequency does not matter (e.g. if the first word is "loopy", then you can include words with any number of o's, so long as they only contain o's, and not any other vowels).

def same_vowel(l):
    l1 = set()
    z = ['a', 'e', 'i', 'o', 'u']
    output = [l[0]]
    [l1.update(x) for x in l[0] if x in z]
    for x in l[1:]:
        if set([i for i in x if i in z]) == l1:
            output.append(x)
    return output


l = ["many", "carriage", "emit", "apricot", "animal"]
same_vowel(l)

""" Challenge 57  -Sum of Pairs- """


# Given a list of integers and a single sum value,
# return the first two values (parse from the left please) in order of appearance that add up to form the sum.
# Example: sum_pairs([11, 3, 7, 5], target = 10   == [3, 7]
#  sum_pairs([10, 5, 2, 3, 7, 5],   target= 10  == [3, 7]  not [5,5] because 3,7 finishes

# Naive way :

def sum_pairs(ints, s):
    l = []
    for num in ints:
        y = s - num
        if num in l:
            return [y, num]
        else:
            l.append(y)


ints = [1, 4, 8, 7, 3, 15]
s = 8
sum_pairs(ints, s)


# Time efficient way:
def sum_pairs(ints, s):
    d = {}
    for num in ints:
        if s - num in d.keys() and d[s - num] == num:
            return [s - num, num]
        else:
            d[num] = s - num


""" Challenge 58  -Compare Two lists- """


# Compare two list, whether one of them includes items are the square roots of the items at other list.
# Example: l1 = [1,2,3,4]  , l2 ≈ [1,4,9,16]
# be sure about the empty lists.


def same_list(l1, l2):
    if not l1 or not l2:
        return False
    else:
        l1 = sorted(l1)
        l2 = sorted(l2)
        l1_s = [x ** 0.5 for x in l1]
        l2_s = [x ** 0.5 for x in l2]
        return l1_s == l2 or l2_s == l1


l1 = [1, 4]
l2 = [2, 1]
same_list(l1, l2)

""" Challenge 59  -Compare Two lists- """


# Create a function that returns the simplified version of a fraction.
# Examples
# simplify("4/6") ➞ "2/3"
# simplify("10/11") ➞ "10/11"
# simplify("100/400") ➞ "1/4"
# simplify("8/4") ➞ "2"
# Notes
# A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator.
# For example, 4/6 is not simplified, since 4 and 6 both share 2 as a factor.
# If improper fractions can be transformed into integers, do so in your code (see example #4).

def fraction(s):
    n1, n2 = map(int, s.split("/"))
    if n1 < n2:
        if not n2 % n1:
            print(f'"1/{n2 // n1}"')
        else:
            for x in range(n1 - 1, 0, -1):
                if not n1 % x and not n2 % x and x != 1:
                    print(f'"{n1 // x}/{n2 // x}"')
                elif x == 1:
                    print(f'{n1}/{n2}')
    elif n1 == n2:
        print(1)
    else:
        print(f'"{n1 // n2}"')


s = '8/4'
fraction(s)


# Another way
def gcd_euclid_theorem(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_euclid_theorem(b, a % b)


def simplify(frac):
    num, den = map(int, frac.split("/"))
    gcd = gcd_euclid_theorem(num, den)
    return str(num // gcd) + (("/" + str(den // gcd)) if den // gcd != 1 else "")


""" Challenge 60  -Basic FizzBuzz- with excellent solution """

# Print numbers from 1 to 100 inclusively following these instructions:
# if a number is multiple of 3, print "Fizz" instead of this number,
# if a number is multiple of 5, print "Buzz" instead of this number,
# for numbers that are multiples of both 3 and 5, print "FizzBuzz", print the rest of the numbers unchanged.

for number in range(1, 101):
    print(
        'FizzBuzz' if not number % 3 and not number % 5 else 'Buzz' if not number % 5 else 'Fizz' if not number % 3 else number)

""" Challenge 61  -Compare Two lists- """

# Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.
# Everyone can see the front-stage in the example below:

# FRONT STAGE
l = [[1, 2, 3, 2, 1, 1],
     [2, 4, 4, 3, 2, 2],
     [5, 5, 5, 5, 4, 4],
     [6, 6, 7, 6, 5, 5]]


# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.

def see(l):
    for x in range(len(l) - 1, 0, -1):
        for y in range(len(l) - 1, -1, -1):
            if l[x][y] <= l[x - 1][y]:
                return False
    return True


see(l)

""" Challenge 62  -Expanded Form 2- """


# You will be given a number and you will need to return it as a string in expanded form.

# Example: n = 1.24 --> '1 + 2/10 + 4/100'


def expanded_form(num):
    if '.' in str(num):
        integer_part, fractional_part = str(num).split('.')
        result = [str(int(num) * (10 ** i)) for i, num in enumerate(integer_part[::-1]) if num != '0'][::-1]
        result += [str(num) + '/' + str(10 ** (i + 1)) for i, num in enumerate(fractional_part) if num != '0']
        return ' + '.join(result)
    else:
        result = [str(int(num) * (10 ** i)) for i, num in enumerate(str(num)[::-1]) if num != '0'][::-1]
        return ' + '.join(result)


num = 70.304
expanded_form(num)

""" Challenge 63  -Balanced Parentheses- """


# Write a function that groups a string into parentheses cluster. Each cluster should be balanced.
# Examples
# split("()()()") ➞ ["()", "()", "()"]
# split("((()))") ➞ ["((()))"]
# split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]


def split(str_input):
    my_list = []
    count = 0
    s = ""
    for char in str_input:
        if char == "(":
            count += 1
            s += "("
        else:
            count -= 1
            s += ")"
            if count == 0:
                my_list.append(s)
                s = ""
    return my_list


""" Challenge 64  -Direction Reduction- """


#  The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
# Going to one direction and coming back the opposite direction right away is a needless effort. .
# Examples:
# l= ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] --> route = ["WEST"]

def dirReduc(a):
    count = 0
    while count < len(a) - 1:
        if a[count] == 'SOUTH' and a[count + 1] == 'NORTH':
            del a[count:count + 2]
            count = 0
        elif a[count] == 'NORTH' and a[count + 1] == 'SOUTH':
            del a[count:count + 2]
            count = 0
        elif a[count] == 'WEST' and a[count + 1] == 'EAST':
            del a[count:count + 2]
            count = 0
        elif a[count] == 'EAST' and a[count + 1] == 'WEST':
            del a[count:count + 2]
            count = 0
        else:
            count += 1
    return a

# better way

def dirReduc(l):
    s = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    i = 0
    while i < len(l) - 1:
        if s[l[i]] == l[i + 1]:
            del l[i:i + 2]
            i = 0
        else:
            i += 1
    return l


""" Challenge 65  -Factorial- """


def factor(x):
    result = 1
    for i in range(x):
        result *= (i + 1)
    return print(result)
factor(5)


""" Challenge 66  -Calculating with Functions- """
# This time we want to write calculations using functions and get the results.
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

def zero(x=0):
    if x == 0:
        return x
    else:
        y = 0
        return x(y)
def one(x=1):
    if x == 1:
        return x
    else:
        y = 1
        return x(y)
def two(x=2):
    if x == 2:
        return x
    else:
        y = 2
        return x(y)
def three(x=3):
    if x == 3:
        return x
    else:
        y = 3
        return x(y)
def four(x=4):
    if x == 4:
        return x
    else:
        y = 4
        return x(y)
def five(x=5):
    if x == 5:
        return x
    else:
        y = 5
        return x(y)
def six(x=6):
    if x == 6:
        return x
    else:
        y = 6
        return x(y)
def seven(x=7):
    if x == 7:
        return x
    else:
        y = 7
        return x(y)
def eight(x=8):
    if x == 8:
        return x
    else:
        y = 8
        return x(y)
def nine(x=9):
    if x == 9:
        return x
    else:
        y = 9
        return x(y)
def times(x):
    def times1(y):
        return x * y
    return times1
def plus(x):
    def times1(y):
        return x + y
    return times1
def minus(x):
    def times1(y):
        return y-x
    return times1
def divided_by(x):
    def times1(y):
        return y // x
    return times1

# Better way
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y


"""" Challenge 67  -Missing Letter- """

# 62. Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array. You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2. The array will always contain letters in only one case.
# Example:
# ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
# ["a","b","c","d","f"] -> "e"
# ["O","Q","R","S"] -> "P"
# (Use the English alphabet with 26 letters!)

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def missing_letter(s):
    for letter in s:
            if not  l[(l.index(letter))+1] == s[(s.index(letter))+1]:
                return l[(l.index(letter))+1]


"""" Challenge 68  -Valid Parentheses- """

#Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true


def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


"""" Challenge 69  -Maximum subarray sum- """
# Aim is finding the maximum sum of a contiguous subsequence in an array or list of integers:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])  should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray

def maxSubArray(l):
    count = 0
    max_count = max(l)
    for x in l:
        count += x
        if count < 0:
            count = 0
        elif count > max_count:
            max_count = count
    return max_count


# better way
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

# best way:

def maxSequence(l):
    for i in range(1, len(l)):
        if l[i - 1] > 0:
            l[i] += l[i - 1]
    return max(l)

"""" Challenge 70  -Simple Pig Latin- """

# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
# Example: pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(s):
    s1 = ''
    for x in s.split():
        if x.isalpha():
            new_x = x[1:] + x[0] + 'ay' + ' '
            s1 += new_x
        else:
            s1 += x
    return s1.strip()

# better way
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


"""" Challenge 71  -Move Zeros- """
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# example: move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(l):
    l1 = [x for x in l if x]
    l2 = [x for x in l if x==0]
    return l1+l2

# better way
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)


"""" Challenge 72  -Weight for weight- """
# Given a string with the weights in normal order can you give this string ordered by "weights" of these numbers?
# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
# "100 180 90 56 65 74 68 86 99"

def order_weight(strng):
    if strng == '':
        return strng
    l=[]
    for num in strng.split():
        y =sum([int(x) for x in num])
        l.extend([[y,num]])
    return ' '.join([x[1] for x in sorted(l)])


# better way
def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split(' ')), key=lambda x: sum(int(c) for c in x)))


"""" Challenge 73  -Weight for weight- """
# A number is Economical if the quantity of digits of its prime factorization (including exponents greater than 1)
# is equal to or lower than the digit quantity of the number itself.
# Given an integer n, implement a function that returns a string: "Equidigital" if the quantity of digits of
# the prime factorization (including exponents greater than 1) is equal to the quantity of digits of n; "Frugal"
# if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity
# of digits of n; "Wasteful" if none of the two above conditions is true.
# Examples:
# is_economical(14) ➞ "Equidigital"
# The prime factorization of 14 (2 digits) is [2, 7] (2 digits)
# Exponents equal to 1 are not counted
# is_economical(125) ➞ "Frugal"
# The prime factorization of 125 (3 digits) is [5^3] (2 digits)
# Notice how exponents greater than 1 are counted
# is_economical(1024) ➞ "Frugal"
# The prime factorization of 1024 (4 digits) is [2^10] (3 digits)
# is_economical(30) ➞ "Wasteful"

n = 125
prime_factors = {}


def result(n, prime_factors):
    if len(prime_factors) > 1:
        count = 0
        for k in prime_factors:
            count += len(str(k))
            if count > len(str(n)):
                print('Wasteful')
            elif count == len(str(n)):
                print('Equidigital')
            else:
                print('Frugal')

    elif len(prime_factors) == 1:
        count = 0
        for k, v in prime_factors.items():
            if v == 1:
                print('Equidigital')
            else:
                count += len(str(k)) + len(str(v))
                if count > len(str(n)):
                    print('Wasteful')
                elif count == len(str(n)):
                    print('Equidigital')
                else:
                    print('Frugal')


def prime_factor(n):
    m = n
    for i in range(2, m + 1):
        while not m % i and m >= i:
            if not i in prime_factors:
                prime_factors[i] = 1
                m = m // i
                if m == 1:
                    result(n, prime_factors)
            else:
                prime_factors[i] += 1
                m = m // i
                if m == 1:
                    result(n, prime_factors)


prime_factor(n)

"""" Measuring time between two code implementations """

import timeit

stmt_one ="""
l=[]
for x in range(100):
    if x%2 ==0:
        l.append(x)
"""
timeit.timeit(stmt=stmt_one, number= 1000000)

stmt_two ="""
l=[x for x in range(100) if x%2 ==0 ]
"""
timeit.timeit(stmt=stmt_two, number= 1000000)



