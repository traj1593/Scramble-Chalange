'''
Program: Scramble challenge
Filename: scrambleChallenge-tRaj-00.py
Author: Tushar Raj
Revisions: No revisions made
Description:
    Scrambled Words
    The source code below defines four encoded common English words.
    Each word is 7 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions in your solution.
'''
print("Scramble Challenge:\n")

z = [('v', 'c', 'l', 6, 'r'), ('i', 'a', 'i', 4, 't'),
     ('a', 'f', 'g', 1, 'p'), ('h', 'n', 'r', 3, 's'),
     ('e', 'e', 'a', 7, 'e'), ('c', 'i', 'o', 2, 'a'),
     ('e', 'n', 'l', 5, 'u')]


# Step 1:   Sort the tuples based on the integer value in each.  Use a
#           lambda construct to provide the sort key.

z.sort(key=lambda a:a[3]) #picking up the 4th position character from the tuple inside the list and sorting on the basis of that

# Step 2:   Use a list comprehension to create a list of characters
#           for each word.

s=[[j[i] for j in z] for i in range(len(z[1])) if i != 3] #itterating through tuple length skipping index postion 3 and adding all element from one index position in one list

# Step 3:   Use the join() method to create a string for each of the 
#           four words and print them.

print (' '.join([''.join(i) for i in s])) #joining the list of element together and seperating them by space

print("\n***Scramble Challenge Ended***")
