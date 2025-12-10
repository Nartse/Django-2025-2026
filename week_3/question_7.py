class Library:
    def __init__(self):
        self.titles=[]
    def add_book(self,title):
        self.titles.append(title)
    def show_book(self):
        print("Titles:",self.titles)
l=Library()
l.add_book("Verity")
l.add_book("Housemaid")
l.add_book("Silent Patient")
l.show_book()