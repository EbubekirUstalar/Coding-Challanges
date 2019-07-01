def next_number(n):
    s = [int(i) for i in str(n)]

    for i in range(len(s)-1, 0, -1):
        if s[i-1] < s[i]:
            digit = s[i-1]
            while digit not in s[i:]:
                digit += 1
            nearest = s[i:].index(digit) + i
            s[i-1], s[nearest] = s[nearest], s[i-1]
            s[i:] = sorted(s[i:])
            return int(''.join(str(i) for i in s))
    return n

###################################################
  
def next_number(num):
	num = list(str(num))
	k = -1
	for i in range(len(num) - 2, -1, -1):
		if num[i] < num[i + 1]:
			k = i
			break
	if k == -1:
		return int(''.join(num))
	l = k
	for i in range(len(num) - 1, k, -1):
		if num[k] < num[i]:
			l = i
			break
	t = num[k]
	num[k] = num[l]
	num[l] = t
	num = num[:k + 1] + num[k + 1:][::-1]
	return int(''.join(num))
  
###################################################

def next_number(num):
  s=list(str(num))
  i=len(s)-2
  while int(''.join(s))<=num and i>-1:
    if s[i:]==sorted(s[i:],reverse=True):
      i-=1
    else:
      tail=sorted(s[i:])
      s=s[:i] + [tail.pop(tail.index(s[i])+1)] + tail
  return int(''.join(s))
  
###################################################

def next_number(num):
	num = list(str(num))
	k = -1
	for i in range(len(num) - 2, -1, -1):
		if num[i] < num[i + 1]:
			k = i
			break
	if k == -1:
		return int(''.join(num))
	l = k
	for i in range(len(num) - 1, k, -1):
		if num[k] < num[i]:
			l = i
			break
	t = num[k]
	num[k] = num[l]
	num[l] = t
	num = num[:k + 1] + num[k + 1:][::-1]
	return int(''.join(num))
  
###################################################

def next_number(num):
	n = num
	num = list(str(num))
	if sorted(num)[::-1] == num:
		return n
	for i in range(2, len(num) + 1):
		temp = sorted(num[-i:])
		start = ''.join(num[:-i])
		for x in range(len(temp)):
			check = int(start + ''.join([temp[x]] + temp[:x] + temp[x + 1:]))
			if check > n:
				return check
