# List of keywords that are considered spam
spam_keywords = ["Make a lot of money", "buy now", "subscribe this", "click this"]

# Taking input from the user for a comment and converting it to lowercase for case-insensitive comparison
spam_comments = input("Please enter your spam comment: ").lower()

# Checking if any of the spam keywords are present in the comment
# The 'any()' function returns True if any keyword from the spam_keywords list is found in spam_comments
if any(keyword.lower() in spam_comments for keyword in spam_keywords):
    # If a spam keyword is found in the comment, print "this is a spam"
    print("This is a spam")
else:
    # If none of the keywords are found, print "this is not a spam"
    print("This is not a spam")
