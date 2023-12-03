alphabet = input()
shift = int(input())
while shift > len(alphabet) or shift < 0:
    if shift > len(alphabet):
        shift -= len(alphabet)
    else:
        shift += len(alphabet)
enc_alphabet = ''
dec_alphabet = ''
for i in range(len(alphabet)):
    enc_alphabet += alphabet[i - (len(alphabet) - shift)]
    dec_alphabet += alphabet[-shift + i]
print(f'{enc_alphabet}\n'
      f'{alphabet}\n'
      f'{dec_alphabet}')