from collections import deque

def main():
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

    list1=G
    n=len(list1)
    print(n)
    color=[[]*1 for _ in range(n)]
    dist=[[]*1 for _ in range(n)]
    prev=[[]*1 for _ in range(n)]
    visited=[]
    for i in range(n) :
        color[i]='white'
        dist[i]=float('inf')
    s=int(input("Enter the source vertex\n"))
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
        color[v]='black'
    print(dist)
    print(color)
    print(visited)

if __name__ == '__main__':
    main()