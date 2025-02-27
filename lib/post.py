from lib.comment import Comment

class Post:
    def __init__(self, title, contents, comments = None, views=0):
        self.title = title
        self.contents = contents
        if comments == None:
            comments = []
        self.comments = comments
        self.views = views

    def __repr__(self):
        if len(self.comments) != 0:
            return f'Post({self.title}, {self.contents}, Views: {self.views}\n{self.comments})\n'
        else:
            return f'Post({self.title}, {self.contents}, Views: {self.views})'
            
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

