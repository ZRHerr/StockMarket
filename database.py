import sqlite3

# Open database
conn = sqlite3.connect("database.db")

# Create table
conn.execute(
    """CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)"""
)

conn.execute(
    """CREATE TABLE symbols
		(symbolId TEXT PRIMARY KEY,
		name TEXT,
		currentPrice REAL,
        openPrice REAL,
        closePrice REAL,
        percentageChange REAL,
		description TEXT,
		image TEXT,
		)"""
)

conn.execute(
    """CREATE TABLE watchList
		(userId INTEGER,
		symbolId TEXT,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(symbolId) REFERENCES symbols(symbolId)
		)"""
)


conn.close()
