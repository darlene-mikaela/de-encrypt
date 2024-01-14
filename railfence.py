class Railfence:
  def __init__(self,key):
    self.key = key

  def makeTable(self,text,rail=""):
    return [['*' for i in range(len(text))]
            for j in range(self.key)]

  def encrypt(self,plainText):
    cipher = ""
    rail = self.makeTable(plainText)

    down = False
    row, col = 0, 0

    #place items
    for i in range(len(plainText)):
      if row==0 or row==self.key-1:
        down = not down

      rail[row][col] = plainText[i]
      col += 1

      row = row + 1 if down else (row -1)

    #cipher
    for rails in rail:
      for railss in rails:
        if railss != "*":
          cipher += railss

    return cipher

  def decrypt(self,cipher):
    plain = ""
    rail = self.makeTable(cipher)

    down = None
    row,col = 0,0
    for i in range(len(cipher)):
      if row==0:
        down = True
      elif row==self.key-1:
        down = False

      rail[row][col] = "&"
      col += 1
      row = (row+1) if down else (row-1)

    #place items   
    index = 0 
    for i in range(len(rail)):
      for j in range(len(rail[i])):
        if rail[i][j] == "&" and index < len(cipher):
          rail[i][j] = cipher[index]
          index += 1

    row,col = 0,0
    for i in range(len(cipher)):
      if row==0:
        down = True
      elif row==self.key-1:
        down = False

      if rail[row][col] != "*":
        plain += rail[row][col]
        col += 1
      row = (row+1) if down else (row-1)

    return plain


print(Railfence(5).encrypt("UNIVERSITASCIPUTRA"))
print(Railfence(5).decrypt("UTRNIATAISSUVRCPEI"))
