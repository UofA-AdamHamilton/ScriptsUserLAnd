with open('oedict.sql') as f:
    lines = f.readlines()

import re
import ast  # To safely evaluate the string as a Python literal
import matplotlib.pyplot as plt

# Recognized part-of-speech markers
POS_PATTERN = r'(?:n\.|adj\.|v\.|adv\.|prep\.|conj\.|pron\.|int\.|det\.|suffix|abbr\.|symb\.|comb\.|predic\.|contr\.|Colloq\.|attrib\.|sing\.|var\.|see|prefix|Abbr\.|past of| past part\.|pl\.)'

def take_brackets(entry_str):
    #returns the proprtion of a string between teh first instance of a ( 
    # bracket and the last occurence of a ) bracket (including the brackets themselves)
    l_bracket = entry_str.find('(')
    r_bracket = entry_str.rfind(')')
    return entry_str[l_bracket: r_bracket +1]

def extract_words_only(text):
    """
    Extracts and returns a list of words from the input text.
    Words are sequences of alphabetic characters only.
    Removes numbers, punctuation, brackets, and special characters.
    """
    # Match sequences of alphabetic characters (ignores punctuation, digits, etc.)
    return re.findall(r'\b[a-zA-Z]+\b', text)

def parse_string_entry(entry_str):
    if "INSERT INTO" in entry_str:
        # this seems to be a feature of the .sql file and we ignore lines like this
        return

    entry_str = take_brackets(entry_str)
    try:
        # Convert the string to a tuple
        entry = ast.literal_eval(entry_str)
    except Exception as e:
        raise ValueError(f"Failed to parse entry string: {e}")

    if not isinstance(entry, tuple) or len(entry) != 4:
        raise ValueError("Entry must be a tuple of 4 elements")

    index, letter, part1, part2 = entry
    if '\nUsage' in part1:
        # this represents an exception, where the line is adding more context to the previous entry
        return 
    if part1[-1] in {'1','2','3','4','5','6','7','8','9','0'}:
        # this is another exception and is a continuation of the previous line. 
        return

    # Combine word + definition
    combined = (part1 + part2).replace('\x7f', '').strip()

    # Find part-of-speech marker
    pos_match = re.search(POS_PATTERN, combined)
    if not pos_match:
        #raise ValueError(f"Part of speech not found in entry: {entry}")
        word = part1 
        part_of_speech = ''
        def_body = part2
    else:
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
    definitions = [extract_words_only(d) for d in definitions]

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
#parsed = parse_string_entry(entry_str)

import pprint
#pprint.pprint(parsed)
 
n=28
index_list = []
for i in range(n,n+36750):
    dict_def = parse_string_entry(lines[i])
    if dict_def is not None:
        if len(dict_def['definitions']) > 1:
            print(dict_def)
            print(' ')

