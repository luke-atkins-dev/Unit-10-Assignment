"""
Name: Word Counter
Author: Luke Atkins
Date: 3/24/2026
Purpose: Counts number of words within specified documents
Starter Code: No starter code used.
"""
from pathlib import Path
import string
from WordAnalyzer import WordAnalyzer

# this is here because cwd is not consistent and changes depending on where the file is executed
project_dir = Path(__file__).resolve().parent
document_path = project_dir / "documents"

documents = {
    "1": document_path / "file_1.txt",
    "2": document_path / "file_2.txt",
    "3": document_path / "file_3.txt",
    "4": document_path / "file_4.txt"
}

def display_documents(options: dict[str: Path]):
    for pos, item in options.items():
        print(f"{pos}. {item.name()}")

def main():
    pass

if __name__ == "__main__":
    main()