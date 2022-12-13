USE `practica1`;

INSERT INTO `practica1`.`artist` (`name`) SELECT DISTINCT t.artist FROM practica1.temporal t;
INSERT INTO `practica1`.`genre` (`name`) SELECT DISTINCT t.genre FROM practica1.temporal t;
INSERT INTO `practica1`.`song`
(`energy`,
`name`,
`durationMs`,
`year`,
`popularity`,
`danceability`,
`llave`,
`loudness`,
`mode`,
`speechiness`,
`accousticness`,
`instrumentalness`,
`liveness`,
`valence`,
`tempo`,
`Artist_idArtist`,
`Genre_idGenre`)
SELECT
	t.energy,
	t.song,
    t.duration_ms,
    t.year,
    t.popularity,
    t.danceability,
    t.llave,
    t.loudness,
    t.mode,
    t.speechiness,
    t.acousticness,
    t.instrumentalness,
    t.liveness,
    t.valence,
    t.tempo,
	a.idArtist,
    g.idGenre
FROM practica1.temporal t
LEFT JOIN artist a ON a.name = t.artist
LEFT JOIN genre g ON g.name = t.genre;