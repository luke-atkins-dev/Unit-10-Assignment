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

def display_documents(options: dict[str: Path]):
    for pos, item in options.items():
        print(f"{pos}. {item.name()}")

def get_document_option() -> Path:
    pass

# def verify_paths(document_options: dict[str: Path]):
#     assert document_path.is_dir(), "Documents path does not exist! Please add a folder called 'documents' inside of the project directory"

#     for pos, option in document_options.items():
#         assert option.is_file(), f"{option.name()} at position {pos} is not a valid file!"
    
#     return True

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
    def __init__(self, src_path: Path):
        self._options = {}
        self._src_path = src_path
    def set_options(self, options: dict[str: Path]):
        self._options = options
    def get_option(self, pos: str):
        opt = self._options.get(pos)
        if opt:
            return opt
        else:
            raise InvalidDocumentSelectionError(pos)
    def get_options(self):
        return {k:self._get_option_path(v) for k, v in self._options.items()}
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
        
        return out

def select_document(options: DocumentOptions) -> Path:
    print(options)
    
    document = None

    while document is None:
        str_option = input(f"Choose document: (1-{len(options.get_options())}): ")

        if str_option == "quit":
            break

        try:
            if str_option.isalpha():
                raise ValueError()
            
            document = options.get_option(str_option)
            
        except ValueError:
            print("Only numerical input is allowed within the specified ranges")
        except InvalidDocumentSelectionError as e:
            print(f"No document exists at position: {e.pos}")
    
    return document
    
from sys import exit

def main():
    options = DocumentOptions(document_path)
    options.set_options(documents)

    selection = select_document(options)

    if selection:
        pass
    else:
        exit(1)
    

if __name__ == "__main__":
    main()