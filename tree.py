import numpy as np

class Tree:
    def __init__(self,filename):
        self.file = open("{}".format(filename))
        self.node_dict = {}
        for node in self.file.readlines():
            parameter = node.strip().split(",")
            if len(parameter) == 4:
                self.node_dict[int(parameter[0])] = [parameter[1],parameter[2],[int(x) for x in parameter[3].split("|")],None]
            elif len(parameter) == 3:
                self.node_dict[int(parameter[0])] = [parameter[1],parameter[2],[],None]
        for uid in self.node_dict.keys():
            for key in self.node_dict.keys():
                if uid in self.node_dict[key][2]:
                    self.node_dict[uid][3] = key

    def node(self,uid,name=None,description=None,children=None):
        if uid in self.node_dict.keys():
            if name == None:
                name = self.node_dict[uid][0]
            if description == None:
                description = self.node_dict[uid][1]
            if children == None:
                children = self.node_dict[uid][2]
            parent = self.parent(uid)
        else:
            children = []
            parent = None
        self.node_dict[uid] = [name,description,children,parent]

    def parent(self,uid):
        return self.node_dict[uid][3]

    def move(self,uid,new_parent):
        if self.parent(uid) is not None:
            self.node_dict[self.parent(uid)][2].remove(uid)
        self.node_dict[new_parent][2].append(uid)
        self.node_dict[uid][3] = new_parent

    def delete(self,uid):
        if uid in self.node_dict[self.parent(uid)][2]:
            self.node_dict[self.parent(uid)][2].remove(uid)
            for child in self.node_dict[uid][2]:
                self.move(child,self.parent(uid))
        del self.node_dict[uid]

    def close(self,save=None):
        self.file.close()
        new_lines = []
        new_line = ""
        if save != None:
            save = open("{}".format(save),"w")
            for key in self.node_dict.keys():
                new_line = "{},{},{}".format(key,self.node_dict[key][0],self.node_dict[key][1])
                if self.node_dict[key][2] != []:
                    new_line += ","
                    new_line += "|".join(str(x) for x in self.node_dict[key][2])
                new_line += "\n"
                new_lines.append(new_line)
            save.writelines(new_lines)

if __name__ == "__main__":
    a = Tree("saves/test.save")
    a.node(3,name="new_node",description="a new node")
    a.move(3,1)
    print(a.node_dict)
    a.delete(1)
    print(a.node_dict)
    a.close(save="saves/other.save")