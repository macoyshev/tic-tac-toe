
import typer
import curses
from curses import wrapper
from tictactoe import TicTacToe
from settings import Settings


def init(rows: int, colums: int):
    Settings.rows(rows)
    Settings.colums(colums)
    wrapper(main)
    
def play(screen, game: TicTacToe):
    y, x = 0, 1
    while True:
        screen.move(y, x)
        screen.refresh()
        
        try:
            key = screen.getkey()
        except:
            key = None
            
        if key == "KEY_UP":
            if (y > 0):
                y -= 1
                
        if key == "KEY_DOWN":
            if (y < game.field.height - 1):
                y += 1
                
        if key == "KEY_LEFT":
            if (x > 1):
                x -= 2
                
        if key == "KEY_RIGHT":
            if (x < game.field.width - 2):
                x += 2
                
        if key == "x":
            if [y, x] not in game.field.userMoves and [y, x] not in game.field.botMoves:
                game.field.addUserMove(y, x)
                game.field.addBotMove()
                
                # if game.winner():
                #     return game.winner()
                
                if game.field.isFull():
                    return "draw"
                
                botMove = game.field.getLastBotMove()
            
                screen.addstr(y, x, "x") 
                screen.addstr(botMove[0], botMove[1], "o")
        
        if key == "s":
            game.saveGame()
            
            screen.addstr(game.field.height + 2, 0, "game saved")
        if key == "q":
            raise typer.Exit()
        

def drawField(screen, game: TicTacToe):
    for x in range(game.field.width):
        for y in range(game.field.height):
            if x % 2 == 0:
                screen.addstr(y, x, "|")


def main(screen):
    game = TicTacToe()
    
    if game.searchSaves():
        screen.addstr(0, 0, game.loadSaveMessage)
        answer = screen.getkey()
        if answer == 'y':
            game.loadSave()
        game.eraseSaves()
    
    screen.clear()

    drawField(screen, game)
    
    for move in game.field.userMoves:
        x = move[1]
        y = move[0]
        screen.addstr(y, x, "x")
    
    for move in game.field.botMoves:
        x = move[1]
        y = move[0]
        screen.addstr(y, x, "o") 
    
    x, y = 1, 0
    
    screen.addstr(game.field.height, 0,"press 'q' to quit")
    screen.addstr(game.field.height + 1, 0,"press 's' to save")

    res = play(screen, game)
    
    screen.clear()
    if res in ["bot", "user"]:
        screen.addstr(0, 0, f"WINNER: {res}")
    else:
        screen.addstr(0, 0, f"DRAW")
    
    screen.getch()     
         
if __name__ == "__main__":
    typer.run(init)