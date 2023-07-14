/* The average energy of songs that are by Drake. */
SELECT AVG(energy)
  FROM songs AS s
       JOIN 
 WHERE s.artist_id = artists.id
   AND artists.name = 'Drake';