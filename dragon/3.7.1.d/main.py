import nfa_dfa

def main():
    tt = nfa_dfa.tt_from_input()
    print(tt)
    print(nfa_dfa.nfa_dfa(tt))

if __name__ == "__main__":
    main()
