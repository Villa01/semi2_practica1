SELECT  a.name Artista,  COUNT(s.idSong) Cantidad FROM practica1.artist a
JOIN practica1.song s on s.Artist_idArtist = a.idArtist
GROUP BY a.idArtist
ORDER BY COUNT(s.idSong) DESC
LIMIT 10;

SELECT s.name Cancion, COUNT(s.name) Reproducciones FROM practica1.song s
GROUP BY s.name, s.Artist_idArtist
ORDER BY COUNT(s.name) DESC
LIMIT 10;

SELECT g.name Genero, COUNT(s.idSong) Reproducciones FROM practica1.genre g
JOIN practica1.song s ON s.Genre_idGenre = g.idGenre
GROUP BY g.idGenre
ORDER BY COUNT(s.idSong) DESC
LIMIT 5;

SELECT g.name, (
     SELECT COUNT(s.Genre_idGenre) cantidad FROM practica1.Song s
     GROUP BY s.Genre_idGenre
     HAVING s.Genre_idGenre = g.idGenre
    ORDER BY COUNT(s.Genre_idGenre) DESC LIMIT 1
) as mayorReproduccion FROM practica1.Genre g
GROUP BY g.name
ORDER BY mayorReproduccion DESC;

SELECT g.name, (
     SELECT a.name FROM practica1.Song s
     JOIN practica1.artist a ON s.Artist_idArtist = a.idArtist
     GROUP BY s.Genre_idGenre
     HAVING s.Genre_idGenre = g.idGenre
    ORDER BY COUNT(s.Genre_idGenre) DESC LIMIT 1
) as artista FROM practica1.Genre g
GROUP BY g.name;

SELECT s.year, (
     SELECT s.name FROM practica1.Song s1
     GROUP BY s1.year
     HAVING s.year = s1.year
    ORDER BY COUNT(*) DESC LIMIT 1
) as artista FROM practica1.Song s
GROUP BY s.year
ORDER BY s.year
;


SELECT a.name FROM practica1.Song s
JOIN practica1.artist a ON a.idArtist = s.Artist_idArtist
GROUP BY s.Artist_idArtist
ORDER BY COUNT(*) DESC
LIMIT 10;

SELECT s.name Cancion, COUNT(s.name) Reproducciones FROM practica1.song s
WHERE s.explicit = 1
GROUP BY s.name, s.Artist_idArtist
ORDER BY COUNT(s.name) DESC
LIMIT 1;
