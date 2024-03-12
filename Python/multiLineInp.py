def readMultiLines(stopCharacter="."):
    inp=""
    text=""
    while inp!=stopCharacter:
        text+=inp +"\n"
        inp = input()
    return text.strip()

print(readMultiLines(","))