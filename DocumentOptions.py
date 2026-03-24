
"""
Name: DocumentOptions.py
Author: Luke Atkins
Date: 3/24/2026
Purpose: Manages documents and document selection
Starter Code: No starter code used.
"""

from pathlib import Path

class InvalidDocumentSelectionError(Exception):
    def __init__(self, invalid_selection_pos: int):
        super().__init__(f"Invalid selection pos: {invalid_selection_pos}")
        self.pos = invalid_selection_pos

class DocumentOptions:
    """
    Manages, displays, and selects document options
    """
    def __init__(self, src_path: Path, options: dict[str: Path]):
        """
        Initialize

        Args:
            src_path: (Path) Path to the root directory for all documents
            options: (dict[str: Path]) Mapping of option identifiers
        """
        self._options = {}
        self._src_path = src_path
        self._options = options
    def set_options(self, options: dict[str: Path]):
        """
        Set or replace the available document options.

        Args:
            options (dict[str, Path]): Mapping of option identifiers (e.g., "1", "2")
                to relative document paths.

        Returns:
            None
        """
        self._options = options
    def get_option(self, pos: str):
        """
        Retrieve a single document path based on its selection key.

        Args:
            pos (str): The selection key corresponding to a document option.

        Returns:
            Path: The full path to the selected document (joined with the source path).

        Raises:
            InvalidDocumentSelectionError: If the provided selection key does not exist.
        """
        opt = self._options.get(pos)
        if opt:
            return self._get_option_path(opt)
        else:
            raise InvalidDocumentSelectionError(pos)
    def get_options(self):
        """
        Get all available document options with their resolved paths.

        Returns:
            dict[str, Path]: A dictionary mapping option identifiers to their full paths.
        """
        return {k:self._get_option_path(v) for k, v in self._options.items()}
    def select_document(self) -> Path | None:
        """
        Prompts the user to select a document from available options.

        Displays the list of options and repeatedly prompts the user until a valid
        selection is made or the user exits.

        Returns:
            Path | None: The selected document path, or None if the user exits
            or interrupts the selection process.

        Raises:
            KeyboardInterrupt: If the user interrupts input (handled internally).
        """
        document = None

        while document is None:
            print(self)
            option_count = len(self.get_options())
            str_option = input(f"Choose document: (1-{option_count+1}): ")

            try:
                if str_option.isalpha():
                    raise ValueError()
                
                if str_option == str(option_count+1):
                    break

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
        """
        Construct the full path for a given document option.

        Args:
            option (str): The relative path or filename of the document.

        Returns:
            Path: The full path resolved against the source directory.
        """
        return self._src_path / option
    def __repr_single_option(pos: int, path: Path):
        """
        Format a single option entry for display.

        Args:
            pos (str): The position of the option.
            path (str): The display name of the document.

        Returns:
            str: A formatted string representing the option.
        """
        return f"{pos}. {path}"
    def __repr__(self):
        out = "Document Options:\n"
        options = self.get_options()
        option_strings = []

        for pos, option_path in options.items():
            option_strings.append(DocumentOptions.__repr_single_option(
                pos, option_path.stem
            ))
        
        option_strings.append(
            DocumentOptions.__repr_single_option(
                str(len(options)+1), 'Exit'
            )
        )

        out += '\n'.join(option_strings)

        return out