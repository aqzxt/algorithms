"""
Created on Tue Apr 24 20:30:29 2018 ----------- @author: mxhfield
"""

def black_shapes(A):
    def dfs(B, i, k, visited, left, right):
        if i < 0 or i > left -1: return
        if k < 0 or k > right -1: return
        if B[i][k] == 'O' or visited[i][k]: return
        
        visited[i][k] = True
        dfs(B, i +1, k, visited, left, right)
        dfs(B, i -1, k, visited, left, right)
        dfs(B, i, k +1, visited, left, right)
        dfs(B, i, k -1, visited, left, right)
    
    answer = 0
    visited = [ [False for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for k in range(len(A[0])):
            if A[i][k] == 'X' and visited[i][k] == False:
                dfs(A, i, k, visited, len(A), len(A[0]))
                # visited[i][j] = True
                answer += 1
    return answer


print(black_shapes(['OOOXOOO',
                    'OOXXOXO',
                    'OXOOOXO']))