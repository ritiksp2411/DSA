class Node:
    def __init__(self,x):
        self.val = x
        self.parent = self
        self.rank = 0

    def __str__(self):
        return str(self.val)

class DisjointSets:

    def makeset(self,node):
        node1= Node(node)
        return node1

    def findset(self,node):
        if(node.parent==node):
            return node
        node.parent=self.findset(node.parent)
        return node.parent
    
    def union(self,node1,node2):
        rx=self.findset(node1)
        ry=self.findset(node2)
        if(rx.rank==ry.rank):
            rx.parent=ry
            ry.rank+=1
        elif(rx.rank>ry.rank):
            ry.parent=rx
        else :
            rx.parent=ry

   
def main():
    ds = DisjointSets()
    
    nodes = []
    for i in range(10):
        node = ds.makeset(i)
        nodes.append(node)

    ds.union(nodes[0],nodes[1])
    print(ds.findset(nodes[0]))    # Should print 1
    ds.union(nodes[3],nodes[2])
    print(ds.findset(nodes[2]))    # Should print 1
    ''' Add more tests!'''
    ds.union(nodes[3],nodes[0])
    print(ds.findset(nodes[2]))
if __name__ == '__main__':
    main()