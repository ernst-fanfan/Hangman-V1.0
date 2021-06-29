from Game import Player

c1 = Player(0, "Ai")
word = "monkey"
mask = []
for i in word:
    mask += "_"
mask[1] = "o"
mask[4] = "e"
c1.brain.isolate(mask)
c1.brain.analyze(mask)

print(word)
print(mask)
print(c1.brain.pick(mask))
