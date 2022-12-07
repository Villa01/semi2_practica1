DROP_TABLES = 'DROP TABLE IF EXISTS TEMPORAL;'

TEMPORAL_CREATION = """CREATE TABLE TEMPORAL (
    artist VARCHAR(50),
    song VARCHAR(500),
    duration_ms INT,
    explicit BIT,
    year INT,
    popularity DECIMAL(10 , 4 ),
    danceability DECIMAL(10 , 4 ),
    energy DECIMAL(10 , 4 ),
    llave INT,
    loudness DECIMAL(10 , 4 ),
    mode DECIMAL(10 , 4 ),
    speechiness DECIMAL(10 , 4 ),
    acousticness DECIMAL(10 , 4 ),
    instrumentalness DECIMAL(10 , 7 ),
    liveness DECIMAL(10 , 4 ),
    valence DECIMAL(10 , 4 ),
    tempo DECIMAL(10 , 4 ),
    genre VARCHAR(50)
);"""

tables_to_create = (
    TEMPORAL_CREATION
)
