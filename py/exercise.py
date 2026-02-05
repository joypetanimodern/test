text = """is a powerfull programming language. its easy to learn and versatile!. you can use python for web development, data science, and automation. the syntax is clean and readable. this make python perfext for beginer and 
expert alike."""

char_count =len(text)
char_count_no_space = (len(text.replace(' ','')))
# word_count = len(text.split())
# sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"character count (including space): {char_count}")
print(f"character count with no space: {char_count_no_space}")