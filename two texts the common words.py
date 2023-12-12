#problem: Given two texts, find the common words between them.
text1 = "This is a sample text document."
text2 = "A text document may contain in multiple words."

words1 = text1.lower().split()
words2 = text2.lower().split()
common_words = set(words1) & set(words2)
print("Text 1:", words1)
print("Text 2:", words2)
print("Common Words:", list(common_words))
