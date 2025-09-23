with open('oedict.sql') as f:
    lines = f.readlines()
for i in range(50):
    print(lines[i])
    print(i)

import re
import ast  # To safely evaluate the string as a Python literal

# Recognized part-of-speech markers
POS_PATTERN = r'\b(?:n\.|adj\.|v\.|adv\.|prep\.|conj\.|pron\.|int\.|det\.)\b'

def parse_string_entry(entry_str):
    try:
        # Convert the string to a tuple
        entry = ast.literal_eval(entry_str)
    except Exception as e:
        raise ValueError(f"Failed to parse entry string: {e}")

    if not isinstance(entry, tuple) or len(entry) != 4:
        raise ValueError("Entry must be a tuple of 4 elements")

    index, letter, part1, part2 = entry

    # Combine word + definition
    combined = (part1 + part2).replace('\x7f', '').strip()

    # Find part-of-speech marker
    pos_match = re.search(POS_PATTERN, combined)
    if not pos_match:
        raise ValueError(f"Part of speech not found in entry: {entry}")

    pos_start = pos_match.start()
    pos_end = pos_match.end()

    word = combined[:pos_start].strip()
    part_of_speech = combined[pos_start:pos_end]
    def_body = combined[pos_end:].strip()

    # Extract definitions (1 ..., 2 ..., etc.)
    definitions = re.split(r'\b\d+\s+', def_body)
    definitions = [d.strip() for d in definitions if d.strip()]

    # Detect any trailing additional info (heuristically)
    additional_info = ""
    if definitions:
        last_def = definitions[-1]
        if re.search(r'\b(?:adj\.|adv\.|n\.|v\.)\b.*\[.*\]', last_def):
            additional_info = last_def
            definitions = definitions[:-1]

    return {
        'index': index,
        'letter': letter,
        'word': word,
        'part_of_speech': part_of_speech,
        'definitions': definitions,
        'additional_info': additional_info
    }

# Example usage
entry_str = "(22, 'a', '\\nAbdomen', ' n. 1 the belly, including the stomach, bowels, etc. 2 the hinder part of an insect etc. \\x7f abdominal adj. [latin]')"
parsed = parse_string_entry(entry_str)

import pprint
pprint.pprint(parsed)


 
n=50
for i in range(n,n+9):
    print(parse_entry(lines[i]))
