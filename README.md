# LostPet
Типо проект для типо хакатона
Делается на Python 3.7.9 с использованием Django 3.2.8
В роли БД выступает PostgreSQL 12.8



Инфо для разработчиков:
Создать виртуальное окружение(гугл в помощь) и поставить в него обнову pip, django, и psycopg2

Перед стартом серва также следует создать бд введя следующие строки в запросник:
create database databases;
create user admin with password 'superpass123';
alter role admin set client_encoding to 'utf8';
alter role admin set default_transaction_isolation to 'read committed';
alter role admin set timezone to 'UTC';
 
 
 А ТАК ЖЕ СКОПИРОВАТЬ ФАЙЛ .gitignore И ВСТАВИТЬ ЕГО В СВОЙ ПРОЕКТ ТУДА ЖЕ ГДЕ ОН СТОИТ У МЕНЯ!!!!
 (кто закинет в репо хлам получит по жопе)
