print ("Введите слово:")
word  = input()
lngh = len(word)
lngh2 = lngh // 2
print(word[lngh2:lngh]+word[0:lngh2])