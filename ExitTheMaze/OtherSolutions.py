def can_exit(lst):
	m = len(lst[0])
	n = len(lst)
	alreadyPassed = [[0 for i in range(m)] for j in range(n)]
	
	def check(x,y,dx,dy):
		if x+dx < n and x+dx >= 0 and y+dy < m and y+dy >= 0:
			if not alreadyPassed[x+dx][y+dy]:
				return lst[x+dx][y+dy] == 0
		return False
	
	def propagate(x, y):
		alreadyPassed[x][y] = 1
		if check(x,y,1,0):
			propagate(x+1,y)
		if check(x,y,-1,0):
			propagate(x-1,y)
		if check(x,y,0,1):
			propagate(x,y+1)
		if check(x,y,0,-1):
			propagate(x,y-1)
	
	propagate(0,0)
	return alreadyPassed[n-1][m-1]

###################################################
  
def can_exit(lst):
	start = [0,0]
	end = [len(lst)-1, len(lst[0])-1]
	marked = [start]
	marked = fillmarked(lst,marked)
	for i in lst:
		print(i)
	print(marked)
	return end in marked
	
def fillmarked(lst, marked):
	temp = marked
	for i in marked:
		marked = leftright(lst,i,marked)
		marked = updown(lst,i,marked)
	if len(marked) == len(temp):
		return marked
	else:
		return fillmarked(lst,marked)
		
def leftright(lst,place,marked):
	left = place[1]-1
	right = place[1]+1
	if place[1]>0 and lst[place[0]][left]==0 and [place[0],left] not in marked:
		marked.append([place[0],left])
	if place[1]<len(lst[0])-1 and lst[place[0]][right]==0 and [place[0],right] not in marked:
		marked.append([place[0],right])
	return marked

def updown(lst,place,marked):
	up = place[0]-1
	down = place[0]+1
	if place[0]>0 and lst[up][place[1]]==0 and [up,place[1]] not in marked:
		marked.append([up,place[1]])
	if place[0]<len(lst)-1 and lst[down][place[1]]==0 and [down,place[1]] not in marked:
		marked.append([down,place[1]])
	return marked
  
###################################################

def can_exit(cave):
  height, width = len(cave), len(cave[0])
  start = [[0, i] for i in range(len(cave)) if cave[i][0] == 0]

  def neighbors(c):
    x, y = c
    n = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
    n = [[x, y] for x,y in n if x in range(width) and y in range(height) and cave[y][x] == 0]
    return n
      
  for first in start:
    current=[first]
    next = []
    seen = []
    while current:
      for c in current:
        for n in neighbors(c):
          if n not in seen and n not in next:
            next.append(n)
            if n[0] == width-1 and n[1] == height-1:
              return True
        seen.append(c)
      current, next = next, []
  return False
  
###################################################

def can_exit(lst):
    lst[0][0] = 2
    m = len(lst)
    n = len(lst[0])
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 0 and (((i + 1) > -1 and lst[i-1][j] ==2) or ((i + 1) < m and lst[i+1][j] ==2) or ((j+1) < n and lst[i][j+1]==2) or ((j-1) > -1 and lst[i][j-1]==2)):
                    lst[i][j] = 2
    if lst[m-1][n-1] ==2:
         return True
    else:
        return False
  
###################################################

def can_exit(lst, y=0, x=0, visited=set()):
    if y==len(lst)-1 and x == len(lst[0])-1:
        return True
    adjacents = {(y-1, x), (y+1, x), (y, x-1), (y, x+1)}
    adjacents = {(y_,x_) for y_,x_ in adjacents if 0<=y_<len(lst) and 0<=x_<len(lst[0]) and not lst[y_][x_]}
    return any(can_exit(lst, y_, x_, visited |{(y,x)}) for y_,x_ in adjacents if (y_,x_) not in visited)
