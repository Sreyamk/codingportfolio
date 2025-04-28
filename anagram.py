
str1 = input("Enter a word: ")
str2 = input("Enter another word: ")
l1 = len(str1)
l2 = len(str2)

if l1 != l2:
    print("Not an anagram")
else:
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        print("An anagram")
    else:
        print("Not an anagram")