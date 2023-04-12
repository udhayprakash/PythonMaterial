CREATE TABLE authors (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE comments (
  id INTEGER PRIMARY KEY,
  body TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  article_id INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (article_id) REFERENCES articles(id),
  FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- DB VIEWS
    -- Creating DB View to show number of comments for each article
        CREATE VIEW article_comment_counts AS
        SELECT
        a.id AS article_id,
        a.title AS article_title,
        COUNT(c.id) AS comment_count
        FROM
        articles a
        LEFT JOIN comments c ON c.article_id = a.id
        GROUP BY
        a.id, a.title;
        -- Usage: SELECT * FROM article_comment_counts;

    -- DB view to show the top authors by the number of comments they've made
        CREATE VIEW top_comment_authors AS
        SELECT
        a.id AS author_id,
        a.name AS author_name,
        COUNT(c.id) AS comment_count
        FROM
        authors a
        JOIN comments c ON c.author_id = a.id
        GROUP BY
        a.id, a.name
        ORDER BY
        comment_count DESC;
        -- Usage: SELECT * FROM top_comment_authors;


-- DB TRIGGERS
    -- DB trigger to automatically updates the updated_at field in the articles table whenever a comment is added or deleted for that article
    CREATE TRIGGER update_article_timestamp
    AFTER INSERT OR DELETE ON comments
    FOR EACH ROW
    BEGIN
    UPDATE articles
    SET updated_at = NOW()
    WHERE id = NEW.article_id;
    END;

-- SQL stored procedure
    -- stored procedure allowing to add a new article along with multiple comments in a single transaction:
    CREATE PROCEDURE add_article_and_comments(
    IN title VARCHAR(255),
    IN body TEXT,
    IN author_id INT,
    IN comments JSON
    )
    BEGIN
    DECLARE article_id INT;

    -- Start transaction
    START TRANSACTION;

    -- Insert article
    INSERT INTO articles (title, body, author_id)
    VALUES (title, body, author_id);
    SET article_id = LAST_INSERT_ID();

    -- Insert comments
    SET @comment_count = JSON_LENGTH(comments);
    SET @i = 0;
    WHILE @i < @comment_count DO
        SET @comment = JSON_EXTRACT(comments, CONCAT('$[', @i, ']'));
        INSERT INTO comments (body, article_id, author_id)
        VALUES (@comment, article_id, author_id);
        SET @i = @i + 1;
    END WHILE;

    -- Commit transaction
    COMMIT;
    END;
    -- USAGE: CALL add_article_and_comments('New Article', 'Lorem ipsum dolor sit amet', 1, '["Comment 1", "Comment 2", "Comment 3"]');


-- FUNCTIONS
    -- function to calculate the number of comments for a given article
        CREATE FUNCTION get_comment_count(article_id INT) RETURNS INT
        BEGIN
        DECLARE comment_count INT;

        -- Calculate comment count
        SELECT COUNT(*) INTO comment_count FROM comments WHERE article_id = article_id;

        RETURN comment_count;
        END;
        -- USAGE: SELECT get_comment_count(1);
