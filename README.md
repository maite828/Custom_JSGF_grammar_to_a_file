# JSGF Grammar Validator

This script allows you to read and validate JSGF (Java Speech Grammar Format) grammar files and parse commands using the grammar to find matching rules.

## Requirements

- Python 3.x
- jsgf 1.9.0

## Usage

1. Install the required dependencies:
pip install jsgf==1.9.0


2. Run the script using the following command:
python grammar_validator.py <grammar_file> <command>


- `<grammar_file>`: The path to the JSGF grammar file.
- `<command>`: The command to parse and match against the grammar rules.

3. The script will perform the following steps:
- It will read the grammar file specified by `<grammar_file>` and parse it using the `jsgf.parse_grammar_string()` function.
- It will check if the grammar is valid using the `jsgf.parser.valid_grammar()` function. If the grammar is invalid, an error will be raised.
- If the grammar is valid, it will compile the parsed grammar and print it.
- Finally, it will attempt to find matching rules in the grammar for the provided `<command>` and display the results.

## Example

Let's demonstrate the usage with an example:

Suppose we have a JSGF grammar file named `grammar_en.jsgf` with the following content:

```plaintext
# JSGF Grammar File

public <command> = (play | stop | pause) (music | radio);
To validate a command against this grammar, run the following command:

Copy code
python grammar_validator.py grammar_en.jsgf "play music"
The script will read the grammar file, parse it, check if it is valid, compile it, and then attempt to find matching rules for the command "play music". It will display the matched rules and any associated tags.
