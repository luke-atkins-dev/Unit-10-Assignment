"""
Name: WordAnalyzer.py
Author: Luke Atkins
Date: 3/24/2026
Purpose: Handles counting words from a singular text file
Starter Code: No starter code used.
"""

from pathlib import Path
from string import punctuation

class AnalyzationFailedError(Exception):
    pass

class WordAnalyzer():
    _translation = str.maketrans("", "", punctuation + '\n')
    DEFAULT_STOP_WORDS = ['']
    def __init__(self, filepath: str, stop_words:list=DEFAULT_STOP_WORDS):
        """
        Initialize

        Args:
            filepath: (str) path to the file represented as a string
            stop_words: (list, optional) a list of word to not be counted in the final count
        """
        self._word_frequencies = {}
        self._path = Path(filepath)
        self._stop_words = stop_words
    def get_word_frequency(self, word: str) -> int:
        """
        Returns how frequent a word is within the document once processed


        Args:
            word: (str) the word to check the count of

        Returns:
            int: the amount of occurences
        """
        return self._word_frequencies.get(word)
    def count_word(self, word: str) -> None:
        """
        Counts a word within the internal dictionary

        Args:
            word: (str) word to be counted
        
        Returns:
            None
        """
        if word in self._stop_words:
            return

        exists = self.get_word_frequency(word)
        if exists:
            self._word_frequencies[word] += 1
        else:
            self._word_frequencies[word] = 1
    def _get_words(line: str) -> list[str]:
        """
        Strip the line of whitespace and punctuation

        Args:
            line: (str) the line to be processed
        
        Returns:
            list[str]: the words from the line
        """
        return line.lower().translate(WordAnalyzer._translation).strip().split(' ')
    def get_file_path(self) -> Path:
        """
        Returns the internal file path

        Args:
            None

        Returns:
            Path: the internal path
        """
        return self._path
    def process_file(self) -> bool:
        """
        Processes the file and returns whether the operation was successful

        Args:
            None

        Returns:
            bool: Whether the operation was successful
        """
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
        """
        Prints the word count within the document

        Args:
            None

        Returns:
            None
        """
        keys = list(self._word_frequencies.keys())
        keys.sort()

        for word in keys:
            count = self._word_frequencies[word]
            print(f'{word:<20}:: {count}')



