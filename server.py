# Sololearn Python Code Project 1: Letter Frequency

# Question: You are making a program to analyse text.
#           Take the text as the first input, and a letter as the second input,
#           and output the frequency of that letter in the text as a whole percentage.

# Sample Input:
# text: hello, letter: l

# Sample Output:
# 40

# Explanation: The letter l appears 2 times in the text hello, which has 5 letters.
# So the frequency would be (2/5)*100 = 40.

# My Solution:

# 1. Import the trunc function to convert decimals to whole number since our frequency is in percentage.
from math import trunc 

# 2. Accept a text as input.
text = input() 

# 3. Accept a letter as input.
letter = input()

# 4. Loop through the text.
for x in text:

    # 5. Check if any of the text matches the letter input.
    if x == letter:

        # 6. If yes, count the freq of the letter in the text.
        letterlen = text.count(x)

        # 7. Also count the length of the whole text.
        textlen = len(text)

# 8. Calculate the frequency with this formula.
freq = (letterlen/textlen) * 100

# 9. Print the frequency.
print(trunc(freq))

# Hossanadev :)