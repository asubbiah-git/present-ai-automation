# Utility function independant of the project level code.
# do no import any project specific file import, it will cause cyclic import

def normalize_text(text: str) -> str:
    return ' '.join(text.split())

def convert_string_to_func_name_Format(text: str) -> str:
    return text.lower().replace(" ", "_").strip()