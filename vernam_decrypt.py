


class VernamDecrpyt:
    
    """
        Args: 
            Keyword: Keyword from opposite side
            Cipher: Password from the other side

        Return:
            Message: Main message of the other party
    """


    def __init__(
        self,
        keyword,
        cipher
    ):

        self.keyword = keyword
        self.cipher = cipher


        a = [(ord(i) - 97) - (ord(j) - 97) for i,j in zip(cipher, keyword)]
        k = [i + 26 if i < 0 else i for i in a]
        message = "".join(chr(main + 97) for main in k)
        print(message.upper())


Decrypt = VernamDecrpyt


