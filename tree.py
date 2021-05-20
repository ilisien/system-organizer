import numpy as np

class Tree:
    def __init__(self,filename):
        self.file = open("{}".format(filename))
        self.node_dict = {}
        for node in self.file.readlines():
            parameter = node.strip().split(",")
            if len(parameter) == 4:
                self.node_dict[int(parameter[0])] = [parameter[1],parameter[2],[int(x) for x in parameter[3].split("|")]]
            elif len(parameter) == 3:
                self.node_dict[int(parameter[0])] = [parameter[1],parameter[2],[]]

    def node(self,uid,name=None,description=None,children=None):
        if name == None:
            name = self.node_dict[uid][0]
        if description == None:
            description = self.node_dict[uid][1]
        if children == None:
            children = self.node_dict[uid][2]
        self.node_dict[uid] = [name,description,children]

    def move(self,uid,new_parent):
        for key in self.node_dict.keys():
            if uid in self.node_dict[key][2]:
                self.node_dict[key][2].remove(uid)
        self.node_dict[new_parent][2].append(uid)

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
    a.node(1,name="child1")
    print(a.node_dict)
    a.close(save="saves/test.save")