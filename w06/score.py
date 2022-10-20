


class Score:
    
    
    def __init__(self):
        self._score = False
        
    def calc_score(self,letter,word):
        word = str(word)
        letter = str(letter)
        for w in word:
            print(f"w: {w} letter: {letter} word: {word}")
            if word.find(letter):
                
                self._score = True
            else:
                self._score = False
                
        print(f"self._score: {self._score}")    
            
            
    def get_score(self):
        return self._score
            