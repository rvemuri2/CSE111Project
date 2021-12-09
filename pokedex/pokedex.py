import sqlite3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query

app = Flask(__name__)
conn = sqlite3.connect('database.sqlite',check_same_thread=False)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

db = SQLAlchemy(app)

@app.route('/', methods = ['GET'])
def home():
   return render_template('homePokedex.html')

@app.route('/pokeName/<string:name>')
def pokeName(name):
    query = f"""SELECT p_Name
                FROM pokemon
                WHERE p_Name = "{name}"
                ;"""
    cur = conn.cursor()
    nam = cur.execute(query).fetchall()

    query = f"""SELECT nationalNumber,typeOne,typeTwo,generation,p_Description
                FROM pokemon
                WHERE p_Name = "{name}"
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()

    query = f"""SELECT ability.a_Name, a_Description
                FROM ability, pokemon, pokemonAbility
                WHERE pokemon.p_Name = "{name}"
                and pokemon.p_Name = pokemonAbility.p_Name
                and pokemonAbility.a_Name = ability.a_Name
                ;"""
    cur = conn.cursor()
    result1 = cur.execute(query).fetchall()

    query = f"""SELECT attack,defense,hp,speed,spDefense,spAttack,total
                FROM baseStats, pokemon
                WHERE p_Name = "{name}"
                and p_Name = b_Name
                ;"""
    cur = conn.cursor()
    result2 = cur.execute(query).fetchall()

    query = f"""SELECT evYield,catchRate,baseFriendship,baseExperience,growthRate
                FROM train, pokemon
                WHERE p_Name = "{name}"
                and p_Name = train_Name
                ;"""
    cur = conn.cursor()
    result3 = cur.execute(query).fetchall()

    query = f"""SELECT eggGroupOne,eggGroupTwo,genderMale_Percent,genderFemale_Percent,eggCycle
                FROM breed, pokemon
                WHERE p_Name = "{name}"
                and p_Name = br_Name
                ;"""
    cur = conn.cursor()
    result4 = cur.execute(query).fetchall()

    query = f"""SELECT normal,fire,water,electric,grass,ice,fighting,poison,ground,flying,psychic,bug,rock,ghost,dragon,dark,steel,fairy
                FROM typeDefenses, pokemon
                WHERE p_Name = "{name}"
                and p_Name = type_Name
                ;"""
    cur = conn.cursor()
    result5 = cur.execute(query).fetchall()

    query = f"""SELECT moves.m_Name,type,category,power,accuracy,PP,effect
                FROM moves, pokemon, pokemonMoves
                WHERE pokemon.p_Name = "{name}"
                and pokemon.p_Name = pokemonMoves.pm_Name
                and pokemonMoves.m_Name = moves.m_Name
                ;"""
    cur = conn.cursor()
    result6 = cur.execute(query).fetchall()

    return render_template('pokePage.html', name = nam,results = result, results1 = result1, results2 = result2, results3 = result3, results4 = result4, results5 = result5, results6 = result6)

@app.route('/pokemonName', methods = ['POST'])
def pokemonName():
    pokeNam = request.form['PokeName']

    query = f"""SELECT p_Name
                FROM pokemon
                WHERE p_Name = "{pokeNam}"
                ;"""
    cur = conn.cursor()
    nam = cur.execute(query).fetchall()

    query = f"""SELECT nationalNumber,typeOne,typeTwo,generation,p_Description
                FROM pokemon
                WHERE p_Name = "{pokeNam}"
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()

    query = f"""SELECT ability.a_Name, a_Description
                FROM ability, pokemon, pokemonAbility
                WHERE pokemon.p_Name = "{pokeNam}"
                and pokemon.p_Name = pokemonAbility.p_Name
                and pokemonAbility.a_Name = ability.a_Name
                ;"""
    cur = conn.cursor()
    result1 = cur.execute(query).fetchall()

    query = f"""SELECT attack,defense,hp,speed,spDefense,spAttack,total
                FROM baseStats, pokemon
                WHERE p_Name = "{pokeNam}"
                and p_Name = b_Name
                ;"""
    cur = conn.cursor()
    result2 = cur.execute(query).fetchall()

    query = f"""SELECT evYield,catchRate,baseFriendship,baseExperience,growthRate
                FROM train, pokemon
                WHERE p_Name = "{pokeNam}"
                and p_Name = train_Name
                ;"""
    cur = conn.cursor()
    result3 = cur.execute(query).fetchall()

    query = f"""SELECT eggGroupOne,eggGroupTwo,genderMale_Percent,genderFemale_Percent,eggCycle
                FROM breed, pokemon
                WHERE p_Name = "{pokeNam}"
                and p_Name = br_Name
                ;"""
    cur = conn.cursor()
    result4 = cur.execute(query).fetchall()

    query = f"""SELECT normal,fire,water,electric,grass,ice,fighting,poison,ground,flying,psychic,bug,rock,ghost,dragon,dark,steel,fairy
                FROM typeDefenses, pokemon
                WHERE p_Name = "{pokeNam}"
                and p_Name = type_Name
                ;"""
    cur = conn.cursor()
    result5 = cur.execute(query).fetchall()

    query = f"""SELECT moves.m_Name,type,category,power,accuracy,PP,effect
                FROM moves, pokemon, pokemonMoves
                WHERE pokemon.p_Name = "{pokeNam}"
                and pokemon.p_Name = pokemonMoves.pm_Name
                and pokemonMoves.m_Name = moves.m_Name
                ;"""
    cur = conn.cursor()
    result6 = cur.execute(query).fetchall()

    return render_template('pokePage.html', name = nam,results = result, results1 = result1, results2 = result2, results3 = result3, results4 = result4, results5 = result5, results6 = result6)

@app.route('/pokemonNumber', methods = ['POST'])
def pokemonNumber():
    pokeNum = request.form['PokeNumber']

    query = f"""SELECT p_Name
                FROM pokemon
                WHERE nationalNumber = "{pokeNum}"
                ;"""
    cur = conn.cursor()
    nam = cur.execute(query).fetchall()

    query = f"""SELECT nationalNumber,typeOne,typeTwo,generation,p_Description
                FROM pokemon
                WHERE nationalNumber = "{pokeNum}"
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()

    query = f"""SELECT ability.a_Name, a_Description
                FROM ability, pokemon, pokemonAbility
                WHERE nationalNumber = "{pokeNum}"
                and pokemon.p_Name = pokemonAbility.p_Name
                and pokemonAbility.a_Name = ability.a_Name
                ;"""
    cur = conn.cursor()
    result1 = cur.execute(query).fetchall()

    query = f"""SELECT attack,defense,hp,speed,spDefense,spAttack,total
                FROM baseStats, pokemon
                WHERE nationalNumber = "{pokeNum}"
                and p_Name = b_Name
                ;"""
    cur = conn.cursor()
    result2 = cur.execute(query).fetchall()

    query = f"""SELECT evYield,catchRate,baseFriendship,baseExperience,growthRate
                FROM train, pokemon
                WHERE nationalNumber = "{pokeNum}"
                and p_Name = train_Name
                ;"""
    cur = conn.cursor()
    result3 = cur.execute(query).fetchall()

    query = f"""SELECT eggGroupOne,eggGroupTwo,genderMale_Percent,genderFemale_Percent,eggCycle
                FROM breed, pokemon
                WHERE nationalNumber = "{pokeNum}"
                and p_Name = br_Name
                ;"""
    cur = conn.cursor()
    result4 = cur.execute(query).fetchall()

    query = f"""SELECT normal,fire,water,electric,grass,ice,fighting,poison,ground,flying,psychic,bug,rock,ghost,dragon,dark,steel,fairy
                FROM typeDefenses, pokemon
                WHERE nationalNumber = "{pokeNum}"
                and p_Name = type_Name
                ;"""
    cur = conn.cursor()
    result5 = cur.execute(query).fetchall()

    query = f"""SELECT moves.m_Name,type,category,power,accuracy,PP,effect
                FROM moves, pokemon, pokemonMoves
                WHERE nationalNumber = "{pokeNum}"
                and pokemon.p_Name = pokemonMoves.pm_Name
                and pokemonMoves.m_Name = moves.m_Name
                ;"""
    cur = conn.cursor()
    result6 = cur.execute(query).fetchall()

    return render_template('pokePage.html', name = nam,results = result, results1 = result1, results2 = result2, results3 = result3, results4 = result4, results5 = result5, results6 = result6)

@app.route('/pokemonType', methods = ['POST'])
def pokemonType():
    pokeType = request.form['PokeType']

    query = f"""SELECT p_Name, nationalNumber,typeOne,typeTwo,p_Description
                FROM pokemon
                WHERE typeOne = "{pokeType}"
                or typeTwo = "{pokeType}"
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()

    return render_template('pokeList.html', name = pokeType, results = result)

@app.route('/pokemonAbility', methods = ['POST'])
def pokemonAbility():
    pokeAbility = request.form['PokeAbility']

    query = f"""SELECT pokemon.p_Name, nationalNumber,typeOne,typeTwo,p_Description
                FROM pokemon, ability, pokemonAbility
                WHERE ability.a_Name = "{pokeAbility}"
                and pokemonAbility.a_Name = ability.a_Name
                and pokemon.p_Name = pokemonAbility.p_Name
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
    return render_template('pokeList.html', name = pokeAbility, results = result)

@app.route('/pokemonMoveBreed', methods = ['POST'])
def pokemonMoveBreed():
    pokeMove = request.form['PokeMove']
    pokeEgg = request.form['PokeEgg']

    query = f"""SELECT pokemon.p_Name, nationalNumber,eggGroupOne,eggGroupTwo,p_Description
                FROM pokemon, breed, pokemonMoves, moves
                WHERE moves.m_Name = "{pokeMove}"
                and pokemonMoves.m_Name = moves.m_Name
                and pokemon.p_Name = pokemonMoves.pm_Name
                and pokemon.p_Name = br_Name
                and eggGroupOne = "{pokeEgg}"
                UNION
                SELECT pokemon.p_Name, nationalNumber,eggGroupOne,eggGroupTwo,p_Description
                FROM pokemon, breed, pokemonMoves, moves
                WHERE moves.m_Name = "{pokeMove}"
                and pokemonMoves.m_Name = moves.m_Name
                and pokemon.p_Name = pokemonMoves.pm_Name
                and pokemon.p_Name = br_Name
                and eggGroupTwo = "{pokeEgg}"
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
    return render_template('pokeList1.html',name = pokeMove, name1 = pokeEgg, results = result)

@app.route('/allpokemon', methods = ['POST'])
def allpokemon():
    query = f"""SELECT *
                FROM pokemon
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()

    return render_template('pokeList.html', name = 'All Pokemon', results = result)

@app.route('/pokemonAbilityStats', methods = ['POST'])
def pokemonAbilityStats():
    pokeAbility = request.form['PokeAbility']
    pokeTotal = request.form['PokeTotal']
    pokeAttack = request.form['PokeAttack']

    query = f"""SELECT pokemon.p_Name, nationalNumber,attack,total,p_Description
                FROM pokemon, baseStats, pokemonAbility, ability
                WHERE ability.a_Name = "{pokeAbility}"
                and pokemonAbility.a_Name = ability.a_Name
                and pokemon.p_Name = pokemonAbility.p_Name
                and pokemon.p_Name = b_Name
                and attack > "{pokeAttack}"
                and total > "{pokeTotal}"
                ;"""
    cur = conn.cursor()
    result = cur.execute(query).fetchall()

    return render_template('pokelist2.html', name = pokeAbility, name1 = pokeTotal, name2 = pokeAttack, results = result)

if __name__ == '__main__':
   app.run(debug = True)