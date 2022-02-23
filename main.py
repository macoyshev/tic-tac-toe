import curses
import typer
import curses
from curses import wrapper
from field import Field


def init(width: int, height: int):
    Field.init(width, height)
    wrapper(main)
    

def main(screen):
    if Field.isThereSave():
        screen.clear()
        screen.addstr(0,0, "There is game save, want to load ?")
        key = screen.getkey()
        
        if key == "y":
            Field.loadSave();
            
    for x in range(Field.getWidth()):
        for y in range(Field.getHeigth()):
            if x % 2 == 0:
                screen.addstr(y, x, "|")
    
    for move in Field.getMoves():
        x = move[0]
        y = move[0]
        screen.addstr(y, x, "X")
    
    x, y = 1, 0

    while True:
        screen.move(y, x)
        screen.refresh()
        try:
            key = screen.getkey()
        except:
            key = None
            
        if key == "KEY_UP":
            if (y > 0):
                y-=1
        if key == "KEY_DOWN":
            if (y < Field.getHeigth() - 1):
                y+=1
        if key == "KEY_LEFT":
            if (x > 1):
                x-=2
        if key == "KEY_RIGHT":
            if (x < Field.getWidth() - 2):
                x+=2
        if key == "x":
            screen.addstr(y,x, "x")
        if key == "q":
            raise typer.Exit()
        
         
if __name__ == "__main__":
    typer.run(init)