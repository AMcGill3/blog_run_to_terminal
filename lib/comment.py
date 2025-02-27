class Comment:
    def __init__(self, author, contents):
        self.author = author
        self.contents = contents

    def __repr__(self):
        return (f'Comment({self.author}, {self.contents})')
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

