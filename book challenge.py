class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print(f"{self.title} is the book which was written by {self.author} and selling at {self.price}.")

a = book("The Ghost Rider", "Neil Peart", 299)
a.show_details()