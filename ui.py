import curses,numpy,time,glob,os
from tree import Tree


def which(root,list,x,y,x_ind,accept_non_int_outputs=True):
    win.addstr(y,x,root)
    for i in range((len(list))):
        line_y = y + i + 1
        win.addstr(line_y,x+x_ind,list[i])
    win.refresh()
    selection = 0
    old_selection = 0
    while True:
        if len(list) != 0:
            win.addstr(y+old_selection+1,x+x_ind,list[old_selection])
            win.addstr(y+selection+1,x+x_ind,list[selection],curses.A_REVERSE)
            win.refresh()

        c = win.getch()

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
        
        if c == ord('n'):
            return 'n'

        if c == ord('e'):
            return 'e'

        if c == ord('d'):
            return 'd'

def editMenu(cur_name,cur_description,new):
    pass

if __name__ == "__main__":
    win = curses.initscr()
    curses.noecho()
    curses.cbreak()
    win.keypad(True)
    curses.curs_set(0)
    

    saves = glob.glob("saves/*.save")

    tree = Tree(saves[which("Which save do you want to load?",saves,0,0,5,False)])

    win.clear()
    win.refresh()
    
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

        win.addstr(2+len(children),0,tree.node_dict[node][1]) 
        
        ipt = which(tree.node_dict[node][0],children_names,0,0,2) #get input

        if ipt == 'q': #quit
            break

        elif ipt == 'n': #new
            pass

        elif ipt == 'e': #edit
            pass

        elif ipt == 'd': #delete
            if parent != -1: #-1 as parent is the root node, shouldn't be deleted
                tree.delete(node)
                node = parent

        elif ipt == -1: #go back
            if parent != -1:
                node = parent
        
        else:
            if children != []: #go forward to selected node
                node = children[ipt]      

        win.clear()
        win.refresh()

    curses.nocbreak()
    win.keypad(False)
    curses.echo()
    curses.endwin()
