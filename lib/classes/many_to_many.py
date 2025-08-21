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
        if hasattr(self, 'title'):
            return 'Cannot change the title after instantiation'
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine


class Author:
    def __init__(self, name):
        self.name = name
    
    articles = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            return 'Cannot change the name after instantiation'
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazines = {article.magazine for article in self.articles()}
        return list(magazines)

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            article = Article(author = self, magazine= magazine, title=title)
            return article
        return 'failed'
    def topic_areas(self):
        topics = {magazine.category for magazine in self.magazines()}
        return list(topics) if topics else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 17:
            self._name = name

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        contributors = {article.author for article in self.articles()}
        return list(contributors)

    def article_titles(self):
        title = [article.title for article in self.articles()]
        return title if title else None

    from collections import Counter
    def contributing_authors(self):
        author = {}
        for article in self.articles():
            author[article.author] = author.get(article.author, 0) + 1
        authors = [author for author, count in author.items() if count > 2]
        return authors or None