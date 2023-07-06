#!/usr/bin/env python3

class Book:
    
    def __init__(self, title = "Title", page_count = "1"):
        self.title = title
        self.page_count = page_count

    def get_pages(self):
        return self._page_count
    
    def set_pages(self, new_pages):
        if type(new_pages) == int:
            self._page_count = new_pages
        else: 
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_pages, set_pages)