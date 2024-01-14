import re

class Polyalpha:
  def __init__(self, vegenere="", chars=""):
    self.chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    vegeneres = []
    for i in range(26):
      vegeneres.append(self.chars)
      self.chars = self.chars[1:] + [self.chars[0]]
    self.vegenere = vegeneres

  def encrypt(self,keyword,plainText):
    #initialize
    cipher = ""
    #remove non alphabetic
    plainText = re.sub(r'[^A-Z]+', '', plainText)

    #make pairs
    pairs = []
    for j in range(len(plainText)):
      pairs.append([keyword[j%len(keyword)],plainText[j]])

    #crosses in vegenere
    for pair in pairs:
      x = self.chars.index(pair[0])
      y = self.chars.index(pair[1])
      cipher += self.vegenere[x][y]

    return cipher

  def decrypt(self,keyword,cipher):
    plain = ""
    #buat pasangan
    pairs = []
    for j in range(len(cipher)):
      pairs.append([keyword[j%len(keyword)],cipher[j]])

    #cari baris dari keyword, cari kolom dari cipher
    for pair in pairs:
      y = self.chars.index(pair[0])
      x = self.vegenere[y].index(pair[1])
      plain += self.vegenere[0][x]
    return plain

print(Polyalpha().decrypt("UCSBY","OPAWCLUAUYMEAQSNTS"))
# OPAWCLUAUYMEAQSNTS
