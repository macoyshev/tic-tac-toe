from os import scandir
from click import echo
import typer
from curses import wrapper
from cursor import Cursor
from tictactoe import TicTacToe
from settings import Settings


def play(screen):

    game = TicTacToe()

    if game.has_save():
        screen.addstr(0, 0, game.get_load_message())
        try:
            ans = screen.getkey()
        except:
            ans = None

        if ans == "y":
            game.load_save()

        game.erase_save()

    screen.addstr(0, 0, game.get_field())
    screen.addstr(game.field.HEIGHT, 0, game.get_menu())

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
            game.make_user_move()
            if game.is_move_success:
                screen.addstr(game.move_y, game.move_x, "x")

            if game.is_winner():
                break

            game.make_bot_move()
            if game.is_move_success:
                screen.addstr(game.move_y, game.move_x, "o")

            if game.is_winner():
                break

        if key == "s":
            game.save_game()
            screen.addstr(game.get_saved_message_height(), 0, game.get_saved_message())

        if key == "q":
            raise typer.Exit()

    screen.addstr(game.field.HEIGHT, 0, game.get_result())

    screen.refresh()
    screen.getch()


def main(rows: int, colums: int):
    try:
        Settings.setColums(colums)
        Settings.setRows(rows)
        wrapper(play)
    except AttributeError as err:
        typer.echo(err.args[0])


if __name__ == "__main__":
    # main(3, 3)
    typer.run(main)