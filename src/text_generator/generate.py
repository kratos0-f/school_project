import numpy as np
import train
text = train.words[0]
textLength = train.args.count
song = ''
for i in range(0, textLength):
    song += text
    song += " "
    text = str(np.random.choice(train.dictionary.get(text), 1)[0])

print(song)



