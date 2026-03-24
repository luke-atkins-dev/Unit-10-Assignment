# You must create a class named WordAnalyzer.
# __init__(self, filepath): The initializer should take the filepath (as a string) and store it as a private pathlibrary
# Path object. It should also initialize a private dictionary to hold the word frequencies.
# process_file(self): This method will contain the main logic. It must:

# Use a try-except block to handle FileNotFoundError gracefully.
# Use the pathlib.Path object's .exists() method to check for the file.
# Use the pathlib.Path object's .open() method to read the file line by line.
# Use string.punctuation to create a translation table to remove all punctuation from each line.
# Convert each line to all lowercase.
# Split each line into words and update their counts in the internal frequencies dictionary.
# The method should return True if processing was successful and False if a FileNotFoundError occurred.
# print_report(self): This method should print the results.
# Get the keys from the frequencies dictionary and sort them alphabetically.
# Print the word and its count in the specified format (see example).

from pathlib import Path

class WordAnalyzer():
    def __init__(self, filepath: str):
        self._word_frequencies = {}
        self._path = Path(filepath)
    def get_word_frequency(self, word: str):
        return self._word_frequencies.get(word)
    def count_word(self, word: str):
        exists = self.get_word_frequency(word)
        if exists:
            self._word_frequencies[word] += 1
        else:
            self._word_frequencies[word] = 1
    def process_file(self):
        


