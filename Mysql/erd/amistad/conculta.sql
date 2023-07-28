use asignacion_1;

select *
from users;

-- Creando usuarios

-- usuario 1
INSERT INTO users(id_users,first_name,last_name,created_at,updated_at)
VALUES(1,'Hinata','Hyuga',now(),now());

-- usuario 2
INSERT INTO users(id_users,first_name,last_name,created_at,updated_at)
VALUES(2,'Shino','Aburame',now(),now());

-- usuario 3
INSERT INTO users(id_users,first_name,last_name,created_at,updated_at)
VALUES(3,'kiba','inosuka',now(),now());

-- usuario 4
INSERT INTO users(id_users,first_name,last_name,created_at,updated_at)
VALUES(4,'Shimakaru','Nara',now(),now());

-- usuario 5
INSERT INTO users(id_users,first_name,last_name,created_at,updated_at)
VALUES(5,'Ino','Yamanaka',now(),now());

-- usuario 6
INSERT INTO users(id_users,first_name,last_name,created_at,updated_at)
VALUES(6,'Choji','Akimichi',now(),now());

-- haz que el usuario 1 sea amigo del usuario 2, 4 y 6

SELECT *
FROM friendships;

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(1,NOW(),NOW(),1,2);

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(2,NOW(),NOW(),1,4);

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(3,NOW(),NOW(),1,6);

SELECT *
FROM friendships
WHERE users_id_users = 1;

-- haz que el usuario 2 sea amigo del usuario 1, 3 y 5

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(4,NOW(),NOW(),2,1);

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(5,NOW(),NOW(),2,3);

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(6,NOW(),NOW(),2,5);

SELECT *
FROM friendships
WHERE users_id_users = 2;

-- haz que el usuario 3 sea amigo del usuario 2 y 5

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(7,NOW(),NOW(),3,2);

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(8,NOW(),NOW(),3,5);

SELECT *
FROM friendships
WHERE users_id_users = 3;

--  haz que el usuario 4 sea amigo del usuario 3

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(9,NOW(),NOW(),4,3);

SELECT *
FROM friendships
WHERE users_id_users = 4;

-- haz que el usuario 5 sea amigo del usuario 1 y 6

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(10,NOW(),NOW(),5,1);

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(11,NOW(),NOW(),5,6);

SELECT *
FROM friendships
WHERE users_id_users = 5;

-- haz que el usuario 6 sea amigo del usuario 2 y 3

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(12,NOW(),NOW(),6,2);

INSERT INTO friendships(id_friendships,creted_at,updated_at,users_id_users,users_id_users1)
VALUES(13,NOW(),NOW(),6,3);

SELECT *
FROM friendships
WHERE users_id_users = 6;

-- Devuelve todos los usuarios que son amigos del primer usuario, asegúrate de que sus nombres se muestren en los resultados.

SELECT  users_id_users
FROM friendships
WHERE users_id_users1 = 1;

SELECT first_name
FROM users
WHERE id_users = 2;

SELECT first_name
FROM users_id 
WHERE id_users = 5;
