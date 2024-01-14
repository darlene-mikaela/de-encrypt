class Caesar:
  def toCipher(key,plain):
    cipher = ""
    plain = plain.upper()
    for plains in plain:
      if ord(plains) >= 65 and ord(plains) <= 90:
        cipher += chr((ord(plains)+key-65)%26 + 65)
      else:
        cipher += plains
    return cipher

  def toPlain(key,cipher):
    plain = ""
    cipher = cipher.upper()
    for ciphers in cipher:
      if ord(ciphers) >= 65 and ord(ciphers) <= 90:
        plain += chr((ord(ciphers)-key+65)%26 + 65)
      else:
        plain += ciphers
    return plain

print(Caesar.toPlain(3, "CHEUD, ZRUOG!"))
print(Caesar.toCipher(3, "ZEBRA, WORLD!"))
