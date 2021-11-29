from PyFun.commons import pipe, partial

alphabeticalValues = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
    "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
    "X": 24, "Y": 25, "Z": 26
}

def getCharValue(c):
    return alphabeticalValues[c]

# String -> number
getStringValue = pipe(
    list,
    partial(map, getCharValue),
    sum
)

sortAndToValue = pipe(
    sorted,
    partial(map, getStringValue)
)

def solve(data):
    sortedData = sortAndToValue(data)
    result = 0
    for i in range(len(sortedData)):
        val = (i+1) * sortedData[i]
        result = result + val
    return result

smallData = ["MARY","PATRICIA","LINDA","BARBARA","ELIZABETH","JENNIFER","MARIA","SUSAN"]
smallestData = ["MARY","SUSAN","LINDA"]
data = open("files/p022_names.txt", "r").read()
# split at ","
print data