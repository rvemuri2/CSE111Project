CREATE TABLE pokemon (
    p_Name  varchar(25) PRIMARY KEY,
    nationalNumber int not null,
    typeOne varchar(15) not null,
    typeTwo varchar(15),
    generation int not null,
    p_Description varchar(120) not null
);

CREATE TABLE breed (
    br_Name  varchar(25) not null,
    eggGroupOne varchar(15) not null,
    eggGroupTwo varchar(15),
    genderMale_Percent float,
    genderFemale_Percent float,
    eggCycle int not null,
    FOREIGN KEY(br_Name) REFERENCES pokemon(p_Name)
);

CREATE TABLE ability (
    a_Name varchar(25) PRIMARY KEY,
    a_Description varchar(120) not null
);

CREATE TABLE pokemonAbility (
  p_Name varchar(30), 
  a_Name varchar(30),
  FOREIGN KEY(p_Name) REFERENCES pokemon(p_Name),
  FOREIGN KEY(a_Name) REFERENCES ability(a_Name)
);

CREATE TABLE pokemonMoves (
  pm_Name varchar(30), 
  m_Name varchar(30),
  FOREIGN KEY(pm_Name) REFERENCES pokemon(p_Name),
  FOREIGN KEY(m_Name) REFERENCES moves(m_Name)
);

CREATE TABLE train (
    train_Name varchar(25) not null,
    evYield varchar(25) not null,
    catchRate int not null,
    baseFriendship int not null,
    baseExperience int not null,
    growthRate varchar(25) not null,
    FOREIGN KEY(train_Name) REFERENCES pokemon(p_Name)
);

CREATE TABLE typeDefenses (
    type_Name varchar(25) not null,
    normal float not null,
    fire float not null,
    water float not null,
    electric float not null,
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
    dragon float not null,
    dark float not null,
    steel float not null,
    fairy float not null,
    FOREIGN KEY(type_Name) REFERENCES pokemon(p_Name)
);

CREATE TABLE moves (
    m_Name varchar(40) PRIMARY KEY,
    type varchar(20) not null,
    category varchar(25),
    power int,
    accuracy int,
    PP int not null,
    effect varchar(120)
);

CREATE TABLE baseStats (
    b_Name varchar(25) not null,
    attack int not null,
    defense int not null,
    hp int not null,
    speed int not null,
    spDefense int not null,
    spAttack int not null,
    total int not null,
    FOREIGN KEY(b_Name) REFERENCES pokemon(p_Name)
);
