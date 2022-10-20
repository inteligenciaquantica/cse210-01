
import random

class SecretWord:
    
    def __init__(self):
        self._word = ['bird','car','man','rocket','table','faith','bible','ship','heaven','uncommonly'] 
        self._secret_word = ''
        
        
    def get_word(self):           
        self._secret_word = self._word[random.randint(0,9)]      
    
    def get_secret_word(self):
        return self._secret_word