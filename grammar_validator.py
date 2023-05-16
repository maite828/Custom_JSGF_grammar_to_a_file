import sys
from jsgf import Grammar, Literal, NamedRuleRef, PublicRule, Rule, AlternativeSet, Sequence, OptionalGrouping
from jsgf.parser import parse_grammar_string


def save_grammar(filename):
    """
    Saves a custom JSGF grammar to a file.
    """
    grammar = Grammar("music_play", case_sensitive=False)
    grammar.add_rules(
        PublicRule(name="command", expansion=Sequence(
            OptionalGrouping(Literal("can you")), AlternativeSet(
                Sequence(NamedRuleRef("action"), OptionalGrouping(NamedRuleRef("item")), OptionalGrouping(
                    NamedRuleRef("oneormoreitem"))),
                Sequence(Literal("play me"), NamedRuleRef("album"), OptionalGrouping(Literal("by")), NamedRuleRef(
                    "artist")),
                Sequence(Literal("put"), OptionalGrouping(NamedRuleRef("item")), OptionalGrouping(Literal("on"))))
        )),
        Rule(name="action", visible=True, expansion=AlternativeSet(
            Literal("play"),
            Literal("put on"),
            Literal("i want to listen"),
            Literal("put"),
            Literal("play me")
        )),
        Rule(name="oneormoreitem", visible=True, expansion=AlternativeSet(
            NamedRuleRef("item"),
            Literal("and"),
            Literal("with")
        )),
        Rule(name="item", visible=True, expansion=AlternativeSet(
            NamedRuleRef("artist"),
            NamedRuleRef("song"),
            NamedRuleRef("album"),
            NamedRuleRef("genre")
        )),
        Rule(name="artist", visible=True, expansion=AlternativeSet(
            Literal("the beatles"),
            Literal("radiohead"),
            Literal("lady gaga"),
            Literal("pink floyd")
        )),
        Rule(name="song", visible=True, expansion=AlternativeSet(
            Literal("comfortably numb"),
            Literal("paranoid android"),
            Literal("let it be"),
            Literal("hey jude")
        )),
        Rule(name="album", visible=True, expansion=Literal("ummagumma"), case_sensitive=False),
        Rule(name="genre", visible=True, expansion=Literal("jazz"), case_sensitive=False)
    )
    with open(filename, 'w') as file:
        file.write("#JSGF V1.0 utf-8 en;\n\n")
        file.write(grammar.serialize())
    print(f"Grammar saved to {filename}")



def grammar_read(grammar_file):
    """
    Reads a JSGF grammar file and parses it using jsgf.parse_grammar_string.
    """
    with open(grammar_file, "r") as file:
        grammar_string = file.read()

    grammar = parse_grammar_string(grammar_string)

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
    save_grammar(sys.argv[1])
    read_grammar = grammar_read(sys.argv[1])
    parse_command(read_grammar, sys.argv[2])
else:
    print("Please provide a command to match.")
