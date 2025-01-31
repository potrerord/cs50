/*
List the titles of the five highest rated movies (in order) that
Chadwick Boseman starred in, starting with the highest rated.
*/
SELECT m.title
  FROM movies AS m
       INNER JOIN stars AS s
       ON m.id = s.movie_id

       INNER JOIN ratings AS r
       ON m.id = r.movie_id
 WHERE s.person_id =
       (SELECT id
          FROM people
         WHERE name = 'Chadwick Boseman'
       )
 ORDER BY r.rating DESC
 LIMIT 5;
