import nfa_dfa
import tabulate


def main():
    tt = nfa_dfa.tt_from_input()
    print(tt)
    dfa = nfa_dfa.nfa_dfa(tt)
    print(tabulate.tabulate(dfa[1:], headers=dfa[0]))


if __name__ == "__main__":
    main()
