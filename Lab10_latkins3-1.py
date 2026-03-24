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
    "1": "monte_cristo.txt",
    "2": "princess_mars.txt",
    "3": "Tarzan.txt",
    "4": "treasure_island.txt"
}

def main():
    options = DocumentOptions(document_path, documents)

    print("Please select a file to analyze:")

    selection = options.select_document()

    if selection is None:
        # user has quit
        print("Quitting...")
        return

    analyzer = WordAnalyzer(
        str(selection) # It would be better just to pass the path object, but for project requirements it needs to be a string
    )
    
    if analyzer.process_file():
        print(f'\nProcessing {analyzer.get_file_path().stem}...\n')
        analyzer.print_report()
    else:
        print("Failed to analyze file")
    
    input("\nPress enter to analyze another file...")
    main()

if __name__ == "__main__":
    main()