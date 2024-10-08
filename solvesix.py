from itertools import combinations

def has_unique_letters(word):
    """Checks if all letters in the word are unique."""
    return len(set(word)) == len(word)

def create_bitmask(word):
    """Creates a bitmask for a given word where each letter corresponds to a bit."""
    bitmask = 0
    for char in word:
        bitmask |= (1 << custom_alphabet.index(char))  # Set the bit for the letter
    return bitmask

def backtrack(combination, start_index, used_letters):
    """Recursively finds valid combinations of words without shared letters."""
    if len(combination) == 5:
        valid_combinations.append(combination[:])
        return

    for i in range(start_index, len(unique_letter_words_sorted)):
        word = unique_letter_words_sorted[i]
        word_mask = create_bitmask(word)

        # Check if the current word shares letters with the used letters
        if used_letters & word_mask == 0:  # No overlap
            combination.append(word)
            backtrack(combination, i + 1, used_letters | word_mask)  # Include current word
            combination.pop()  # Backtrack

        # Update the progress bar
        if (i + 1) % progress_interval == 0:
            display_progress(i + 1, len(unique_letter_words_sorted))

def display_progress(current, total):
    """Displays a simple progress bar in the console."""
    percent = (current / total) * 100
    bar_length = 40  # Length of the progress bar
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress: |{bar}| {percent:.2f}% Complete', end='')

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

# Initialize list to hold valid combinations
valid_combinations = []
progress_interval = 100

# Start backtracking to find valid combinations
backtrack([], 0, 0)

# Finalize progress display to 100%
display_progress(len(unique_letter_words_sorted), len(unique_letter_words_sorted))
print("\n")

# Write valid combinations to the output file
with open(result_file, 'w') as file:
    for combo in valid_combinations:
        file.write(f"{', '.join(combo)}\n")

print(f"Total valid combinations found: {len(valid_combinations)}")
