import re

S = "hello WORLD 123"
count_S = len(S)

proStr = S.title()
count_proStr = len(proStr)
revStr = proStr[::-1]

pattern = r'[AEIOUaeiou]' 
match = re.findall(pattern, S)

acronym = ''.join(word[0].upper() for word in S.split() if word)

encode = S.encode('utf-8').upper()
count_encode = len(encode)
encode_hex = S.encode('utf-8').hex()

print(f'Original Input: \" {S} \"')
print(f'Processed String: \"{proStr}\"')
print(f'Reversed String: \"{revStr}\"')
print(f'Vowel count: {len(match)}')
print(f'Acronym: {acronym}')
print(f'UTF-8 encoded: {encode}')
print(f'UTF-8 encoded (hex): {encode_hex}')
print(f'Original length: {count_S}')
print(f'Processed length: {count_proStr}')
print(f'Encoded length: {count_encode}')