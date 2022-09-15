import argparse
import numpy
import train
text = train.words[0]
textLengh = train.args.count
song = ''
for i in range(0, textLengh):
    song += text
    song += " "
    text = str(numpy.random.choice(train.dictionary.get(text), 1)[0])

print(song)
