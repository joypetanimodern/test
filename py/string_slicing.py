#string indexing and slicing

from pyexpat.errors import messages


text = "emir izzat hensem"

print(text[0])         #first character
print(text[-1])        #last character
print(text[0:6])       #slice 0 to 5 
print(text[:6])        #from start to 5
print(text[7:])        #7 to end

#string method

name = "emir izzat ensem"

print(len(name))
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
(name.replace("emir", "farhan"))

#string formatting

name = "mad"
age = 45
hobby = "cook"
school = "smk"

messages_1 = f"my name is {name} and i am {age} years old. my hobby is {hobby} and also my school name is {school}."

print(messages_1)



#exercise
text = """python is a powerfull programming language, its easy to learn and versatile you can use python for web development data science and automation, the scientax is clean and readable. this makes python perfect for beginner and expert"""

char_count = len(text)
char_count_no_spaces = (len(text.replace(' ', '')))
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"character count (incluiding space):{char_count}")
print(f"character count with no space):{char_count_no_spaces}")
print(f"word count:{word_count}")
print(f"sentence count:{sentence_count}")