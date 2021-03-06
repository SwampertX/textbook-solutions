import string

# Task: design a function that takes in a NFA
# as a graph and returns the corresponding DFA
# input: A graph, nfa
# output: A graph, dfa

# we represent all graph as a adjacency matrix.
# nfa graph - ns * (l + 1) matrix
# dfa graph - __unknown__ * l matrix

# nfa_tt is a list of hashmaps from letter + epsilon to state number
# discipline: epsilon must exist and represented by "epsilon"
# dfa_tt is a list of hashmaps from letter to state number
# we keep a hashmap of number to set of numbers
def nfa_dfa(nfa_tt):
    # maintain a queue of dfa states
    # while the queue is not empty
    #   pop dfa state one out
    #   transition_row = []
    #   for each letter in set of letters:
    #       moved = move(state, letter)
    #       final = e-closure(moved)
    #       add final into dfa states if final not in dfa states
    letters = list(nfa_tt[0].keys())
    letters.remove("epsilon")

    nfa_states_to_dfa_state = {}  # tuple of num to num
    dfa_state_to_nfa_states = []  # list of tuples
    dfa_tt = []  # list of hashmap of letter to num
    not_explored_dfa_states = []  # list of num

    # takes in a list of n
    def dfa_state_is_new(list_of_num):
        tuple_of_num = tuple(sorted(list_of_num))
        if any(nfa_states == tuple_of_num for nfa_states in dfa_state_to_nfa_states):
            # print("seen {} before, moving on".format(tuple_of_num))
            return False
        # print("{} is a new state".format(tuple_of_num))
        nfa_states_to_dfa_state[tuple_of_num] = len(dfa_state_to_nfa_states)
        dfa_state_to_nfa_states.append(tuple_of_num)
        not_explored_dfa_states.append(nfa_states_to_dfa_state[tuple_of_num])
        return True

    # we kick start with the first dfa state
    dfa_starting_state = epsilon_closure(nfa_tt, [0])
    dfa_state_is_new(dfa_starting_state)

    while not_explored_dfa_states:
        # print("current queue:", not_explored_dfa_states)
        # print("current dtrans:", dfa_tt)
        curr_dfa_state = not_explored_dfa_states.pop()
        curr_nfa_states = dfa_state_to_nfa_states[curr_dfa_state]
        dfa_tt_row = {}  # letter to num
        for letter in letters:
            next_nfa_states = move_then_epsilon_closure(nfa_tt, curr_nfa_states, letter)
            dfa_state_is_new(next_nfa_states)
            next_dfa_state = nfa_states_to_dfa_state[tuple(sorted(next_nfa_states))]
            dfa_tt_row[letter] = next_dfa_state
        dfa_tt.append(dfa_tt_row)
    return tt_to_lol((dfa_tt, dfa_state_to_nfa_states))


####### Below are helper functions ########

# output: set of integers
def move(nfa_tt, states, letter):
    list_of_tuples = [nfa_tt[i][letter] for i in states if nfa_tt[i][letter]]
    list_of_states = [state for tup in list_of_tuples for state in tup]
    return set(list_of_states)


# output: set of integers
def epsilon_closure(nfa_tt, states):
    # dfs through tt using only epsilon edges
    # keep track of visited states and return it
    visited = set()  # set of number

    def dfs(state):
        if state in visited:
            return
        visited.add(state)
        for neighbour in nfa_tt[state]["epsilon"]:
            dfs(neighbour)

    for state in states:
        dfs(state)
    return visited


def move_then_epsilon_closure(nfa_tt, states, letter):
    moved = move(nfa_tt, states, letter)
    ec = epsilon_closure(nfa_tt, moved)
    # print("moving {} along {} edge resulted in {}".format(states, letter, moved))
    # print("taking epsilon closure of {}, we have {}".format(moved, ec))
    return ec


def tt_from_input():
    rows = int(input("Number of rows (states, including zero): "))
    cols = int(input("Number of cols (letters, including epsilon): "))
    letters = []
    for i in range(cols - 1):
        letters.append(input("{}th letter : ".format(i + 1)))
    print("\nFrom now on, please input space separated values, or just enter")
    tt = []
    for state in range(rows):
        tt_row = {}
        for j in range(cols):
            letter = letters[j] if j < (cols - 1) else "epsilon"
            prompt = "states from {} via {}: ".format(state, letter)
            tt_row[letter] = set(
                int(i) for i in input(prompt).strip().split(" ") if i != ""
            )
            tt_row[letter] = tuple(sorted(tt_row[letter]))
        tt.append(tt_row)
    return tt


# structure of tt:
# a tuple of 2 lists
# first list: d_state number of dicts from letter to a d_state
# second list: d_state number of tuples, representing the d_state
#
# output structure:
# list of lists:
# cols: number of letters + 1
# rows: d_state + 1
# | nfa_states | | a | b |
# | {1,2,3}    |A| B | C |
def tt_to_lol(tt):
    num_of_letters_in_lang = len(tt[0][0])
    num_cols = num_of_letters_in_lang + 1
    letters_in_lang = list(tt[0][0].keys())

    num_of_d_states = len(tt[0])
    num_rows = num_of_d_states + 1

    lol = []
    lol.append(["nfa states", ""] + letters_in_lang)  # pad for header
    for i in range(num_rows - 1):  # except header
        lol.append(
            [tt[1][i], string.ascii_uppercase[i]]
            + [string.ascii_uppercase[tt[0][i][letter]] for letter in letters_in_lang],
        )
    return lol
