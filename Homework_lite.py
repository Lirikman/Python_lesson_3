import string

with open('text.txt', encoding='utf-8') as file:
        text = file.read()

text_new = text
for p in string.punctuation:
        if p in text_new:
                text_new = text_new.replace(p, '')

print(text_new)



