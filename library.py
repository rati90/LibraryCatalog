# id for all items
last_id = 0


class LibraryItems:
    """
    All items store in the library get 
    type: book, cd or dvd
    title, UPC and the subject it is about"""

    def __init__(self,
                 title: str,
                 subject: str
                 ):

        self.title = title
        self.subject = subject
        global last_id
        last_id += 1
        self.id = str(last_id)

    def match(self, filter):
        return filter in self.id


class Library:
    """
    Represent a collection of books, CD, DVD. 
    Here is added new item and searchedd the existed one
    """

    def __init__(self):
        """Library with an empty list"""
        self.library_items = []

    def new_book(self,
                 title: str,
                 subject: str,
                 isbn: str,
                 authors: str,
                 ddsnumber=""):

        """
        Create a new book and add it to the list.
        books + need to have isbn, authors and ddsnumber (to search in physical libarary)
        """
        sort = "Book"
        self.sort = sort
        self.isbn = isbn
        self.authors = authors
        self.ddsnumber = ddsnumber
        self.library_items.append([LibraryItems(title, subject), sort, isbn, authors, ddsnumber])

    def new_dvd(self,
                title: str,
                subject: str,
                genre: str,
                actors: str,
                directors: str):
        """
        Creats the DVD,
        DVD + need to have  genre, actors and directors
        """
        sort = "DVD"
        self.sort = sort
        self.genre = genre
        self.actors = actors
        self.directors = directors

        self.library_items.append([LibraryItems(title, subject), sort, genre, actors, directors])

    def new_cd(self,
               title: str,
               subject: str,
               artists: str):
        """
        Creates new cd
        CD need +  need to have artists
        """
        sort = "CD"
        self.sort = sort
        self.artists = artists

        self.library_items.append([LibraryItems(title, subject), sort, artists])

    def new_magazine(self,
                     title: str,
                     subject: str,
                     isbn: str,
                     volume: str,
                     editors: str):
        """
        Creates new magazine
        Magazine + needs to have isbn, volume, editors
        """
        sort = "Magazine"
        self.sort = sort
        self.isbn = isbn
        self.volume = volume
        self.editors = editors

        self.library_items.append([LibraryItems(title, subject), sort, isbn, volume, editors])

    def _find_item(self, item_id):
        """Locate the note with the given id."""
        for item in self.library_items[int(item_id) - 1]:
            if item.id == item_id:
                return item
            return None

    def modify_item(self, item_id, new_title, new_subject):
        """Find the note with the given id and change its
        memo to the given value."""
        item = self._find_item(item_id)
        if item:
            item.title = new_title
            item.subject = new_subject
            print("Item was modified")
            return True
        print("There is no id with this number")
        return False

    def search(self, filter):
        """Find all notes that match given filter
        string."""
        return [item for item in self.library_items if item[0].match(filter)]


