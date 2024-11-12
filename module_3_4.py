def single_root_words(root_words, *other_words):
    same_words = []
    root_list = root_words.lower()
    words_list_l = [word.lower() for word in other_words]
    i = 0
    for elem in words_list_l:
        if root_list in elem or elem in root_list:
            same_words.append(other_words[i])
        i += 1
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)