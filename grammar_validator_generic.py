import sys
from jsgf.parser import valid_grammar
from jsgf import parse_grammar_string

def grammar_read(grammar_file):
    """
    Reads a JSGF grammar file and parses it using jsgf.parse_grammar_string.
    """
    with open(grammar_file, "r") as file:
        grammar_string = file.read()

    grammar = parse_grammar_string(grammar_string)

    if not valid_grammar(grammar_string):
        raise ValueError("Invalid grammar! Please check your input.")
    else:
        print("Valid Grammar!\n")
        return grammar

def parse_command(grammar, command):
    """
    Parses a command using a JSGF grammar.
    """
    # Print the compiled grammar
    print("Compiled grammar is:\n%s" % grammar.compile())

    matches = grammar.find_matching_rules(command)
    if matches:
        for rule in matches:
            print(f"Matching rule: {rule}\n")
            print("Matched tags:")
            for tag in rule.tags:
                print(tag)
            print()
    else:
        print("No matching rule found")


if len(sys.argv) > 2:
    grammar = grammar_read(sys.argv[1])
    parse_command(grammar, sys.argv[2])
else:
    print("Please provide a command to match")


# =============================================================================
# Requirements
# =============================================================================
# python>=3
# jsgf==1.9.0
