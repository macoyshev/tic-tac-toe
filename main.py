
import typer
from curses import wrapper
from field import Field


def init(width: int, height: int):
    Field.init(width, height)
    wrapper(main)
    

def main(stdscr):
    if Field.isThereSave():
        
    

if __name__ == "__main__":
    typer.run(init)