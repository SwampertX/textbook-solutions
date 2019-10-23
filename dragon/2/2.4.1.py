# stmt switches on the current lookahead, a global variable
# use a match function to move lookahead forward

def part_A():
    symbols = input().split('')
    switch = {'+': plus, '-': minus, 'a': a}
    index = 0
    lookahead = symbols[0]
    def next_lookahead():
        global lookahead
        global index
        index = index + 1
        lookahead = symbols[index]
    def S():
        switch[lookahead]()
    def match(terminal):
        if lookahead == terminal:
            next_lookahead()
    def plus():
        match('+')
        S()
        S()
    def minus():
        match('-')
        S()
        S()
    def a():
        match('a')

