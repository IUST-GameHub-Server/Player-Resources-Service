import sqlite3

class DataAccess:
    def create_user(email):
        conn=sqlite3.connect('./PlayerResourcesService/DataLayer/resources.db')
        cur=conn.cursor()
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS resources(
                    email TEXT PRIMARY KEY,
                    coins INT,
                    gems INT,
                    tickets INT
        );
        """)

        cur.execute(f"""
        INSERT INTO resources(email, coins, gems, tickets) VALUES('{email}', {0},{0},{0});
        """)
        conn.commit()
        return "user created successfully"
    
    def set_gems(email,gems):
        conn=sqlite3.connect('./PlayerResourcesService/DataLayer/resources.db')
        cur=conn.cursor()
        cur.execute(f"""
        UPDATE resources SET gems = '{gems}' WHERE email='{email}'
        """)

    def set_coins(email,coins):
        conn=sqlite3.connect('./PlayerResourcesService/DataLayer/resources.db')
        cur=conn.cursor()
        cur.execute(f"""
        UPDATE resources SET coins = '{coins}' WHERE email='{email}'
        """)

    def set_tickets(email,tickets):
        conn=sqlite3.connect('./PlayerResourcesService/DataLayer/resources.db')
        cur=conn.cursor()
        cur.execute(f"""
        UPDATE resources SET tickets = '{tickets}' WHERE email='{email}'
        """)

    def get_gems(email):
        conn=sqlite3.connect('./PlayerResourcesService/DataLayer/resources.db')
        cur=conn.cursor()
        cur.execute(f"""
        SELECT gems FROM progress where email='{email}'
        """)
        return cur.fetchone()
    
    def get_coins(email):
        conn=sqlite3.connect('./PlayerResourcesService/DataLayer/resources.db')
        cur=conn.cursor()
        cur.execute(f"""
        SELECT coins FROM progress where email='{email}'
        """)
        return cur.fetchone()
    
    def get_tickets(email):
        conn=sqlite3.connect('./PlayerResourcesService/DataLayer/resources.db')
        cur=conn.cursor()
        cur.execute(f"""
        SELECT tickets FROM progress where email='{email}'
        """)
        return cur.fetchone()
    
    