import typer
from curses import wrapper

def init(width: str, height: str):
    typer.echo(f"w:{width}, h: {height}")
    wrapper(main)
    

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "hello")
    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    typer.run(init)