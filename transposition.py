def transposition(key, plainText):
  table = []
  cipherText = ""
  plainText = plainText.upper()

  while len(plainText) >= len(key):
    table.append([plainText[i] for i in range(5)])
    plainText = plainText[5:]
  table.append([chars for chars in plainText])
  for i in range(len(key)-len(plainText)):
    table[-1].append("X")

  for cipher in key:
    for rows in table:
        cipherText += rows[cipher-1]

  return cipherText

print(transposition([4,3,1,5,2],"TRANSPOSITION"))
