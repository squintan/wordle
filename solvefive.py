from itertools import combinations

def has_unique_letters(word):
    """Checks if all letters in the word are unique."""
    return len(set(word)) == len(word)

def create_bitmask(word):
    """Creates a bitmask for a given word where each letter corresponds to a bit."""
    bitmask = 0
    for char in word:
        bitmask |= (1 << (custom_alphabet.index(char)))  # Set the bit for the letter
    return bitmask

# Custom alphabet (least common to most common letters)
custom_alphabet = 'QXJZVFWBKGPMHDCYTLNUROISEA'

# File paths
input_file = 'words_alpha.txt'
debug_file = 'debug_words_with_letters.txt'
result_file = 'results.txt'

# Read the word list and filter out words with repeated letters
with open(input_file, 'r') as file:
    words = file.read().splitlines()

unique_letter_words = []
for word in words:
    word = word.strip().upper()  # Use upper() to match the custom alphabet case

    # Check if the word has valid length, unique letters, and only contains valid characters
    if len(word) == 5 and has_unique_letters(word) and all(char in custom_alphabet for char in word):
        unique_letter_words.append(word)

# Sort words based on custom alphabet
unique_letter_words_sorted = sorted(unique_letter_words)

# Create a dictionary to store words containing each letter
letter_word_dict = {letter: [] for letter in custom_alphabet}

# Populate the dictionary with words for each letter
for word in unique_letter_words_sorted:
    for letter in word:
        letter_word_dict[letter].append(word)

# Write the dictionary to the debug file
with open(debug_file, 'w') as file:
    for letter in custom_alphabet:
        file.write(f'Words with "{letter}":\n')
        if letter_word_dict[letter]:  # Only write if there are words for that letter
            for word in letter_word_dict[letter]:
                file.write(f'  {word}\n')
        else:
            file.write('  None\n')  # Indicate no words for that letter

# Open results file for writing directly
with open(result_file, 'w') as file:
    results_count = 0
    total_words = len(unique_letter_words_sorted)

    # Initialize progress tracking
    progress_count = 0

    # Check all combinations of 5 words
    for combination in combinations(unique_letter_words_sorted, 5):
        combined_mask = 0
        valid_combination = True

        for word in combination:
            word_mask = create_bitmask(word)  # Calculate the bitmask for the current word
            if combined_mask & word_mask:  # Check for shared letters
                valid_combination = False
                break
            combined_mask |= word_mask  # Combine bitmasks for the current combination

        if valid_combination:
            file.write(f"{', '.join(combination)}\n")
            results_count += 1

        progress_count += 1
        if progress_count % 1000 == 0:  # Display progress every 1000 combinations processed
            print(f'Progress: {progress_count} combinations processed')

    print(f"Total valid combinations found: {results_count}")
    print(f"Results written to {result_file}")
