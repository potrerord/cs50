/*
List the titles of all movies in which both Bradley Cooper and Jennifer
Lawrence starred.
*/

CREATE VIEW view_name AS
SELECT column1, column2
FROM table1
JOIN table2
ON table1.common_column = table2.common_column;



SELECT DISTINCT(movies.title)
  FROM movies AS m
       JOIN stars AS s
       ON m.id = s.movie_id

       JOIN people AS p
       ON s.person_id = p.id
          AND (p.name = 'Bradley Cooper'
               OR p.name = 'Jennifer Lawrence')

 -- Movie matches with both of the following:
 WHERE m.id IN
       -- Movies starring Bradley Cooper
       (SELECT m.id
         FROM movies AS m
              JOIN stars AS s
              ON m.id = s.movie_id

              JOIN people AS p
              ON s.person_id = p.id
        WHERE p.name = 'Bradley Cooper'
       )
   AND m.id IN
       -- Movies starring Jennifer Lawrence
       (SELECT m.id
         FROM movies AS m
              JOIN stars AS s
              ON m.id = s.movie_id

              JOIN people AS p
              ON s.person_id = p.id
        WHERE p.name = 'Jennifer Lawrence'
       );
