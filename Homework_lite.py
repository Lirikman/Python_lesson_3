# 1. методами строк очистить текст от знаков препинания

with open('text.txt', encoding='utf-8') as file:
        text = file.read()

marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_«»—'''

for x in marks:
        text = text.replace(x, '')

print(text)

#Альтернативное решение, правда не удаляет символы « » — (скорее всего они не включены в знаки пунктуации модуля strings Python)
# import string
#
#with open('text.txt', encoding='utf-8') as file:
#        text = file.read()
#
#for p in string.punctuation:
#        if p in text:
#                text = text.replace(p, '')
#
#print(text)


#2. сформировать list со словами (split)

word_list = []

for i in text.split():
     word_list.append(i)

print(word_list)

#3. привести все слова к нижнему регистру (map)

new_list = list(map(lambda x: x.lower(), word_list))

print(new_list)

# 4. получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте
word_dict = dict()
new_list.sort()

for word in new_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict)

#5. вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)

sorted_dict = {}
sorted_keys = sorted(word_dict, key=word_dict.get)

for w in sorted_keys:
    sorted_dict[w] = word_dict[w]

print(sorted_dict)

a = set(new_list)
print('Количество разных слов в тексте: ', len(a))