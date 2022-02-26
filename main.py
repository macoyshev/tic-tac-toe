import curses
import typer
from curses import wrapper
from cursor import Cursor
from tictactoe import TicTacToe
from settings import Settings


def play(screen):
    game = TicTacToe()

    if game.hasSave():
        screen.addstr(
            0,
            0,
            "Press 'y' to load last saved game, otherwise any key to start new game...\n",
        )
        if screen.getkey() == "y":
            game.loadSave()
        game.eraseSave()

    game.displayField(screen)
    game.displayMenu(screen)

    while not game.field.isFull():
        screen.move(game.cursor.y, game.cursor.x)
        screen.refresh()
        try:
            key = screen.getkey()
        except:
            key = None

        if key == "KEY_UP":
            game.cursor.move(Cursor.UP)

        if key == "KEY_DOWN":
            game.cursor.move(Cursor.DOWN)

        if key == "KEY_LEFT":
            game.cursor.move(Cursor.LEFT)

        if key == "KEY_RIGHT":
            game.cursor.move(Cursor.RIGHT)

        if key == "x":
            game.userMove(screen)
            game.botMove(screen)

        if key == "s":
            game.saveGame()
            game.saveSuccessMessage(screen)

        if key == "q":
            raise typer.Exit()
        

def main(rows: int, colums: int):
    Settings.colums = colums
    Settings.rows = rows
    
    wrapper(play)


if __name__ == "__main__":
    # typer.run(main)
    main(3,3)
