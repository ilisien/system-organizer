import curses,numpy,time,glob,os
from tree import Tree


def which(root,list,x,y,x_ind,accept_non_int_outputs=True):
    stdscr.addstr(y,x,root)
    for i in range((len(list))):
        line_y = y + i + 1
        stdscr.addstr(line_y,x+x_ind,list[i])
    stdscr.refresh()
    selection = 0
    old_selection = 0
    while True:
        if len(list) != 0:
            stdscr.addstr(y+old_selection+1,x+x_ind,list[old_selection])
            stdscr.addstr(y+selection+1,x+x_ind,list[selection],curses.A_REVERSE)
            stdscr.refresh()

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

        if (c == curses.KEY_LEFT) and (accept_non_int_outputs == True):
            return -1

        if c == curses.KEY_RIGHT:
            return selection

        if c == ord('q'):
            return 'q'


if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)
    

    saves = glob.glob("saves/*.save")

    tree = Tree(saves[which("Which save do you want to load?",saves,0,0,5,False)])

    stdscr.clear()
    stdscr.refresh()
    
    node = 0
    while True:
        parent = -1
        children = tree.node_dict[node][2]
        children_names = []
        for child in children:
            children_names.append(tree.node_dict[child][0])

        for key in tree.node_dict.keys():
            for i in tree.node_dict[key][2]:
                if i == node:
                    parent = key

        stdscr.addstr(2+len(children),0,tree.node_dict[node][1]) 
        
        ipt = which(tree.node_dict[node][0],children_names,0,0,2)

        if ipt == 'q':
            break

        if ipt == -1:
            if parent != -1:
                node = parent

        else:
            if children != []:
                node = children[ipt]      

        stdscr.clear()
        stdscr.refresh()

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
