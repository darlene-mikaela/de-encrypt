# de-encrypt
My private project I've been working on for a few days in January 2024. I am still trying to find ways to make it more efficient.

## caesar.py
caesar.py is a file containing a module to encrypt and decrypt capslocked text according to a certain key using the caesar cipher.

## vegenere.py
vegenere.py is a file containing a module using the vegenere table to encrypt and decrypt a sequence of capslocked letters. Also known as the polyalphabetic cipher.

## railfence.py
railfence.py is a module to encrypt and decrypt a string of text using the railfence cipher
### makeTable(self,text,rail="")
makeTable function takes only 1 argument, the text to make into the railfence. It arranges the string into a zigzag form by inserting it to the array
### encrpyt(self,plainText)
Also takes only 1 argument that is the text to cipher/encrypt. The function checks which direction it is going and assigns each of the chars in the plainText to the appropriate place in the railfence using the makeTable function. Then it outputs the cipher text by joining all of the chars per row.
### decrypt(self,cipher)
...
