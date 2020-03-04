global time
time=0
def dfs1(Grev, u, visited, topo, finish, start):
    global time
    start[u] = time
    time += 1
    visited[u] = 1
    for v in Grev[u]:
        if visited[v]==0:
            dfs1(Grev, v, visited, topo, finish, start)
    finish[u] = time
    time = time+1
    topo.append(u)

def dfs(G, u, visited, finish, start):
    global time
    start[u] = time
    time += 1
    visited[u] = 1
    print(u, end=" ")
    for v in G[u]:
        if visited[v]==0:
            dfs(G, v, visited, finish, start)
    finish[u] = time
    time = time+1

def main():
    ''' Adjacency List representation. G is a list of lists. '''
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
    n = len(G)
    visited = [0]*n
    start = [0]*n
    finish = [0]*n
    topo = [0]*n
    Grev = [[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            Grev[j].append(i)

    for i in range(n):
        if visited[i]==0:
            dfs1(Grev, i, visited, topo, finish, start)
    visited = [0]*n
    start = [0]*n
    finish = [0]*n
    for i in topo:
        if visited[i]==0:
            dfs(G, i, visited, finish, start)
            print()

    print(Grev)
    print(G)

if __name__ == '__main__':
    main()