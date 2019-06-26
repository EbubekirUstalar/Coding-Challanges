def same_vowel_group(w):
	first = set(w[0]) & set('aeiou')
	return [i for i in w if set(i) & set('aeiou') == first]
  
  
def same_vowel_group(w):
  return [i for i in w if set(j for j in i if j in 'aeiou')==set(j for j in w[0] if j in 'aeiou')]
  
  
def same_vowel_group(w):
  v = sorted(list(set([i for i in w[0] if i in 'aeiou'])))
  return [i for i in w if sorted(list(set([x for x in i if x in 'aeiou']))) == v]
  
  
def same_vowel_group(w):
	vowels = 'aeiou'
	v = set([i for i in w[0] if i in vowels])
	to_delete = []
	for i in range(1,len(w)):
		for letter in w[i]:
			if letter in vowels and letter not in v:
				to_delete.append(i)
				break
	while len(to_delete) > 0:
		del w[to_delete[-1]]
		del to_delete[-1]
	return w
  
  
def same_vowel_group(w):
	result = []
	word_zero = set()
	for char in w[0]:
		if char in 'aeiou':
			word_zero.add(char)
	for word in w:
		vowels = set()
		for char in word:
			if char in 'aeiou':
				vowels.add(char)
		if vowels == word_zero:
			result.append(word)
	return result
