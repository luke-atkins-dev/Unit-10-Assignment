"""
Name: Word Counter
Author: Luke Atkins
Date: 3/24/2026
Purpose: Counts number of words within specified documents
Starter Code: No starter code used.
"""
from pathlib import Path
from WordAnalyzer import WordAnalyzer
from DocumentOptions import DocumentOptions

# this is here because cwd is not consistent and changes depending on where the file is executed
project_dir = Path(__file__).resolve().parent
document_path = project_dir / "documents"

documents = {
    "1": "file_1.txt",
    "2": "file_2.txt",
    "3": "file_3.txt",
    "4": "file_4.txt"
}


    
from sys import exit

def main():
    options = DocumentOptions(document_path, documents)

    selection = options.select_document()

    if selection is None:
        exit(1)
        return

    analyzer = WordAnalyzer(
        str(selection) # It would be better just to pass the path object, but for project requirements it needs to be a string
    )
    
    if analyzer.process_file():
        analyzer.print_report()
    else:
        print("Failed to analyze file")
    

if __name__ == "__main__":
    main()