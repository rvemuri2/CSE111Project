CREATE TABLE pokemon (
    p_Name  varchar(25) not null,
    nationalNumber int not null,
    p_Description varchar(120) not null,
    typeOne varchar(15) not null,
    typeTwo varchar(15),
    generation int not null
);

CREATE TABLE breed (
    br_Name  varchar(25) not null,
    eggGroupOne varchar(15) not null,
    eggGroupTwo varchar(15),
    genderFemale_Percent float,
    genderMale_Percent float,
    eggCycle int not null
);

CREATE TABLE ability (
    a_Name varchar(25) not null,
    a_Description varchar(120) not null
);

CREATE TABLE train (
    train_Name varchar(25) not null,
    evYield varchar(25) not null,
    catchRate int not null,
    baseFriendship int not null,
    baseExperience int not null,
    growthRate varchar(25) not null
);

CREATE TABLE typedefenses (
    type_Name varchar(25) not null,
    water float not null,
    electric float not null,
    fire float not null,
    grass float not null,
    ice float not null,
    fighting float not null,
    poison float not null,
    ground float not null,
    flying float not null,
    psychic float not null,
    bug float not null,
    rock float not null,
    ghost float not null,
    fairy float not null,
    dragon float not null,
    dark float not null,
    steel float not null,
    normal float not null
);

CREATE TABLE moves (
    type varchar(20) not null,
    m_Name varchar(40) not null,
    power int,
    category varchar(25),
    effect varchar(120),
    PP int not null,
    accuracy int
);

CREATE TABLE basestats (
    b_Name varchar(25) not null,
    attack int not null,
    defense int not null,
    hp int not null,
    speed int not null,
    spDefense int not null,
    spAttack int not null,
    total int not null
);

INSERT INTO pokemon(p_Name,nationalNumber,typeOne,typeTwo,generation,p_Description)
VALUES('bulbasaur',1,'grass','poison',1,'For some time after its birth, it grows by taking nourishment from the seed on its back.'),
('',2,'','',1,'');