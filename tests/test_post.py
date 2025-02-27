from lib.comment import Comment
from lib.post import Post
post_1 = Post('Dale Winton was the better Hole in the Wall host', 'Anton Du Beke was whack')

def test_post_initialises_with_title_and_contents_and_0_views_and_empty_list_of_comments():
    assert post_1.title == 'Dale Winton was the better Hole in the Wall host'
    assert post_1.contents == 'Anton Du Beke was whack'
    assert post_1.comments == []
    assert post_1.views == 0

def test_repr_prints_without_comments_if_none():
    assert repr(post_1) == 'Post(Dale Winton was the better Hole in the Wall host, Anton Du Beke was whack, Views: 0)'