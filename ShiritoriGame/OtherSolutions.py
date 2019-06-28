class Shiritori:
	words=[]
	game_over=False
	
	def play(self,word):
		if(isinstance(word,str)):
			if(not self.words):
				self.words.append(word)
				return self.words
			lastword=self.words[len(self.words)-1]
			if(lastword[len(lastword)-1]==word[0]):
				if(word not in self.words):
					self.words.append(word)
					return self.words
		self.game_over=True
		return "game over"
		
	def restart(self):
		self.words=[]
		self.game_over=False
		return "game restarted"

###################################################
  
class Shiritori:
	words = []
	
	def __init__(self, word = ''):
		self.game_over = False
		self.game_restart = self.restart()
		
	def play(self, word):
		w = self.words
		if word in w:
			self.game_over = True
			return 'game over'
		elif w == []:
			w.append(word)
		else:
			if word[0] != w[-1][-1]:
				self.game_over = True
				return 'game over'
			else:
				w.append(word)
		self.words = w
		return self.words
		
	def restart(self):
		self.words = []
		self.game_over = False
		return 'game restarted'
  
###################################################

class Shiritori:
	def __init__(self,words=[],game_over=False):
		self.words = words
		self.game_over = game_over
	
	def play(self,word):
		if not self.words:
			self.words.append(word)
		else:
			if word[0] == self.words[-1][-1] and word not in self.words:
				self.words.append(word)
			else:
				self.game_over = True
				return 'game over'
		return self.words
	
	def restart(self):
		self.game_over = False
		self.words = []
		return 'game restarted'
  
###################################################

class Shiritori:
  def __init__(self, words=[], game_over=False):
    self.words=words
    self.game_over=game_over
  def play(self, word):
    if not self.words or (word not in self.words and word[0]==self.words[-1][-1]):
      self.words.append(word)
      return self.words
    else:
      self.game_over=True
      return 'game over'
  def restart(self):
    self.words = []
    self.game_over=False
    return 'game restarted'
  
###################################################

class Shiritori:

    def __init__(self, words=[], game_over=False):
        self.words = words
        self.game_over = game_over
        
    def play(self, word):
        if not self.words:
            self.words.append(word)
            return self.words
        if word not in self.words and self.words[-1][-1] == word[0]:
            self.words.append(word)
            return self.words
        self.game_over = True
        return 'game over'
    
    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'
