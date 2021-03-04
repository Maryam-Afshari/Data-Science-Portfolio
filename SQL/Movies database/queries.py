# pylint: disable=C0103
''' Complete each fonction with the right query '''
import sqlite3
conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

def directors_count(db):
    # return the number of directors contained in the database
    query = '''
            SELECT COUNT(*)
            FROM directors
    '''
    db.execute(query)
    directors = db.fetchone() # >> (4092,)
    return (directors[0]) 
    

def sorted_directors(db):
    # return the list of all the directors sorted in alphabetical order
    query = '''
            SELECT name
            FROM directors
            ORDER BY name
    '''
    db.execute(query)
    directors_list = db.fetchall() # >> [('Zoya Akhtar',),...]
      
    return [i[0] for i in directors_list] 


def love_movies(db):
    # return the list of all movies which contain the word "love" in their title, sorted in alphabetical order
    query = """
        SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '%love%'
        ORDER BY title
    """
    db.execute(request) 
    love_movies = db.fetchall() # >> [('A Short Film About Love',),('I think I love my wife',),...] 
    
    return [movie[0] for movie in love_movies]

 
def directors_with_name(db, name):
    # return the number of directors which contain a given word in their name
    query = """
        SELECT COUNT(*)
        FROM directors 
        WHERE name LIKE ?
    """
    db.execute(query, (f"%{name}%",))
    count = db.fetchone() # >> e.g. (131,)
    return count[0]

# print(directors_with_name(db,"John"))
  

def long_movies(db, min_length):
    # return this list of all movies which are longer than a given duration, sorted in the alphabetical order
    query = """
        SELECT title 
        FROM movies 
        WHERE minutes > ? 
        ORDER BY minutes ASC
    """
    db.execute(query,(min_length,)) # the second argument is passed in a tuple form with a comma
    movies = db.fetchall() # >> list of tuples 
    return [movie[0] for movie in movies]  

# print(long_movies(db, 300))    