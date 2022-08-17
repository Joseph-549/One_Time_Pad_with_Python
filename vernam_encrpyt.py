import random
from string import ascii_lowercase

class VernamEncrypt:
    
    """
        Args:
            Message: The message you want to encrypt  (without space).

        Return:
            Your Message: The message you want to encrypt.
            Keyword: Randomly generated keyword in the length of your password
            Cipher: Main Cipher

    """

    def __init__(
        self,
        message,
    ):

        self.message = message

        
        control = 0
        keyword = ""
            
        while control < len(message):
            keyword += random.choice(list(ascii_lowercase))
            control += 1

        a = [(ord(i) - 97) + (ord(j) - 97) for i,j in zip(message, keyword)]
        k = [i - 26 if i > 26 else i for i in a]

        cipher = list("".join(chr(main + 97) for main in k))

        i = 0
        while i < len(cipher):
            if '{' in cipher[i]:
                    cipher[i] = 'a'
            i += 1

        cipher = "".join(cipher)

        if len(cipher) > 15:
            user_message = open("your_message.txt", "x")
            user_message.write(str(message))

            keyword_file = open("keyword.txt", "x")
            keyword_file.write(str(keyword))

            cipher_file = open("cipher.txt", "x")
            cipher_file.write(str(cipher))

        else:
            k = {
                "Message" : message.upper(),
                "Keyword" : keyword.upper(),
                "Cipher" : cipher.upper()
            }

            print(k)

Encrypt = VernamEncrypt
        


        





