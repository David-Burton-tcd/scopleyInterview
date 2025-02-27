DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS leaderboard;

CREATE TABLE player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK (length(name) <= 20),
    gold FLOAT DEFAULT 0 CHECK (gold <= 1000000000.0),
    attack_value INT DEFAULT 10,
    max_health INT DEFAULT 100,
    luck INT DEFAULT 5,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (name)
);

CREATE TABLE leaderboard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position INTEGER NOT NULL,
    player_name TEXT NOT NULL,
    gold_taken FLOAT NOT NULL
);