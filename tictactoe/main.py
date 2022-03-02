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

        ans = screen.getkey()

        if ans == "y":
            game.load_save()

        game.erase_save()

    screen.addstr(0, 0, game.get_field())
    screen.addstr(game.field.HEIGHT, 0, game.get_menu())

    while not game.field.is_full():
        screen.move(game.cursor.y, game.cursor.x)
        screen.refresh()

        key = screen.getkey()
  
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

            if game.is_move_success:
                game.make_bot_move()
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


def main(rows: int = typer.Argument(3), colums: int = typer.Argument(3)):
    try:
        Settings.set_colums(colums)
        Settings.set_rows(rows)
        wrapper(play)
    except AttributeError as err:
        typer.echo(err.args[0])


if __name__ == "__main__":
    typer.run(main)
