CREATE DATABASE bioData;
use bioData;

CREATE TABLE IF NOT EXISTS biostats (
    `id` INT AUTO_INCREMENT,
    `YourName` VARCHAR(6) CHARACTER SET utf8,
    `Sex` VARCHAR(10) CHARACTER SET utf8,
    `Age` INT,
    `Height_in` INT,
    `Weight_lbs` INT,
    PRIMARY KEY(`id`)

);
INSERT INTO biostats (YourName,Sex,Age,Height_in,Weight_lbs) VALUES
    ('Julian','       "M"',   41,       74,      170),
    ('Jake','       "M"',   42,       68,      166),
    ('Jocelyn','       "F"',   32,       70,      155),
    ('Jennifer','       "F"',   39,       72,      167),
    ('Kim','       "F"',   30,       66,      124),
    ('Luna','       "F"',   33,       66,      115),
    ('Teresa','       "F"',   26,       64,      121),
    ('Caitlyn','       "F"',   30,       71,      158),
    ('Juan','       "M"',   53,       72,      175),
    ('Jacob','       "M"',   32,       69,      143),
    ('Justin','       "M"',   47,       69,      139),
    ('Jaime','       "F"',   34,       72,      163),
    ('Juliana','       "F"',   23,       62,       98),
    ('Jasmine','       "F"',   36,       75,      160),
    ('Valetina','       "F"',   38,       70,      145),
    ('Jason','       "M"',   31,       67,      135),
    ('Valeria','       "F"',   29,       71,      176),
    ('Brittany','       "F"',   28,       65,      131);
