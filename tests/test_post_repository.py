from lib.comment import Comment
from lib.post import Post
from lib.post_repository import PostRepository

def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    assert repository.find_with_comments(1) == Post('TV Burp was so good', 'God I miss that show',
                                                    [Comment('Harry Hill', 'Too right')])

def test_find_with_comments_if_post_has_no_comments(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    repository.add_post("I didn't even think the Seinfeld ending was that bad", "Yeah it could've been better but it could've been worse")
    assert repository.find_with_comments(2) == Post("I didn't even think the Seinfeld ending was that bad", 
                                                    "Yeah it could've been better but it could've been worse")

def test_find_all_without_comments(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    assert repository.find_all_without_comments() == ['TV Burp was so good']


def test_add_comment_to_post(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    repository.add_comment_to_post(1, 'Carrie Bradshaw', "Big's moving to Paris")
    assert repository.find_with_comments(1) == Post('TV Burp was so good', 'God I miss that show',
                                                    [Comment('Harry Hill', 'Too right'),
                                                    Comment('Carrie Bradshaw', "Big's moving to Paris")])


def test_add_post_then_add_comment(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    repository.add_post('Dale Winton here saying I was the best Hole in the Wall host', 'Anton Du Beke wishes he was me')
    repository.add_comment_to_post(2, 'Anton Du Beke', 'Sod off')
    assert repository.find_with_comments(2) == Post('Dale Winton here saying I was the best Hole in the Wall host', 
                                                    'Anton Du Beke wishes he was me',
                                                    [Comment('Anton Du Beke', 'Sod off')])

def test_all(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    assert repository.all() == [Post('TV Burp was so good', 'God I miss that show',
                                    [Comment('Harry Hill', 'Too right')])]

def test_all_after_addition_of_post(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    repository.add_post('Dale Winton here saying I was the best Hole in the Wall host', 'Anton Du Beke wishes he was me')
    assert repository.all() == [Post('TV Burp was so good', 'God I miss that show',
                                    [Comment('Harry Hill', 'Too right')]),
                                Post('Dale Winton here saying I was the best Hole in the Wall host', 
                                                    'Anton Du Beke wishes he was me')]

def test_find_posts_by_keyword(db_connection):
    db_connection.seed("seeds/blog_2.sql")
    repository = PostRepository(db_connection)
    assert repository.find_posts_by_keyword('TV') == ['TV Burp was so good']

