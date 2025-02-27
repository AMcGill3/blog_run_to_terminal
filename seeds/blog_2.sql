DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    contents text,
    views int
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    author text,
    contents text,
    post_id int,
    constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);

INSERT INTO posts (title, contents, views) VALUES ('TV Burp was so good', 'God I miss that show', 0);
INSERT INTO comments (author, contents, post_id) VALUES ('Harry Hill', 'Too right', 1);