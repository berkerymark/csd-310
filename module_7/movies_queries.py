import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "movies_user",
	"password": "popcorn",
	"host":"127.0.0.1",
	"database":"movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)

	print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

	input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("   The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_ERROR:
		print("   The spcified database does not exist")

	else:
		print(err)


cursor = db.cursor()

cursor.execute("SELECT studio_id, studio_name FROM studio")

studio = cursor.fetchall()

print("-- DISPLAYING Studio RECORDS --")

for studio in studio:
	print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


cursor.execute("SELECT genre_id, genre_name FROM genre")

genre = cursor.fetchall()

print("-- DISPLAYING Genre RECORDS --")

for genre in genre:
	print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))


cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

shortfilm = cursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --")

for shortfilm in shortfilm:
	print("Film Name: {}\nRuntime: {}\n".format(shortfilm[0], shortfilm[1]))


cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

director = cursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --")

for director in director:
	print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))#, director[2]))
	