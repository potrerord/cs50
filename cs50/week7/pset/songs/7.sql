/* The average energy of songs that are by Drake. */
SELECT AVG(energy)
  FROM songs AS s
 WHERE s.artist_id = artists.id
   AND 