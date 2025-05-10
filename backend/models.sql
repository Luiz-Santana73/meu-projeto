DROP TABLE IF EXISTS producao;

CREATE TABLE producao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    unidade TEXT NOT NULL,
    meta REAL NOT NULL,
    realizado REAL NOT NULL
);
