
from pathlib import Path

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
        return self._src_path / option
    def __repr_single_option(pos: int, path: Path):
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