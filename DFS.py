def RunDfs(Source= 'A', target='T'):
        dfsResult=[]
        visited =set()
        graph ={'A':['B','C','D'], 'B':['A'], 'C':['A','E'], 'D':['A','E'], 'E':['G','F','C','D'],'F':['H','I','E'], 'G':['E','I'],
                 'H':['K','J','F'], 'I':['K','L','G','F'],'J':['M','H'], 'K':['N','I','H'], 'L':['N','S','I'], 'M':['O','J'],
                 'N':['Q','O','K','L'],'O':['P','R','M','N'], 'P':['T','O'], 'Q':['S','R','N'], 'R':['T','Q','O'],'S':['L','Q'], 'T':['P','R']
                 }

        def DFS(graph, visited, vertice):
            if vertice not in visited:
                dfsResult.append (vertice)
                visited.add(vertice)
                for neighbour in graph[vertice]:
                    DFS(graph, visited, neighbour)
        DFS(graph, visited,'A')
        return dfsResult
dfsResult=RunDfs('T')
print('path with DFS :',dfsResult)
