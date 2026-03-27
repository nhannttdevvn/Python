# 1. Tạo class book với thuộc tính 
# title, author, year. 

class Book: 
  def __init__ (self, title, author, year): 
    self.title = title 
    self.author = author 
    self.year = year

  def display_info(self): 
    print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

  
Book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
Book1.display_info()
Book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
Book2.display_info()
 
# Output 
# Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925
# Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960