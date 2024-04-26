import psycopg2
host = 'localhost'
user = 'postgres'
password = 'temur_1336'
database = 'n42'
port = 5432

conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = database,
    port = port
)

cur = conn.cursor()
#  Vazifa CRUD qilish

# create_new_table = """
# CREATE TABLE IF NOT EXISTS programming_languages(
#     id SERIAL PRIMARY KEY,
#     language_names VARCHAR(50) NOT NULL,
#     useges VARCHAR(100) NOT NULL

# )


# """
# cur.execute(create_new_table)
# conn.commit()

# ////////////////////////////////////////////////////////////////////////////
# Tablega ma'lumotlarni qushib chiqaamiz 
# insert_information_to_new_table = """
# INSERT INTO programming_languages(language_names,useges)
# VALUES ('Python','For  Research, Data Science, or Data Analytics'),
#        ('JavaScript','For Web Applications'),
#        ('Kotlin','For Writing Google Programs'),
#        ('C++','For Game Development'),
#        ('Java','Multiplatform Language'),
#        ('Go','For Large Projects')
       


# """
# cur.execute(insert_information_to_new_table)
# conn.commit()

# /////////////////////////////////////////////////////////////////////////////////
# Sql bazasiga kiritgan ma'lumotlarni chiqaramiz

# select_information_from_table = """
# SELECT * FROM programming_languages
# ORDER language_names




# """
# cur.execute(select_information_from_table)
# for i in cur.fetchall():
#     print(i)

# show_s = """
# show searchpath;

# ////////////////////////////////////////////////////////////////////////
# Ma'lumotlarga uzgartirish kiritamiz

# update_information_in_table = """
# UPDATE programming_languages
# SET language_names = 'C++ and C#'
# WHERE id = 4


# """
# cur.execute(update_information_in_table)
# conn.commit()


# /////////////////////////////////////////////////////////////////////////////////
# Jadvalga qushimcha ustun qushamiz

# add_column_to_table = """
# ALTER TABLE programming_languages
# ADD COLUMN created_at DATE NOT NULL DEFAULT CURRENT_DATE

# """
# cur.execute(add_column_to_table)
# conn.commit()

# //////////////////////////////////////////////////////////////////////////////////
# Jadvaldagi ustunni uchiramiz

# delete_column_from_table = """
# ALTER TABLE programming_languages
# DROP COLUMN created_at
# """
# cur.execute(delete_column_from_table)
# conn.commit()

# ////////////////////////////////////////////////////////////////////////////////
#Jadvaldagi malumotlardan birini uzchiramiz 


delete_information_from_table = """
DELETE FROM programming_languages
WHERE id = 6

"""

cur.execute(delete_information_from_table)
conn.commit()




)