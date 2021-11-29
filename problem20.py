from PyFun.commons import pipe, partial

def faculty(n):
    if n == 1:
        return 1
    return n * faculty(n-1)

numberToString = str;
stringToCharList = list;
charListToNumberList = partial(map,int);
addNumbersInList = partial(reduce, lambda x,y: x+y);

# number -> number
sumDigitsForFaculty = pipe(
    faculty,
    numberToString,
    stringToCharList,
    charListToNumberList,
    addNumbersInList
    #str,
    #list,
    #partial(map,int),
    #partial(reduce, lambda x,y: x+y)
)

print sumDigitsForFaculty(100)