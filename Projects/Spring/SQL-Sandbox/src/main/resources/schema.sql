USE Userbase;
CREATE TABLE IF NOT EXISTS Users
(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    salary int,
    PRIMARY KEY (id)
);
