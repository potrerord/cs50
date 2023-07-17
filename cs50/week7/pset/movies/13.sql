/*
List the names of all people who starred in a movie in which Kevin Bacon
also starred.
*/


-- Names of stars of movies starring Kevin Bacon
SELECT p1.name
  FROM people AS p1
       INNER JOIN stars AS s1
       ON p1.id = s1.person_id
 WHERE s1.movie_id =
       -- Movie IDs of movies starring Kevin Bacon
       (SELECT s2.movie_id
          FROM stars AS s2
               INNER JOIN people AS p2
               ON s2.person_id = p2.id
         WHERE p2.name = 'Kevin Bacon'
           AND p2.birth = 1958  -- Avoid other Kevin Bacons
       )
   AND p1.name <> 'Kevin Bacon';  -- Exclude Kevin Bacon from list
