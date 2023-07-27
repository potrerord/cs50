-- SQL Style Guide: https://www.sqlstyle.guide/

CREATE TABLE warehouses (
    id        INTEGER NOT NULL AUTOINCREMENT,
    name      TEXT    NOT NULL,
    latitude  REAL    NOT NULL,
    longitude REAL    NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE inventories (
    warehouse_id INTEGER NOT NULL,
    item_id      INTEGER NOT NULL,
    quantity     INTEGER NOT NULL,
    PRIMARY KEY (warehouse_id, item_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

CREATE TABLE items (
    id           INTEGER NOT NULL AUTOINCREMENT,
    name         TEXT    NOT NULL,
    PRIMARY KEY (id)
);
