-- SQL Style Guide: https://www.sqlstyle.guide/

CREATE TABLE warehouses (
    id        INTEGER NOT NULL,
    name      TEXT    NOT NULL,
    latitude  REAL    NOT NULL,
    longitude REAL    NOT NULL,
    PRIMARY KEY(id)
);
