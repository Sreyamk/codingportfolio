Description
This Python program merges two lists by inserting the second list into the first list starting immediately after the original elements of the first list.

It first takes the size of the first list (li1) as input.

Then, it takes input values for the first list (li1) and the second list (li2).

Finally, it copies all elements from the second list (li2) into the first list (li1) starting after the original elements of li1.

⚡ Important:

The first list li1 must have enough extra space allocated initially to hold the new elements.
Otherwise, you will get an IndexError because Python lists don't automatically expand like arrays in C.

How to Run
Make sure you have Python installed.

Save the code in a file, say merge_lists.py.

Run the script:

bash
Copy
Edit
python merge_lists.py
Input the values as the program prompts.

Example
bash
Copy
Edit
enter size of l1 3
1 2 3
4 5 6 7
li1 = [1, 2, 3]

li2 = [4, 5, 6, 7]

After merging, the output will be:

csharp
Copy
Edit
[1, 2, 3, 4, 5, 6, 7]
