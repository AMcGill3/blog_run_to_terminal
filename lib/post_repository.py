from lib.comment import Comment
from lib.post import Post
class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_post(self, title, contents):
        self._connection.execute(
            'INSERT INTO posts (title, contents, views) VALUES (%s, %s, 0)', [title, contents]
        )
        return None

    def view_post(self, post_id):
        post = self.find_with_comments(post_id)
        post.views += 1
        self._connection.execute(
            'UPDATE posts SET views = views + 1 where id = %s', [post_id]
        )
        return post

    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            'SELECT posts.id AS post_id, posts.title AS post_title, posts.contents AS post_contents, ' \
            'posts.views AS post_views, ' \
            'comments.id AS comment_id, comments.author, ' \
            'comments.contents AS comment_contents ' \
            'FROM posts LEFT JOIN comments ON posts.id = comments.post_id ' \
            'WHERE posts.id = %s', [post_id])
        
        comments = []
        for row in rows:
            if row['author'] and row['comment_contents']:
                comment = Comment(row['author'], row['comment_contents'])
                comments.append(comment)
    
        if len(comments) != 0:
            return Post(rows[0]['post_title'], rows[0]['post_contents'], comments, views=rows[0]['post_views'])
        else:
            print(comments)
            return Post(rows[0]['post_title'], rows[0]['post_contents'], views=rows[0]['post_views'])


    # to view all post titles on homescreen, where user can expand 
    # post to view contents and comments if they wish to do so,
    # resulting in incrementing view count

    def find_all_without_comments(self):
        rows = self._connection.execute(
            'SELECT * from posts')
        
        posts = []

        for row in rows:
            post = Post(row['title'], row['contents'])
            posts.append(f'{post.title}')

        return posts


    def add_comment_to_post(self, post_id, author, contents):
        self._connection.execute(
            'INSERT INTO comments (author, contents, post_id) ' \
            'VALUES (%s, %s, %s)', [author, contents, post_id]    
        )

        comment = Comment(author, contents)
        post = self.find_with_comments(post_id)
        post.comments.append(comment)
        return None
    
    # returns post titles without contents or comments to support view count incrementation
    def find_posts_by_keyword(self, string):
        search_term = f'%{string}%'

        rows = self._connection.execute(
            "SELECT posts.id AS post_id, posts.title AS post_title, posts.contents AS post_contents " \
            "FROM posts " \
            "WHERE posts.title LIKE %s " \
            "OR posts.contents LIKE %s ", [search_term, search_term])
        
        posts = []

        for row in rows:
            post = Post(row['post_title'], row['post_contents'])
            posts.append(f'{post.title}')

        return posts

    def all(self):
        posts = []
        p = self._connection.execute(
            'SELECT COUNT(*) from posts')
        posts_num = p[0]['count']

        for i in range(posts_num):
            post = self.find_with_comments(i + 1)
            posts.append(post)

        return posts