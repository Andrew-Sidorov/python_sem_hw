# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:

str = (input('Введите слово на русском или ангийском: '))
my_dict1 = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
            4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}

print(my_dict1)


# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т = 1, 1, 1, 1, 1, 1, 1, 1, 1
# Д, К, Л, М, П, У = 2, 2, 2, 2, 2, 2
# Б, Г, Ё, Ь, Я = 3, 3, 3, 3, 3
# Й, Ы = 4, 4
# Ж, З, Х, Ц, Ч = 5, 5, 5, 5, 5
# Ш, Э, Ю = 8, 8, 8
# Ф, Щ, Ъ = 10, 10, 10

# my_dict[i] = my_dict.get(i, 0)+1
