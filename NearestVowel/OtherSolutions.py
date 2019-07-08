def distance_to_nearest_vowel(txt):
	vowel_pos = [idx for idx, i in enumerate(txt) if i in 'aeiou']
	return [min(abs(v - pos) for v in vowel_pos) for pos in range(len(txt))]
	
###################################################
  
def distance_to_nearest_vowel(txt):
  loc = [0 if i in 'aeiou' else 1 for i in txt]
  x,y = loc.index(0), len(loc)-1-loc[::-1].index(0)
  d_to = [0 if loc[i]==0 else loc[i:].index(0) if i<y else 100 for i in range(len(loc))]
  d_from = []
  for i in range(len(loc)):
    if i<x:
      d_from.append(100)
    elif loc[i]==0:
      d_from.append(0)
      x=i
    else:
      d_from.append(i-x)
  return [min(d_to[i],d_from[i]) for i in range(len(loc))]
  
###################################################

def distance_to_nearest_vowel(txt):
	v = 'aeiou'
	dist = [0] * len(txt)
	for i in range(len(txt)):
		if txt[i] not in v:
			for x in range(len(txt)):
				if i - x >= 0 and txt[i-x] in v:
					dist[i] = x
					break
				elif i + x < len(txt) and txt[i+x] in v:
					dist[i] = x
					break
	return dist
###################################################

def distance_to_nearest_vowel(txt):
	vowels = 'aeiou'
	v_ndxs = [i for i in range(len(txt)) if txt[i] in vowels]
	return [0 if txt[i] in vowels else get_min_dist(v_ndxs,i) for i in range(len(txt))]

def get_min_dist(lst,ndx):
	res = []
	for i in lst:
		res.append(abs(i-ndx))
	return min(res)
  
###################################################

def distance_to_nearest_vowel(txt):
	v = [i for i in range(len(txt)) if txt[i] in 'aeiou']
	return [min([abs(i - k) for k in v]) for i in range(len(txt))]
