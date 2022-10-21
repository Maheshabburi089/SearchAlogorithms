def runbfs(startnode='A',target='T'):
    graph = {
             'A':['B','C','D'], 'B':['A'], 'C':['A','E'], 'D':['A','E'], 'E':['G','F','C','D'],'F':['H','I','E'], 'G':['E','I'],
             'H':['K','J','F'], 'I':['K','L','G','F'],'J':['M','H'], 'K':['N','I','H'], 'L':['N','S','I'], 'M':['O','J'],
             'N':['Q','O','K','L'],'O':['P','R','M','N'], 'P':['T','O'], 'Q':['S','R','N'], 'R':['T','Q','O'],'S':['L','Q'], 'T':['P','R']
             }
    visited = [] #list for visited nodes
    queue = [] #initialize a queue
    result = []
    visited.append(startnode)
    queue.append(startnode)
    while queue:
        s = queue.pop(0)
        result.append(s)
        if(s == target):
            break
        for adj in graph[s]:
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)

    print("path of BFS is:", result)
runbfs('A','T')