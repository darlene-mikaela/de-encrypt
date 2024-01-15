import re

class Polygraph:
  #create table
  def __init__(self,key,tables="",pairs=""):
    self.key = list(key)

    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    table = [[keys for keys in key]]
    keyLen = len(key)

    #remove keys
    for char in chars:
      if char in key:
        chars.remove(char)

    while len(chars) >= keyLen:
      table.append(chars[:keyLen])
      chars = chars[keyLen:]
    table.append([j for j in chars])
    for i in range(keyLen-len(chars)):
      table[-1].append("?")

    chars = ""
    for i in range(len(table[0])):
      for j in range(len(table)):
        chars += (table[j][i])
    chars = re.sub("[^A-Z0-9]+", "", chars)

    table = []
    while len(chars) >= 6:
      table.append(list(chars[:6]))
      chars = chars[6:]

    self.tables = table

  #find coordinates
  def findCoor(self,search,arr):
    for i in range(len(arr)):
      for j in range(len(arr[i])):
        if arr[i][j] == search:
          return i,j

  #generate pairs
  def makePairs(self,text):
    pairs = []
    for k in range(2, len(text)+1, 2):
      pairs.append(list(text[k-2:k]))
    return pairs

  def encrypt(self,plain):
    cipher = ""
    pairs = self.makePairs(plain)


    for pair in pairs:
      x1,y1 = self.findCoor(pair[0], self.tables)
      x2,y2 = self.findCoor(pair[1], self.tables)
      if x1==x2:
        cipher += self.tables[x1][y1%5+1] + self.tables[x2][y2%5+1]
      elif y1 == y2:
        cipher += self.tables[x1%5+1][y1] + self.tables[x2%5+1][y2]
      else:
        cipher += self.tables[x1][y2] + self.tables[x2][y1]

    return cipher

  def decrypt(self, cipher):
    plain = ""
    pairs = self.makePairs(cipher)

    for pair in pairs:
      row1,col1 = self.findCoor(cipher[0], self.tables)
      row2,col2 = self.findCoor(cipher[1], self.tables)
      cipher = cipher[2:]

      if row1==row2:
        cipher += self.tables[row1][col1%5-1] + self.tables[row2][col2%5-1]
      elif col1 == col2:
        cipher += self.tables[row1%5-1][col1] + self.tables[row2%5-1][col2]
      else:
        cipher += self.tables[row1][col2] + self.tables[row2][col1]

    return cipher

print(Polygraph("UCS02").decrypt("4J52NIDYO95B58ANYU"))
print(Polygraph("UCS02").encrypt("UNIVERSITASCIPUTRA"))
# 4J52NIDYO95B58ANYU
# UN-IV-ER-SI-TA-SC-IP-UT-RA
