CREATE TABLE movies (
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, 
    description TEXT NOT NULL, 
    length INTEGER NOT NULL, 
    path TEXT NOT NULL, 
    uploader_id INTEGER NOT NULL, 
    fsk TEXT, 
    tags TEXT, 
    file_extension TEXT
);

CREATE TABLE tags (
    id INTEGER PRIMARY KEY, 
    tag TEXT NOT NULL
);

CREATE TABLE movie_tag_mapping (
    tag_id INTEGER,
    movie_id INTEGER,
    CONSTRAINT fk_tags FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE,
    CONSTRAINT fk_movies FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
    PRIMARY KEY (tag_id, movie_id)
);



