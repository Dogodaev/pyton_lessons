class PalindromeString(str):
    def is_palindrome(self):
        self = self.lower()
        i=0
        j= len(self)-1
        while i<j:
            if self[i] != self[j]:
                return False
            i = i+1
            j = j-1
        return True
    
word = PalindromeString('Радар')
print(word, word.is_palindrome())
