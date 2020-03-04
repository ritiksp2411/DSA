
from collections import deque
def BFS(p,s):
    list1=p
    flag=0
    n=len(list1)
    color=[[]*1 for _ in range(n)]
    dist=[[]*1 for _ in range(n)]
    prev=[[]*1 for _ in range(n)]
    visited=[]
    for i in range(n) :
        color[i]='white'
        dist[i]=float('inf')
    dist[s]=0
    color[s]='gray'
    q=deque()
    q.append(s)
    visited.append(s)
    while(len(q)!=0):
        u=q.popleft()
        for v in list1[u]:
            if(color[v]=='white'):
                color[v]='gray'
                dist[v]=dist[u]+1
                prev[v]=u
                q.append(v)
                visited.append(v)
            else:
                if(dist[u]==dist[v]):
                    flag=1      
        color[v]='black'
    if(flag==1):
    	print("non bipartite")
    else:
        print("bipartite")
    return visited

def Inp():
    G = [] 

    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()
    return G

def main():
    grap=Inp()
    n=len(grap)
    comp=[0]*n
    i=0
    k=1
    for i in range(n):
        if(comp[i]==0):
            vis=BFS(grap,i)
            for j in vis:
                comp[j]=k
            k=k+1
    print(k-1)
        
if __name__ == '__main__':
    main()