/*
List the names of all people who starred in a movie in which Kevin Bacon
also starred.
*/

-- Movie star names and IDs with matching movie IDs
SELECT p1.name
  FROM people AS p1
       INNER JOIN stars AS s1
       ON p1.id = s1.person_id
 WHERE s1.movie_id IN
       -- Movie IDs of movies starring Kevin Bacon
       (SELECT s2.movie_id
          FROM stars AS s2
               INNER JOIN people AS p2
               ON s2.person_id = p2.id
         WHERE p2.name = 'Kevin Bacon'
           AND p2.birth = 1958  -- Avoid other Kevin Bacons
       )
-- Exclude our Kevin Bacon from list (via id, not name)
   AND p1.id <>
       (SELECT p3.id AS kb_id
          FROM people AS p3
         WHERE p3.name = 'Kevin Bacon'
           AND p3.birth = 1958
       );
