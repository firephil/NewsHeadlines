# Utility Classes and Function for News

class Article:

    def __init__(self, title: str = "" , text: str = "", link: str = "", date: str = "", categ: str = ""):
        self.title = title
        self.text = text.replace("&nbsp;", " ")
        self.link = link
        self.date = date
        self.categ = categ

    def __repr__(self):

        return f"<Article Title: {self.title}  Text: {self.text} Link: {self.link} Date: {self.date} Categ {self.categ}>"
    
    def getText(self) -> str:
        
        return f"{self.title}\n{self.text}\n{self.link}\n{self.date}\n{self.categ}"