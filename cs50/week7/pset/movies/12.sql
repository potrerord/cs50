/*
List the titles of all movies in which both Bradley Cooper and Jennifer
Lawrence starred.
*/
SELECT DISTINCT(title)
  FROM movies AS m1
       INNER JOIN stars AS s1
       ON m1.id = s1.movie_id

       INNER JOIN people AS p1
       ON s1.person_id = p1.id
          AND (p1.name = 'Bradley Cooper'
               OR p1.name = 'Jennifer Lawrence')

 -- Movie matches with both of the following:
 WHERE m1.id IN
       -- Movies starring Bradley Cooper
       (SELECT movies.id
         FROM movies AS m2
              INNER JOIN stars AS s2
              ON m2.id = s2.movie_id

              INNER JOIN people AS p2
              ON s2.person_id = p2.id
        WHERE p2.name = 'Bradley Cooper'
       )
   AND m1.id IN
       -- Movies starring Jennifer Lawrence
       (SELECT movies.id
         FROM movies AS m3
              INNER JOIN stars AS s3
              ON m3.id = s3.movie_id

              INNER JOIN people AS p3
              ON s3.person_id = p3.id
        WHERE p3.name = 'Jennifer Lawrence'
       );


-- inner join for bcoop and jlaw movies
SELECT AS ,  AS
FROM
INNER JOIN employees e2 ON e1.manager_id = e2.employee_id;


SELECT movies.id
  FROM movies AS m2
       INNER JOIN stars AS s2
       ON m2.id = s2.movie_id

       INNER JOIN people AS p2
       ON s2.person_id = p2.id



WHERE  IN (id1, id2)
GROUP BY restaurant
HAVING COUNT(employee_id) = 2;
