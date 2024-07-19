import sqlite3

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO player (name, gold, attack_value, max_health, luck) VALUES (?, ?, ?, ?, ?)",
            ('ControlPlayer', 100, 10, 30, 5))

cur.execute("INSERT INTO player (name, gold, attack_value, max_health, luck) VALUES (?, ?, ?, ?, ?)",
            ('AggressivePlayer', 200, 20, 50, 8))

cur.execute("INSERT INTO player (name, gold, attack_value, max_health, luck) VALUES (?, ?, ?, ?, ?)",
            ('DefensivePlayer', 500, 5, 150, 6))

connection.commit()
connection.close()