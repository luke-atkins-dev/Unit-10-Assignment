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
    "1": "file_1.txt",
    "2": "file_2.txt",
    "3": "file_3.txt",
    "4": "file_4.txt"
}

class InvalidDocumentSelectionError(Exception):
    def __init__(self, invalid_selection_pos: int):
        super().__init__(f"Invalid selection pos: {invalid_selection_pos}")
        self.pos = invalid_selection_pos

class DocumentOptions:
    """
    Manages and displays document options
    """
    def __init__(self, src_path: Path, options: dict[str: Path]):
        self._options = {}
        self._src_path = src_path
        self._options = options
    def set_options(self, options: dict[str: Path]):
        self._options = options
    def get_option(self, pos: str):
        opt = self._options.get(pos)
        if opt:
            return self._get_option_path(opt)
        else:
            raise InvalidDocumentSelectionError(pos)
    def get_options(self):
        return {k:self._get_option_path(v) for k, v in self._options.items()}
    def select_document(self):
        document = None

        while document is None:
            str_option = input(f"Choose document: (1-{len(self.get_options())}): ")

            if str_option.lower() == "exit":
                break

            try:
                if str_option.isalpha():
                    raise ValueError()
                
                document = self.get_option(str_option)
                
            except ValueError:
                print("Only numerical input is allowed within the specified ranges")
            except InvalidDocumentSelectionError as e:
                print(f"No document exists at position: {e.pos}")
            except KeyboardInterrupt:
                break
        
        return document
    # private
    def _get_option_path(self, option: str):
        return self._src_path / option
    def __repr_single_option(pos: int, path: Path):
        return f"{pos}. {path.stem}"
    def __repr__(self):
        out = "Document Options:\n"
        options = self.get_options()
        option_strings = []

        for pos, option_path in options.items():
            option_strings.append(DocumentOptions.__repr_single_option(
                pos, option_path
            ))
        
        out += '\n'.join(option_strings)
        
        out += 'Exit: (Close program)'

        return out
    
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