def bonacci(n, k):
    arr = [0]*(n-1) + [1]
    for _ in range(k):
        arr.append(sum(arr[-n:]))
    return arr[k-1]

###################################################
  
def bonacci(N,k):
	if k < N:
		return [0 for i in range (k)]
	sequence = [0 for i in range (N-1)]+[1]
	for i in range (k-N):
		sequence.append(sum(sequence[-N:]))
	return sequence[-1]
  
###################################################

def bonacci(N, k):
  f = [0]*(N-1)+[1]
  for i in range(k-1):
    f.append(sum(f[-N:]))
  return f[k-1]
  
###################################################

def bonacci(N, k):
    if N > k:
        return 0
    l = [0 for x in range(N - 1)] + [1]
    for x in range(N, k):
        l.append(sum(l[x - N: x]))
    return l[-1]
  
###################################################

def bonacci(N, k):
	if k < N:
		return 0
	lst = [0]*(N-1) + [1]
	for i in range(k-N):
		lst.append(sum(lst[-N:]))
	return lst[-1]
