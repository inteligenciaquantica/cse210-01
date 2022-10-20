

class Parachute:
    
    def __init__(self):
      
        self._parachute = [" _____ ","/     \\","-------","\\     /"," \\   /","   0   ","  /|\\","  / \\ ","^^^^^^^^"]
        
        
        
    def get_parachute(self):
        return self._parachute
    
    def print_parachute(self,score,count,word):
        start = 0
        
        
        for i in range(len(self.get_parachute())):
            print(f"{self._parachute[i]}")
            
        
        
    