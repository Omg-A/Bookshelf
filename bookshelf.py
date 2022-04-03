class Bookshelf:
    def __init__(self, name, author, price, publish_year):
        self.Name = name
        self.Author = author
        self.Price = price
        self.Publish = publish_year
    def Add_Book(self):
        print("\n Book name: " + self.Name)
        print("Book author: " + self.Author)
        print("Book price: " + str(self.Price))
        print("This book was published in " + str(self.Publish))
        print("Book added to database")
    def Years_Since_Published(self):
        years_since = 2022 - self.Publish
        print("This book was published " + str(years_since) + " years ago")

book_1 = Bookshelf("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1928, 1997)
book_1.Add_Book()
book_1.Years_Since_Published()

book_2 = Bookshelf("Dairy of a Wimpy Kid", "Jef Kinney", 700, 2017)
book_2.Add_Book()
book_2.Years_Since_Published()
