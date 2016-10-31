#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3

class DatabaseConnector():

    
    def connectSQLiteDB(DBFileName):
        #Constructor with default values only
        # database creation
        try:
            conn = sqlite3.connect(DBFileName)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                timestamp TEXT,
                node_id TEXT,
                node_type TEXT,
                value REAL
                )""")
            conn.commit()
        except sqlite3.OperationalError:
            print('Warning : table already exists')
        except Exception as e:
            print("Erreur creation database")
            conn.rollback()
            # raise e
        return conn

