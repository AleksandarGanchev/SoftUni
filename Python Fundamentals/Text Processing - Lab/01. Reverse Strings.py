word = input()
reversed_word = ''
while word != 'end':
   for letter in reversed(word):
        reversed_word += letter

   print(f"{word} = {reversed_word}")
   reversed_word = ''

   word = input()