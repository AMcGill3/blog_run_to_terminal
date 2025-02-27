from lib.comment import Comment
comment_1 = Comment('Anton Du Beke', 'Sod off')

def test_comment_initialises_with_author_and_contents():
    assert comment_1.author == 'Anton Du Beke'
    assert comment_1.contents == 'Sod off'

