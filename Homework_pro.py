import pymorphy2

#1. в пункте 3 дополнительно к приведению к нижнему регистру выполнить лемматизацию

with open('text.txt', encoding='utf-8') as file:
    text = file.read()

marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_«»—'''

for x in marks:
    text = text.replace(x, '')

word_list = []

for i in text.split():
        word_list.append(i)

new_list = list(map(lambda x: x.lower(), word_list))

lemmat_word = ''

morph = pymorphy2.MorphAnalyzer()

for i in new_list:
    p = morph.parse(i)[0].normal_form
    lemmat_word += p + ' '

lemmat_list = []

for i in lemmat_word.split():
        lemmat_list.append(i)

print(lemmat_list)