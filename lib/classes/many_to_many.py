class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise Exception("Name cannot be changed after initialization")
        
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception("Title MUST be a string between 5 and 50 characters (inclusive).")
        
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception(f"{author} is not an instance of the Author class")
        
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception(f"{magazine} is not an instance of the Author class")
            


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed after initialization")
            

    def articles(self):
        return[article for article in Article.all if article.author == self and isinstance(article, Article)]

    def magazines(self):
            magazine_list = [article.magazine 
                             for article in Article.all 
                             if article.author == self and isinstance(article.magazine, Magazine)
                            ]
            return list(set(magazine_list))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception(f"{magazine} is not an object of Magazine")
        
        return Article(self, magazine, title)
        
    def topic_areas(self):
        if not self.articles():
            return None
        categories = [article.magazine.category for article in self.articles()]
        return list(set(categories))



class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (isinstance(name, str) and 2 <= len(name) <= 16):
            self._name = name
        else:
            raise Exception("Name must be a string between 2 and 16 characters.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):        
        if isinstance(category, str) and len(category) > 0 :
            self._category = category
        else:
            raise Exception("Category must be a non-empty string.")

    
    def articles(self):
        return[article for article in Article.all if article.magazine == self and isinstance(article, Article)]

    def contributors(self):
        contributor_list = [article.author 
                            for article in Article.all
                            if article.magazine == self and isinstance(article.author, Author)]
        return list(set(contributor_list))
    
    def article_titles(self):
        if not self.articles():
            return None
        else:
            return [article.title for article in self.articles()]
    
    def contributing_authors(self):
        if not self.articles():
            return None
        
        author_counts = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                author_counts[article.author] = author_counts.get(article.author, 0) + 1
            else:
                raise Exception(f"{article.author} is not an instance of Author class")

        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None