import jieba
import jieba.posseg as psg

nounWords = {}
verbWords = {}
adjWords = {}
alphabeticWords = {}
exclamationWords = {}

def separaNcount(filename):
    global nounWords
    global verbWords
    global adjWords
    global alphabeticWords
    global exclamationWords
    with open("./result/text.txt") as textFile:
        for line in textFile:
            for word in psg.cut(line):
                if word.flag.startswith("n"):
                    if word.word in nounWords:
                        nounWords[word.word] += 1
                    else:
                        nounWords[word.word] = 1
                elif word.flag.startswith("v"):
                    if word.word in verbWords:
                        verbWords[word.word] += 1
                    else:
                        verbWords[word.word] = 1
                elif word.flag.startswith("a"):
                    if word.word in adjWords:
                        adjWords[word.word] += 1
                    else:
                        adjWords[word.word] = 1
                elif word.flag.startswith("eng"):
                    if word.word in alphabeticWords:
                        alphabeticWords[word.word] += 1
                    else:
                        alphabeticWords[word.word] = 1
                elif word.flag.startswith("o"):
                    if word.word in exclamationWords:
                        exclamationWords[word.word] += 1
                    else:
                        exclamationWords[word.word] = 1

    nounWords = sorted(nounWords.items(), key = lambda d:d[1], reverse=True)
    verbWords = sorted(verbWords.items(), key = lambda d:d[1], reverse=True)
    adjWords = sorted(adjWords.items(), key = lambda d:d[1], reverse=True)
    alphabeticWords = sorted(alphabeticWords.items(), key = lambda d:d[1], reverse=True)
    exclamationWords  = sorted(exclamationWords.items(), key = lambda d:d[1], reverse=True)
                

def writeResult():
    global nounWords
    global verbWords
    global adjWords
    global alphabeticWords
    global exclamationWords
    with open("./result/nounWords.txt", "w") as fout:
        for item in nounWords:
            fout.write(item[0] + ":" + str(item[1]) + "\n")
    with open("./result/verbWords.txt", "w") as fout:
        for item in verbWords:
            fout.write(item[0] + ":" + str(item[1]) + "\n")
    with open("./result/adjWords.txt", "w") as fout:
        for item in adjWords:
            fout.write(item[0] + ":" + str(item[1]) + "\n")
    with open("./result/alphabeticWords.txt", "w") as fout:
        for item in alphabeticWords:
            fout.write(item[0] + ":" + str(item[1]) + "\n")
    with open("./result/exclamationWords.txt", "w") as fout:
        for item in exclamationWords:
            fout.write(item[0] + ":" + str(item[1]) + "\n")

if __name__ == "__main__":
    separaNcount("./result/text.txt")
    writeResult()

