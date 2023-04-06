

class Anagram:
    
    def __init__(self,word):
        self.word=word
    
    def match(self,anagrams):
        matches=[]
        for word in anagrams:
            if sorted(self.word) == sorted(word):
                matches.append(word)
            
        return matches