#using 3 dictionaries to store the possible questions and answers

level_1 = {
    "question1": {
        "question" : "How can we create a comment in Python?",
        "answers": {
            "correct": "Comments starts with a '#' ",
            "incorrect1": "Comments use single quotation marks",
            "incorrect2": "Comments start with a '!' ",
            "incorrect3": "Comments start with a '?' ",
        }
    },
    "question2": {
        "question" : "In Python, what are the data types in the category Sequence Types? ",
        "answers": {
            "correct": "list, tuple, range",
            "incorrect1": "list, tuple, boolean",
            "incorrect2": "tuple, boolean, dict",
            "incorrect3": "dict, tuple, list",
        }
    },
    "question3": {
        "question" : "What is the output of print(\"Hello world!\"[2:5]) ",
        "answers": {
            "correct": "llo",
            "incorrect1": "ello ",
            "incorrect2": "lo w",
            "incorrect3": "ell",
        }
    },
    "question4": {
        "question" : "What is the output of print(\"Hello, World!\".upper())",
        "answers": {
            "correct": "HELLO, WORLD!",
            "incorrect1": "HELLO WORLD!",
            "incorrect2": "hello, world!",
            "incorrect3": "Syntax Error",
        }
    },
    "question5": {
        "question" : "Which expression returns a boolean answer of True?",
        "answers": {
            "correct": "print( 10 > 9 )",
            "incorrect1": "print( 10 < 9 )",
            "incorrect2": "print( 10 != 9 )",
            "incorrect3": "print( 10 = 9 )",
        }
    },
    "question6": {
        "question" : "Which of the following is not an arithmetic operator?",
        "answers": {
            "correct": "+=",
            "incorrect1": "**",
            "incorrect2": "//",
            "incorrect3": "%",
        }
    },
    "question7": {
        "question" : "Which of the following built in methods adds an element at the end of the list?",
        "answers": {
            "correct": "append()",
            "incorrect1": "add()",
            "incorrect2": "pop()",
            "incorrect3": "sort()",
        }
    },
    "question8": {
        "question" : "What are the two tuple methods built into Python",
        "answers": {
            "correct": "count(), index()",
            "incorrect1": "count(), extend()",
            "incorrect2": "extend(), index()",
            "incorrect3": "index(), append()",
        }
    },
    "question9": {
        "question" : "Which data set is used to store data in key:value pairs?",
        "answers": {
            "correct": "dict",
            "incorrect1": "list",
            "incorrect2": "tuple",
            "incorrect3": "booleans",
        }
    },
    "question10": {
        "question" : "Which data set(s) uses round (brackets)? ",
        "answers": {
            "correct": "tuple",
            "incorrect1": "list",
            "incorrect2": "list and tuple",
            "incorrect3": "tuples and dict",
        }
    },
}  

#level 2 questions
level_2 = {
    "question11": {
        "question" : "Which of the following is NOT a built in method for Python Sets",
        "answers": {
            "correct": "isthisjoint()",
            "incorrect1": "issubset()",
            "incorrect2": "issuperset()",
            "incorrect3": "pop()",
        }
    },
    "question12": {
        "question" : "How can you make a copy of a Python Dictionary labelled 'thisdict'?",
        "answers": {
            "correct": "mydict = dict(thisdict)",
            "incorrect1": "mydict = copy(thisdict)",
            "incorrect2": "mydict = copy(\"thisdict\")",
            "incorrect3": "mydict = thisdict.dict()",
        }
    },
    "question13": {
        "question" : "Which built-in method for dictionaries is used to remove the element with a specified key?",
        "answers": {
            "correct": "pop()",
            "incorrect1": "remove()",
            "incorrect2": "del()",
            "incorrect3": "clear()",
        }
    },
    "question14": {
        "question" : "Create a lambda function that takes one parameter and returns it.",
        "answers": {
            "correct": "x = lambda a : a ",
            "incorrect1": "x = lambda a : b",
            "incorrect2": "x: lambda a = b",
            "incorrect3": "x = lambda a : A",
        }
    },
    "question15": {
        "question" : "Which of the following is generally NOT true regarding Python Scopes",
        "answers": {
            "correct": "A local variable can be access from a global scope",
            "incorrect1": "A global variable can be access from a global scope",
            "incorrect2": "A global variable can be access from a local scope",
            "incorrect3": "A local variable can be access from a local scope",
        }
    },
    "question16": {
        "question" : """Finish off the following code to create and write a file:
        with open(\"log-entry-1\", \"a\") as myfile: """,
        "answers": {
            "correct": "myfile.write(\"Today was a good day.\")",
            "incorrect1": "myfile.overwrite(\"Today was a good day.\")",
            "incorrect2": "myfile.append(\"Today was a good day.\")",
            "incorrect3": "myfile.read(\"Today was a good day.\")",
        }
    },
    "question17": {
        "question" : "As a Python developer, how can you throw an exception if a condition occurs?",
        "answers": {
            "correct": "raise Exception ...",
            "incorrect1": "throw Exception ...",
            "incorrect2": "try Exception ...",
            "incorrect3": "except Exception ...",
        }
    },
    "question18": {
        "question" : "A while loop in Python is used for what type of iteration?",
        "answers": {
            "correct": "indefinite",
            "incorrect1": "indiscriminate",
            "incorrect2": "definite",
            "incorrect3": "indeterminate",
        }
    },
    "question19": {
        "question" : """What is the result of: 
        print(ord('foo'))
        """,
        "answers": {
            "correct": "It raises an exception",
            "incorrect1": "101",
            "incorrect2": "311",
            "incorrect3": "102 101 101",
        }
    },
    "question20": {
        "question" : """Given the file dog_breeds.txt, 
        which of the following is the correct way to open the file for reading as a text file?""",
        "answers": {
            "correct": "open('dog_breeds.txt', 'r')",
            "incorrect1": "open('dog_breeds.txt', 'w')",
            "incorrect2": "open('dog_breeds.txt', 'rb')",
            "incorrect3": "open('dog_breeds.txt', 'wb')",
        }
    },
}


#level 3 questions
level_3 = {
    "question21": {
        "question" : """What is the output of the following code snippet?
        d = {'foo': 1, 'bar': 2, 'baz': 3}
        while d:
            print(d.popitem())
        print('Done.')
        """,
        "answers": {
            "correct": """('baz', 3)
        ('bar', 2)
        ('foo', 1)
        Done.
        """,
            "incorrect1": """foo
        bar
        baz""",
            "incorrect2": "The snippet doesn't generate any output",
            "incorrect3": "Done.",
        }
    },
    "question22": {
        "question" : """Given the following:
        s = 'foo'
        t = 'bar'
        print('barf' in 2 * (s + t))

        What is the output of the print() function call?
        """,
        "answers": {
            "correct": "True",
            "incorrect1": "False",
            "incorrect2": "Syntax Error",
            "incorrect3": "ValueError",
        }
    },
    "question23": {
        "question" : """What is the output of the following code snippet?
        d = {'foo': 1, 'bar': 2, 'baz': 3}
        while len(d) > 3:
            print(d.popitem())
        print('Done.')
        """,
        "answers": {
            "correct": "Done.",
            "incorrect1": """foo,
        bar,
        baz""",
            "incorrect2": "The snippet doesn’t generate any output.",
            "incorrect3": """('baz', 3)
        ('bar', 2)
        ('foo', 1)
        Done.
        """,
        }
    },
    "question24": {
        "question" : """What is the slice expression that gives every third character of string s, 
        starting with the last character and proceeding backward to the first?
        """,
        "answers": {
            "correct": "s[::-3]",
            "incorrect1": "slice(-3)",
            "incorrect2": "sli[-3]",
            "incorrect3": "sli[::3]",
        }
    },
    "question25": {
        "question" : "In a Python program, a control structure:",
        "answers": {
            "correct": "Directs the order of execution of the statements in the program",
            "incorrect1": "Defines program-specific data structures",
            "incorrect2": "Dictates what happens before the program starts and after it terminates",
            "incorrect3": "Manages the input and output of control characters",
        }
    },
    "question26": {
        "question" : "Which one of the following if statements will not execute successfully:",
        "answers": {
            "correct": """
        if (1, 2):
        print('foo')""",
            "incorrect1": "if (1, 2): print('foo')",
            "incorrect2": """
        if (1, 2):
            print('foo')""",
            "incorrect3": """
        if (1, 2):
                        
                print('foo')""",
        }
    },
    "question27": {
        "question" : "What signifies the end of a statement block or suite in Python?",
        "answers": {
            "correct": "A line that is indented less than the previous line",
            "incorrect1": "end",
            "incorrect2": "}",
            "incorrect3": "A comment",
        }
    },
    "question28": {
        "question" : """
        if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
            print(1)
            print(2)
            if 'a' in 'qux':
                print(3)
        print(4)
        """,
        "answers": {
            "correct": """
        1
        2
        4
        """,
            "incorrect1": "4",
            "incorrect2": "It doesn't generate any output",
            "incorrect3": """
        1
        2
        3
        4
        """,
        }
    },
    "question29": {
        "question" : """The following if/elif/else statement will raise what error?
        d = {'a': 0, 'b': 1, 'c': 0}
        if d['a'] > 0:
            print('ok')
        elif d['b'] > 0:
            print('ok')
        elif d['c'] > 0:
            print('ok')
        elif d['d'] > 0:
            print('ok')
        else:
            print('not ok')
        """,
        "answers": {
            "correct": "It will not raise an error",
            "incorrect1": "KeyError",
            "incorrect2": "ValueError",
            "incorrect3": "Syntax Error",
        }
    },
    "question30": {
        "question" : "Which of the following are valid if/else statements in Python, assuming x and y are defined appropriately:",
        "answers": {
            "correct": """
            if x < y: print('foo')
            elif y < x: print('bar')
            else: print('baz')
            """,
            "incorrect1": "if x < y: if x > 10: print('foo')",
            "incorrect2": "if x < y: print('foo') else: print('bar')",
            "incorrect3": "if x > y: print('foo'); print('bar'); print('baz')",
        }
    },
}