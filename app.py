from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blog_2.sql")

    def run(self):
        post_repository = PostRepository(self._connection)
        print('Welcome!')
        while True:
            print('What would you like to do?\n')
            print('1 - See all posts')
            print('2 - Find a post')
            print('3 - Publish a post')
            print('0 - Exit\n')
            choice = input('Enter your choice: ')
      
            if choice == '1':
                while True:
                    print('\nPosts:\n')
                    titles = post_repository.find_all_without_comments()
                    for i, post in enumerate(titles):
                        print(f'* {i + 1} - {post}')

                    print('\nWhat would you like to do?\n')
                    print('1 - View a post')
                    print('2 - Return to home\n')
                    choice = input('Enter your choice: ')
          
                    if choice == '1':
                        view_post(titles, post_repository)

                    elif choice == '2':
                        break

                    else:
                        print('Invalid choice. Please enter a valid option')
                        continue


            elif choice == '2':
                search = input("Search here: ")

                posts = post_repository.find_posts_by_keyword(search)

                while True:
                    print('\n')
                    print(view_posts_by_keyword(post_repository, search))
                    print('\nWhat would you like to do?\n')
                    print('1 - View a post')
                    print('2 - Return to home\n')
                    choice = input('Enter your choice: ')
          
                    if choice == '1':
                        view_post(posts, post_repository)
                    elif choice == '2':
                        break


            elif choice == '3':
                title = input("Post title: ")
                contents = input("Post contents: ")
                post_repository.add_post(title, contents)

            elif choice == '0':
                print('Goodbye!')
                break

            else:
                print('Invalid choice. Please enter a valid option\n')
                continue


def post_options(post_repository, post_id):
    while True:
        print('\nWhat would you like to do?\n')
        print('1 - Add comment')
        print('2 - View another post or return to home')
        choice = input('Enter your choice: ')
        if choice == '1':
            author = input('Enter your name: ')
            c = input('Enter your comment: ')
            post_repository.add_comment_to_post(post_id, author, c)
        elif choice == '2':
            break
        else:
            print('Invalid choice. Please enter a valid option')
            continue

def view_post(titles, post_repository):
    id = int(input('\nPlease input the number of the post you wish to view: \n'))
    for i, post in enumerate(titles):
        if i + 1 == id:
            rows = post_repository._connection.execute(
                'SELECT posts.id, posts.title ' \
                'FROM posts ' \
                'WHERE posts.title = %s', [post.strip()]
            )
            for row in rows:
                post_id = row['id']
                p = post_repository.view_post(int(post_id))
                print(p)
                post_options(post_repository, post_id)

def view_posts_by_keyword(post_repository, search):
    for i, post in enumerate(post_repository.find_posts_by_keyword(search)):
        print(f'* {i + 1} - {repr(post)}')

if __name__ == '__main__':
    app = Application()
    app.run()
