# CTI-110
# Austin Lee
# 11/19/2026
# My version of DHW1

import sqlite3

# Connect to SQLite database file (creates file if it doesn't exist)
conn = sqlite3.connect("signup_hw.db")
cursor = conn.cursor()

# Drop table so script can be re-run cleanly in class
cursor.execute("DROP TABLE IF EXISTS users")

# STUDENT CODE GOES IN THIS SECTION ONLY!!!
#--------------------------------------------------------------------------------------
# STEP 1: Create users table
# TO DO: Create a table called users with fields
# user_id, first_name, last_name, email, username, password_hash, signup_date, country, age
# I have started the table for you with the primary key 'user_id'
# NOTE: SQLite assigns user_id for you. You do not insert a value for it.
# NOTE: Do not put a comma after the LAST column in the table. A trailing comma is a syntax error.
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    username TEXT,
    password_hash TEXT,
    signup_date DATE,
    country TEXT,
    age INTEGER
)""")

# STEP 2: Insert sample fake users
# TO DO: Create a list called users that will store all 10 of your fake users information.
# I have started it for you
# Each user has 8 values, in this order (user_id is NOT included):
# first_name, last_name, email, username, password_hash, signup_date, country, age

users = [('Naruto', 'Uzamaki', 'ramen@example.com', 'naruto_u', 'LoveRamen1', '2026-06-01', 'JAPAN', 16),
    ('Rick', 'Sanchez', 'rick.sanchez@example.com', 'PortalRick', 'RickPortal123', '2024-01-15', 'USA', 70),
    ('Morty', 'Smith', 'morty.smith@example.com', 'MortyAdventures', 'MortyAdventure14', '2024-02-20', 'USA', 14),
    ('Peter', 'Griffin', 'peter.griffin@example.com', 'BigPGriffin', 'ChickenFight45', '2024-03-10', 'USA', 45),
    ('Stewie', 'Griffin', 'stewie.griffin@example.com', 'EvilGenius', 'WorldDomination1', '2024-04-05', 'USA', 1),
    ('Stan', 'Smith', 'stan.smith@example.com', 'CIAStan', 'CIAAgent2024', '2024-05-12', 'USA', 42),
    ('Eric', 'Cartman', 'eric.cartman@example.com', 'CartmanRules', 'RespectMyAuthoritah', '2024-06-18', 'USA', 10),
    ('BoJack', 'Horseman', 'bojack.horseman@example.com', 'BoJack2024', 'HollywooStar50', '2024-07-22', 'USA', 50),
    ('Bender', 'Rodriguez', 'bender.rodriguez@example.com', 'BendingUnit22', 'BiteMyShinyMetal', '2024-08-14', 'USA', 4),
    ('Bob', 'Belcher', 'bob.belcher@example.com', 'BurgerBob', 'BurgerOfTheDay', '2024-09-30', 'USA', 46)]


#------------------------------------------------------------------------------------
# DO NOT CODE PASS HERE!!!
# STEP 3: Run the python script! Once your done creating your table and adding in the user information
# You should run the program and it will create your database called signup_hw.db.
# You can then view it in your terminal and you can upload the .db file to a database viewer thats provided on Canvas.

cursor.executemany("""
INSERT INTO users (
    first_name, last_name, email, username, password_hash,
    signup_date, country, age
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", users)

conn.commit()
conn.close()

print("✅ signup_hw.db created with users table and sample data.")

print()

conn = sqlite3.connect("signup_hw.db")
cur = conn.cursor()
for row in cur.execute("SELECT * FROM users LIMIT 10"):
    print(row)
conn.close()