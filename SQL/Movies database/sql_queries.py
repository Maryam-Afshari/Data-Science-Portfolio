# pylint: disable=C0103, missing-docstring
import sqlite3
conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

def detailed_movies(db):
    # return the list of movies with their genres and director name.A list of tuple like(title,genre,name)
    query = """
        SELECT 
            movies.title,
            movies.genres, 
            directors.name
        FROM movies
        JOIN directors ON movies.director_id = directors.id
    """
    db.execute(query)
    movies = result.fetchall()
    return movies
    

def top_five_youngest_newly_directors(db):
    # return the top 5 youngest directors when they direct their first movie
    query = """
        SELECT 
           directors.name AS youngest_directors,
           (start_year) - (birth_year) AS director_age
        FROM directors
        JOIN movies ON directors.id = movies.director_id
        WHERE director_age IS NOT NULL
        ORDER BY director_age
        LIMIT 5  
    """    
    db.execute(query)
    youngest_directors = db.fetchall()
    return youngest_directors

def late_released_movies(db):
    # return the list of all movies released after their director death
    query = """
        SELECT movies.title AS unseen_movies  
        FROM movies
        JOIN directors ON directors.id = movies.director_id
        WHERE (movies.start_year) > (directors.death_year)
        ORDER BY unseen_movies 
    """
    db.execute(query)
    unseen_movies = db.fetchall()
    return [movie[0] for movie in unseen_movies]

def stats_on(db, genre_name):
    # return a dict of stats for a given genre
    query = """
        SELECT 
            movies.genres AS genre,
            COUNT(movies.id) AS number_of_movies,
            ROUND(AVG(movies.minutes),2) AS avg_length
        FROM movies
        WHERE genre = ? --use ? when you have two arguments passed to your function
    """
    db.execute(query, (genre_name,)) # use the second argument of execute function
    stats = db.fetchone() # >> ('Action,Adventure,Comedy', 153, 100.98) 
    return {
        "genre": stats[0], 
        "number_of_movies": stats[1],
        "avg_length": stats[2]
    }

def top_five_directors_for(db, genre_name):
    # return the top 5 of the directors with the most movies for a given genre
    query = """
        SELECT
            directors.name AS names,
            COUNT(movies.genres) AS count
        FROM directors -- doesnt matter which table to have in FROM clause
        JOIN movies ON directors.id = movies.director_id 
        WHERE movies.genres = ?
        GROUP BY names -- aggregate function is not allowed in the group by clause(you can not have count here)
        ORDER BY count DESC , names
        LIMIT 5
    """
    db.execute(query, (genre_name,))
    directors =db.fetchall()
    return directors
    
print(top_five_directors_for(db, "Action,Adventure,Comedy"))   


def movie_duration_buckets(db):
    # return the movie counts grouped by bucket of 30 min duration
    query = """
        SELECT
            (minutes / 30 + 1)*30 time_range,
            COUNT(*)
        FROM movies
        WHERE minutes IS NOT NULL
        GROUP BY time_range
    """ 
    return db.execute(query).fetchall()       


          
