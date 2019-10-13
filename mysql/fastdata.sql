create database if not exists fiapdb;
use fiapdb;
create table aluno (id INT(6) PRIMARY KEY, name VARCHAR(30) NOT NULL, idade int(2));
insert into aluno values (1, "Jose", 55);
insert into aluno values (2, "Raimundo", 65);
insert into aluno values (3, "Geraldo", 57);
insert into aluno values (4, "Francisco", 58);
