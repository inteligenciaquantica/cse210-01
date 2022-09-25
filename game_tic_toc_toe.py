
#Author: Jorge de Oliveira Echeimberg
import numpy as np


def main():
    
    grid = []
    
    print('------ Tic-Toc-Toe ------\n')
    print('This game runs on a grid 3 rows and 3 columns\n')
    print('Each gamer chooses a number in the range 1 to n\n')
    dim = 1
    while dim < 3:
        dim = int(input('Type the dimension of your grid: ( 3, 4, 5,...)'))
    
    grid = dimension(dim)
    shows_grid(str(dim+1),str(dim+1),'1',grid,dim)
    p = 0
    end_game = False
    while end_game == False:
        player = '1'
        if p%2 != 0:
            player = '2'
    
        choose = int(input(f"Player {player} it's your time, choose a coordenate (1 up to {dim*dim}): "))
        map_coordenates(choose,player,grid,dim)
        
        p+=1
        
        if p == dim*dim and end_game == False:
            end_game= True
            print(f'Draw!')
        elif p < dim*dim:    
            end_game = end_game_test(grid,dim)
            if end_game == True:
                print(f'Player {player} congratulations, you win!')
            
    
    
def shows_grid(x,y,player,grid,dim):
    #this function updte the grid according to the player's choosing.
    x = int(x)
    y = int(y)
    
    for i in range(dim):
        line = ''
        sep = ''
        for j in range(dim):
            if x==i and y==j and player=='1':
                line = line + 'x|'
                grid[i][j]='x'
            elif x==i and y==j and player=='2':
                line = line + 'o|'
                grid[i][j]='o'
            else:
                line = line + f'{grid[i][j]}|'
            
            if j%2!=0:
                sep = sep + '-'
            else:  
                sep = sep + '+'      
        print(line)
        print(sep)   
    
def end_game_test(grid,dim):
    end_game2 = False
    d1 = ''
    d2 = ''
    
    #print(f'dim-1: {dim-1}   grid: {grid}')
    for i in range(dim):
        d1 = d1 + grid[i][i]
        d2 = d2 + grid[i][dim-i-1]
        l = ''
        c = ''
        for j in range(dim):
            l = l + grid[i][j]
            c = c + grid[j][i]
        
        if l.count('x') == dim or l.count('o') == dim or c.count('x') == dim or c.count('o') == dim:
            end_game2 = True

    if d1.count('x') == dim or d1.count('o') == dim:
            end_game2 = True 
              
    return end_game2    

def map_coordenates(choose,player,grid,dim):
    if choose <= dim and choose >= 1:
        coord = []
        for i in range(dim):
            for j in range(dim):
                coord.append(f"{i},{j}")
    
        x,y = coord[choose - 1].split(',')
    
        shows_grid(x,y,player,grid,dim)
    else:
        print(f"I'm sorry, the value you typed is less than 1 or more than {dim*dim}. Try again in your time, please!")

def dimension(dim):
    
    if dim >= 3:
        grid2 = [i for i in range(1,dim*dim+1)]
        grid2 = np.array(grid2)
        grid2 = grid2.reshape(dim,dim)
        grid2 = grid2.astype(str)
        
    else:
        print(f"I'm sorry, but you chose a dimension less than 3. Try again, please!")
         
    return grid2
     


       
if __name__=='__main__':
    main() 
    
    
