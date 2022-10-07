"""
File: anagram.py
Name: Chunya Tsai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    input a character, anagram.py will list all anagrams for the character
    """
    s = ''
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while s != EXIT:
        s = str(input('Find anagrams for: '))
        s = string_manipulation(s)
        if s == EXIT:
            break
        print('Searching...')

        start = time.time()

        d = simplify_dictionary(read_dictionary(), s)
        s_count = {}                                    # key = letters, value = the numbers of each letter in s
        count_char(s, s_count)
        find_anagrams(s, s_count, d)

        end = time.time()

        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def string_manipulation(s):
    # coverts the inputted string to lowercase and remove
    s1 = ''
    for ch in s:
        if ch.isalpha():
            s1 += ch.lower()
        else:
            s1 = '-1'
            print('Error Format!')
    return s1


def count_char(s, s_count):
    # input 'key = letters', 'value = the numbers of each letter in s' to s_count
    for s1 in s:
        if s1 not in s_count:
            s_count[s1] = 1
        else:
            s_count[s1] += 1


def read_dictionary():
    """
    :return: a list includes all characters in 'FILE'
    """
    temp_l = []
    with open(FILE, 'r') as f:
        for line in f:
            temp_l += line.split()
    return temp_l


def simplify_dictionary(d, s):
    """
    :param d: a list, original dictionary
    :param s: a string, the character user would like to find anagrams
    :return: a dictionary, key = letters, value = all characters starts from key,
             only includes those characters with the same length as s and starts from the letters in s
    """
    char_s = []  # all letters in s
    s_d = {}  # simplified dictionary, key = first letter, value = characters
    for i in range(len(s)):
        if s[i] not in char_s:
            char_s.append(s[i])

    for i in range(len(char_s)):
        temp_l = []
        for j in range(len(d)):
            if char_s[i] == d[j][0] and len(s) == len(d[j]):
                temp_l.append(d[j])
        s_d[char_s[i]] = temp_l
    return s_d


def find_anagrams(s, s_count, d):
    """
    :param s: a string,
    :param s_count: a dict, key = each character, value = number of times
    :param d: a dict, simplified dictionary
    :return: boolean, if s is in d
    """
    char = ''
    combination = []                                                    # a list for all anagrams
    find_anagrams_helper(s, s_count, char, len(s), combination, d)
    print(len(combination), ' anagrams:', combination)


def find_anagrams_helper(s, s_count, char, s_length, combination, d):
    if len(char) == s_length:
        if char in d[char[0]]:
            print('Found: ' + char)
            print('Searching...')
            combination.append(char)
    else:
        for c in s:
            if c in char and s_count[c] <= 0:
                pass
            else:
                # Choose
                char += c
                s_count[c] -= 1
                if char in combination:
                    break

                # Explore
                if has_prefix(char, d):
                    find_anagrams_helper(s, s_count, char, s_length, combination, d)

                # Un-choose
                s_count[char[len(char) - 1]] += 1
                char = char[:-1]


def has_prefix(sub_s, d):
    """
    :param sub_s:
    :param d: a dict, simplified dictionary
    :return: boolean, is there characters in d starts from sub_s
    """
    for i in range(len(d[sub_s[0]])):
        if d[sub_s[0]][i].startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
