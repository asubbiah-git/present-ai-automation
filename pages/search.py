from elements.search_elements import Element_hybrid_search, Element_help_title_text

class SearchInAPage:
    def __init__(self, sb):
        self.sb = sb

    def hyrid_search(self, text):
        self.sb.type(f"{Element_hybrid_search}", text)

    def search_text_in_title(self, text):
        elements = self.sb.find_elements(Element_help_title_text)
        for el in elements:
            if text in el.text:
                return True
        return False