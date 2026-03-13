import sqlite3
import os
import json
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'placement.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            student_name TEXT,
            cgpa REAL,
            internships INTEGER,
            projects INTEGER,
            workshops INTEGER,
            aptitude_score REAL,
            ssc_marks REAL,
            hsc_marks REAL,
            backlogs INTEGER,
            probability REAL,
            risk_score REAL,
            category TEXT,
            prediction TEXT,
            recommendations TEXT,
            feature_importance TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS model_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            model_name TEXT,
            accuracy REAL,
            precision_score REAL,
            recall REAL,
            f1_score REAL,
            is_best INTEGER DEFAULT 0
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS improvement_tracker (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            student_name TEXT,
            before_score REAL,
            after_score REAL,
            new_prediction TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_tracker_entry(student_name, before, after, prediction, notes=""):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO improvement_tracker (timestamp, student_name, before_score, after_score, new_prediction, notes)
        VALUES (?,?,?,?,?,?)
    ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), student_name, before, after, prediction, notes))
    conn.commit()
    conn.close()

def get_tracker_entries():
    conn = get_connection()
    c = conn.cursor()
