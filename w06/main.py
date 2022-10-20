from player import Player
from parachute import Parachute
from score import Score
from secret_word import SecretWord

def main():
    
    pr = Parachute()
    sc = Score()
    sw = SecretWord()
    
    for i in range(len(pr.get_parachute())):
        print(f"{pr.get_parachute()[i]}")
    
    pl = Player()
    
    sw.get_word()
    count = 0
    
    while count < 6:
        letter = input("Guess and type a letter, please! ")
        pl.set_guess_letter(letter)
    
        sc.calc_score(pl.get_guess_letter(),sw.get_secret_word())
        print(f"{sc.get_score()}")
        print(f"{sw.get_secret_word()}")
        pr.print_parachute(1,2,3)
        
        count+=1
    
    
    
    
if __name__ == "__main__":
    main()
