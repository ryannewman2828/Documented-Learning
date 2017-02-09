CREATE TABLE IF NOT EXISTS Users
(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    salary int NOT NULL,
    grade int CHECK (grade >= 0 && grade <= 100),
    pass bit NOT NULL,
    PRIMARY KEY (id)
);
