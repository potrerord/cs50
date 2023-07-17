/*
List the titles of all movies in which both Bradley Cooper and Jennifer
Lawrence starred.
*/

CREATE VIEW jlaw_bcoop_movies AS
    SELECT *
      FROM movies AS m
           JOIN stars AS s
           ON m.id = s.movie_id

           JOIN people AS p
           ON s.person_id = p.id
              AND (p.name = 'Bradley Cooper'
                   OR p.name = 'Jennifer Lawrence')

SELECT DISTINCT(movies.title)
  FROM jlaw_bcoop_movies AS jbmovies

 -- Movie matches with both of the following:
 WHERE m.id IN
       -- Movies starring Bradley Cooper
       (SELECT m.id
          FROM jbmovies
         WHERE p.name = 'Bradley Cooper'
       )
   AND m.id IN
       -- Movies starring Jennifer Lawrence
       (SELECT m.id
          FROM jbmovies
         WHERE p.name = 'Jennifer Lawrence'
       );
