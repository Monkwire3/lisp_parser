def tokenize(program):
    tokens = []

    lastTokenIndex = -1
    for i, char in enumerate(program):
        if char in ["(", ")", " "]:
            if (i - lastTokenIndex) > 1:
                tokens.append(program[lastTokenIndex + 1:i])
            if char != " ":
                tokens.append(program[i])
            lastTokenIndex = i


    return tokens 


def getArray(tokens):
    array = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "(":
            j = len(tokens) - 1
            while tokens[j] != ")":
                j -= 1
            
            array.append(getArray(tokens[i + 1:j]))
            i = j + 1
        else:
            try:
                array.append(int(tokens[i]))
            except ValueError:
                array.append(tokens[i])
            i += 1
    
    return array




def lispParser(lisp): 
    tokens = tokenize(lisp)
    return getArray(tokens)[0]


def testFunction(function, testCases):
    print(f"\n====={function.__name__}=====")

    testCasesPassed = 0
    totalTestCases = len(testCases)

    for i, testCase in enumerate(testCases):
        res = function(testCase[0])
        passed = res == testCase[1]
        if passed:
            testCasesPassed += 1
        else:
            print(f"{function.__name__} testcase {i + 1} failed.")
            print(f"Got: {res}")
            print(f"Expected: {testCase[1]}")
    print(f"{testCasesPassed}/{totalTestCases} {function.__name__} testcases passed.")
    if testCasesPassed == totalTestCases:
        print(f"ALL {function.__name__} TESTCASES PASSED.")
        return True
    return False
        

def main():
    lispParserTestCases = [
        ["(first (list 1 (+ 2 3) 9))", ["first", ["list", 1, ["+", 2, 3], 9]]],
        ["(reduce #'- (reverse (list 1 2 3)))", ['reduce', "#'-", ['reverse', ['list', 1, 2, 3]]]],
        ["(mapcar #' string-downcase (list 'Hello' 'world!'))", ['mapcar', "#'", 'string-downcase', ['list', "'Hello'", "'world!'"]]]
    ]

    tokenizeTestCases = [
        ["(first (list 1 (+ 2 3) 9))" , ["(",  "first", "(", "list", "1", "(", "+", "2", "3", ")", "9", ")", ")"]],
        ["(list 1 4 5 (reverse (list 3 2 1)))", ["(", "list", "1", "4", "5", "(", "reverse", "(", "list", "3", "2", "1", ")", ")", ")"]],
    ]

    allTests = [[lispParser, lispParserTestCases], [tokenize, tokenizeTestCases]]
    testsPassed = 0

    for test in allTests:
        if testFunction(test[0], test[1]):
            testsPassed += 1
    
    if testsPassed == len(allTests):
        print("\nALL TESTS PASSING")
    else:
        print(f"\n{testsPassed}/{len(allTests)} function test suites passing.")





if __name__ == "__main__":
    main()