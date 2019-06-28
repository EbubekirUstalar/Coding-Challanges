class Shiritori:
    words = []
    game_over = False

    def play(self, word):
        if (len(word) > 0  and (len(self.words) == 0 or (word not in self.words and word[0] == self.words[-1][-1]))):
            self.words.append(word)
            print(self.words)
        else:
            self.game_over = True
            print("Game Over")

    def restart(self):
        self.words = []
        self.game_over = False
        print("game restarted")


## test case
my_shiritori = Shiritori()

my_shiritori.play("apple")
my_shiritori.play("ear")
my_shiritori.play("rhino")
my_shiritori.play("corn")

print(my_shiritori.words)

my_shiritori.restart()
print(my_shiritori.words)

my_shiritori.play("hostess")
my_shiritori.play("stash")
my_shiritori.play("hostess")

