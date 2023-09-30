import sys
input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int,input().split()))for _ in range(n)] #(그래프 지도는)
chk = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1] #외워서 써주면 빠르다. 
dy = [1, 0, -1, 0]

def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q: # q가 더이상 새 연산을 들어가지 않을때까지
        ey, ex = q.pop()
        for k in range(4): # 상하 좌우에 대해서
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny < n and 0 <=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False :
                    rs +=1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs



cnt = 0
maxv = 0

# 2중 for문일때는 y먼저 돌고 x를 돈다.
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수를 +1
            # BFS > 그림크기를 구해주고
            cnt += 1
            maxv = max(maxv, bfs(j, i))
            # 최댓값 갱신
            
            
print(cnt)
print(maxv)