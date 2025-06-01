import yaml
import time
import functools
from pathlib import Path
from functools import wraps
from pages.search import SearchInAPage
from pages.support_page import SupportPage
from utilities.utils import convert_string_to_func_name_Format

def suite_data(yaml_path):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            grandparent_dir = Path(__file__).resolve().parent.parent
            constructed_path = yaml_path.split("/")
            constructed_path.insert(1, getattr(self, "language", "english"))
            updated_yaml_path = Path.joinpath(grandparent_dir, Path(*constructed_path))
            with open(updated_yaml_path, "r") as f:
                data = yaml.safe_load(f)
            self.suite_data = data
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def go_to_faq_section(section):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            support_page = SupportPage(self)
            search_page = SearchInAPage(self)
            support_page.navigate_to_support_page()
            assert search_page.search_text_in_title(section) is True, f"{section}, is not found in title text"
            support_page.expand_support_section(section)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
