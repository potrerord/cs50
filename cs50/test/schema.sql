-- SQL Style Guide: https://www.sqlstyle.guide/

CREATE TABLE warehouses (
    id        INTEGER NOT NULL AUTOINCREMENT,
    name      TEXT    NOT NULL,
    latitude  REAL    NOT NULL,
    longitude REAL    NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE items (
    id           INTEGER NOT NULL AUTOINCREMENT,
    name         TEXT    NOT NULL,
    quantity     INTEGER NOT NULL,
    warehouse_id INTEGER NOT NULL,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(id),
    PRIMARY KEY (id, warehouse_id)
);

