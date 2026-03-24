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
from string import punctuation

class AnalyzationFailedError(Exception):
    pass

class WordAnalyzer():
    _translation = str.maketrans("", "", punctuation + '\n')
    DEFAULT_STOP_WORDS = ['']
    def __init__(self, filepath: str, stop_words:list=DEFAULT_STOP_WORDS):
        self._word_frequencies = {}
        self._path = Path(filepath)
        self._stop_words = stop_words
    def get_word_frequency(self, word: str) -> int:
        return self._word_frequencies.get(word)
    def count_word(self, word: str) -> None:
        if word in self._stop_words:
            return

        exists = self.get_word_frequency(word)
        if exists:
            self._word_frequencies[word] += 1
        else:
            self._word_frequencies[word] = 1
    def _get_words(line: str) -> list[str]:
        return line.lower().translate(WordAnalyzer._translation).strip().split(' ')
    def get_file_path(self) -> Path:
        return self._path
    def process_file(self) -> bool:
        try:
            if not self._path.exists():
                raise FileNotFoundError
        except FileNotFoundError:
            return False

        with self._path.open("r") as file:
            for line in file:
                for word in WordAnalyzer._get_words(line):
                    self.count_word(word)

        return True
    def print_report(self) -> None:
        keys = list(self._word_frequencies.keys())
        keys.sort()

        for word in keys:
            count = self._word_frequencies[word]
            print(f'{word:<20}:: {count}')



