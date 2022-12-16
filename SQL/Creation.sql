
CREATE TABLE IF NOT EXISTS practica1.Artist (
  idArtist INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NULL,
  PRIMARY KEY (idArtist));

CREATE TABLE IF NOT EXISTS practica1.Genre (
  idGenre INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NULL,
  PRIMARY KEY (idGenre));

CREATE TABLE IF NOT EXISTS practica1.Song (
  idSong INT NOT NULL AUTO_INCREMENT,
  energy DECIMAL(10,4) NULL,
  name VARCHAR(200) NOT NULL,
  durationMs INT NULL,
  year INT NULL,
  explicit tinyint DEFAULT NULL,
  popularity DECIMAL(10,4) NULL,
  danceability DECIMAL(10,4) NULL,
  llave INT NULL,
  loudness DECIMAL(10,4) NULL,
  mode DECIMAL(10,4) NULL,
  speechiness DECIMAL(10,4) NULL,
  accousticness DECIMAL(10,4) NULL,
  instrumentalness DECIMAL(10,7) NULL,
  liveness DECIMAL(10,4) NULL,
  valence DECIMAL(10,4) NULL,
  tempo DECIMAL(10,4) NULL,
  Artist_idArtist INT NOT NULL,
  Genre_idGenre INT NOT NULL,
  PRIMARY KEY (idSong),
  INDEX fk_Song_Artist_idx (Artist_idArtist ASC) VISIBLE,
  INDEX fk_Song_Genre1_idx (Genre_idGenre ASC) VISIBLE,
  CONSTRAINT fk_Song_Artist
    FOREIGN KEY (Artist_idArtist)
    REFERENCES practica1.Artist (idArtist)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Song_Genre1
    FOREIGN KEY (Genre_idGenre)
    REFERENCES practica1.Genre (idGenre)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS practica1.temporal (
  artist VARCHAR(50) NULL DEFAULT NULL,
  song VARCHAR(500) NULL DEFAULT NULL,
  duration_ms INT NULL DEFAULT NULL,
  explicit BIT(1) NULL DEFAULT NULL,
  year INT NULL DEFAULT NULL,
  popularity DECIMAL(10,4) NULL DEFAULT NULL,
  danceability DECIMAL(10,4) NULL DEFAULT NULL,
  energy DECIMAL(10,4) NULL DEFAULT NULL,
  llave INT NULL DEFAULT NULL,
  loudness DECIMAL(10,4) NULL DEFAULT NULL,
  mode DECIMAL(10,4) NULL DEFAULT NULL,
  speechiness DECIMAL(10,4) NULL DEFAULT NULL,
  acousticness DECIMAL(10,4) NULL DEFAULT NULL,
  instrumentalness DECIMAL(10,7) NULL DEFAULT NULL,
  liveness DECIMAL(10,4) NULL DEFAULT NULL,
  valence DECIMAL(10,4) NULL DEFAULT NULL,
  tempo DECIMAL(10,4) NULL DEFAULT NULL,
  genre VARCHAR(50) NULL DEFAULT NULL);
