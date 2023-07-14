/* The names of songs that are by Post Malone. */
SELECT name
  FROM songs AS s
       JOIN artists AS a
       ON s.artist_id = a.id
