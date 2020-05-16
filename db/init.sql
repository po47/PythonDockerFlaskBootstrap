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
    ('Paul','       "M"',   20,       74,      170),
    ('Bill','       "M"',   23,       68,      166),
    ('Joey','       "M"',   25,       70,      155),
    ('Luna','       "F"',   19,       72,      167),
    ('Juan','       "M"',   27,       66,      124),
    ('Tony','       "F"',   18,       66,      115),
    ('Gwen','       "F"',   16,       64,      111),
    ('Adam','       "M"',   25,       71,      158),
    ('Alan','       "M"',   17,       72,      175),
    ('King','       "M"',   30,       69,      143),
    ('Jade','       "F"',   21,       69,      120),
    ('Luke','       "M"',   24,       72,      163),
    ('Myra','       "F"',   23,       62,       98),
    ('Neil','       "M"',   26,       75,      160),
    ('Levi','       "M"',   29,       70,      145),
    ('Page','       "F"',   31,       67,      125),
    ('Quin','       "M"',   26,       71,      176),
    ('Lexi','       "F"',   21,       65,      100);