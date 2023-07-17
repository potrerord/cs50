/*
List the names of all people who starred in a movie in which Kevin Bacon
also starred.
*/


-- Names of stars of movies starring Kevin Bacon
SELECT p1.name
  FROM people AS p1
 WHERE p1.id =
       -- IDs of stars of movies starring Kevin Bacon
       (SELECT s1.person_id
          FROM stars AS s1
         WHERE s1.movie_id =
               -- Movie IDs starring Kevin Bacon
               (SELECT s2.movie_id
                  FROM stars AS s2
                 WHERE s2.person_id =
                       -- Kevin Bacon's ID
                       (SELECT p2.id
                          FROM people AS p2
                         WHERE p2.name = 'Kevin Bacon'
                       )
               )
       )
   AND p1.name <> 'Kevin Bacon';  -- Exclude Kevin Bacon from list
