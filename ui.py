import curses,numpy,time
from tree import Tree

def which(root,list,x,y,x_ind):
    stdscr.addstr(y,x,root)
    for i in range((len(list))):
        line_y = y + i + 1
        stdscr.addstr(line_y,x+x_ind,list[i])
    stdscr.refresh()
    selection = 0
    old_selection = 0
    while True:
        c = stdscr.getch()

        if c == curses.KEY_UP:
            if selection == 0:
                pass
            else:
                old_selection = selection
                selection -= 1

        if c == curses.KEY_DOWN:
            if selection == len(list)-1:
                pass
            else:
                old_selection = selection
                selection += 1

        if c == curses.KEY_LEFT:
            return -1

        if c == curses.KEY_RIGHT:
            return selection

        stdscr.addstr(y+old_selection+1,x+x_ind,list[old_selection])
        stdscr.addstr(y+selection+1,x+x_ind,list[selection],curses.A_REVERSE)
        stdscr.refresh()



if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)

    which("title:",["a","b","c"],0,0,2)
    time.sleep(10)

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
