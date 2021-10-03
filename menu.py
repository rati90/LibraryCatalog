import sys
from library import Library


class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.library = Library()
        self.choices = {
            "1": self.show_library,
            "2": self.search_items,
            "3": self.add_book,
            "4": self.add_dvd,
            "5": self.add_cd,
            "6": self.add_magazine,
            "7": self.modify_item_menu,
            "8": self.delete_item,
            "9": self.quit
        }

    def display_menu(self):
        print(
            """
        Notebook Menu
        1. Show all items(Books, DVDs, CDs, and Magazines)
        2. Search items
        3. Add Book
        4. Add DVD
        5. Add CD
        6. Add Magazine
        7. Modify item
        8. Delete item        
        9. Quit
        """
              )

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_library(self, library_items=None):
            if not library_items:
                library_items = self.library.library_items

            for item in library_items:
                if item[1] == "Book":
                    print("{0}: Title: {1} | Subject: {2} | Sort: {3} "
                          "\nISBN: {4} | Authors: {5} | DDS: {6}".format(
                                                     item[0].id,
                                                     item[0].title,
                                                     item[0].subject,
                                                     item[1],
                                                     item[2],
                                                     item[3],
                                                     item[4]

                                                                        ))

                elif item[1] == "DVD":
                    print("{0}: Title: {1} | Subject: {2} | Sort: {3}"
                          " \nGenre: {4} | Actors: {5} | Directors: {6}".format(
                                                     item[0].id,
                                                     item[0].title,
                                                     item[0].subject,
                                                     item[1],
                                                     item[2],
                                                     item[3],
                                                     item[4]
                                                                           ))

                elif item[1] == "CD":
                    print("{0}: Title: {1} | Subject: {2} | Sort: {3}"
                          " \nArtists: {4}".format(
                                                    item[0].id,
                                                    item[0].title,
                                                    item[0].subject,
                                                    item[1],
                                                    item[2],
                                                   ))

                elif item[1] == "Magazine":
                    print("{0}: Title: {1} | Subject: {2} | Sort: {3}"
                          " \nISBM: {4} | Volume: {5} | Editors: {6}".format(
                                                     item[0].id,
                                                     item[0].title,
                                                     item[0].subject,
                                                     item[1],
                                                     item[2],
                                                     item[3],
                                                     item[4]
                                                                           ))

    def search_items(self):
        """
        Searchs with id, title or, subject
        """
        filter = input("Search for: ")
        library_items = self.library.search(filter)
        self.show_library(library_items)

    def add_book(self):
        title = input("Please enter the title: ")
        subject = input("Please enter the subject: ")
        isbn = input("Please enter the ISBN code: ")
        authors = input("Please enter the authors: ")
        ddsnumber = input("Please enter the dds nubmer: ")

        self.library.new_book(title, subject, isbn, authors, ddsnumber)

    def add_dvd(self):
        title = input("Please enter the title: ")
        subject = input("Please enter the subject: ")
        genre = input("Please enter the genre: ")
        actors = input("Please enter the actors: ")
        directors = input("Please enter the directors: ")

        self.library.new_dvd(title, subject, genre, actors, directors)

    def add_cd(self):
        title = input("Please enter the title: ")
        subject = input("Please enter the subject: ")
        artists = input("Please enter the artists: ")
        self.library.new_cd(title, subject, artists)

    def add_magazine(self):
        title = input("Please enter the title: ")
        subject = input("Please enter the subject: ")
        isbn = input("Please enter the isbn: ")
        volume = input("Please enter the volume: ")
        editors = input("Please enter the editors: ")

        self.library.new_magazine(title, subject, isbn, volume, editors)

    def modify_item_menu(self):
        """
        Modify item with search of id.
        You can modify title and subject of every item.
        """
        item_id = input("Enter a item id which you want to modify: ")
        new_title = input("Please enter new title: ")
        new_subject = input("Please enter new subject: ")
        self.library.modify_item(item_id, new_title, new_subject)

    def delete_item(self):
        """
        It finds the item with id end deletes it
        """
        item_id = input("Enter a item id which you want to delete: ")
        self.library.library_items.pop(int(item_id) - 1)
        print("Successful deletion")

    def quit(self):
        """
        To leave the catalog
        """
        print("Thanks you for using your Library Catalog")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()