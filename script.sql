--1 SQL statement 
SELECT p_Name, nationalNumber
from pokemon;

--2 SQL statement
SELECT p_Name
from pokemon
where p_Name = 'pikachu';

--3 SQL statement
SELECT p_Name
from pokemon
where nationalNumber = '1';

--4 SQL statement
SELECT p_Name
from pokemon
INNER JOIN basestats on p_Name = b_Name
where hp = '45';

--5 SQL statement
SELECT *
from pokemon;

--6 SQL statement
SELECT br_Name, eggGroupOne, eggGroupTwo
from breed
where eggGroupOne = 'dragon';

--7 SQL statement
SELECT type_Name
from typedefenses
where fire = '0.5';

--8 SQL statement
SELECT typeOne, count(*)
from pokemon
group by typeOne;

--9 SQL statement
SELECT p_Name, catchRate, typeOne
from pokemon
INNER JOIN train on train_Name = p_Name
where catchRate = 45
and typeOne = 'grass';

--10 SQL statement
SELECT b_Name, attack, spAttack
from basestats
where attack > 60 and spAttack > 60;

--11 SQL statement
SELECT train_Name, evYield, hp
from train
INNER JOIN basestats on train_Name = b_Name
where hp = 45
and evYield = '1 Special Attack';

--12 SQL statement
INSERT INTO pokemonAbility(p_Name, a_name)
VALUES('blastoise', 'Torrent'); 

--13 SQL statement
SELECT p_Name, a_name
from pokemonAbility 
where p_Name = 'blastoise';

--14 SQL statement
DELETE
from pokemonAbility
where p_Name = 'blastoise';

--15 SQL statement
INSERT INTO pokemonMoves(pm_Name, m_Name)
VALUES('bulbasaur', 'Absorb'); 

--16 SQL statement
SELECT pm_Name 
FROM pokemonMoves
WHERE m_Name = 'Absorb';

--17 SQL statement
DELETE
from pokemonMoves
where m_Name = 'Absorb'
and pm_Name = 'bulbasaur';

--18 SQL statement
SELECT p_Name
from pokemon
where p_Name like 'a%';

--19 SQL statement
SELECT p_Name
FROM pokemon
WHERE typeOne = 'fire' and typeTwo is NULL;

--20 SQL statement
UPDATE pokemon
SET typeOne = 'dark', typeTwo = 'normal'
WHERE p_Name = 'raticate';