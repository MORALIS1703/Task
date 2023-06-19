import csv
import json
import pandas as pd
import psycopg2
import config
INDEX = "posts"

def postgres_insert_logic(file_name: str):
    conn = psycopg2.connect(config.DATABASE_URL)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS posts;")
    cur.execute("""CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        rubrics text[] NOT NULL,
        text text NOT NULL,
        created_date date NOT NULL
    )
    """)

    with open(file_name, 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            sql = "INSERT INTO posts (rubrics, text, created_date) VALUES  (%s, %s, %s)"
            cur.execute(sql, (eval(row[2]), row[0], row[1]))

    conn.commit()
    print("Успешно записал данные в postgres")


def main():
    file_name = "./posts.csv"
    postgres_insert_logic(file_name)


if __name__ == "__main__":
    main()
