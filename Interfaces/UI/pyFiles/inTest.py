import sqlite3
import time

# Создаем соединение с базой данных (в памяти для простоты)
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Создаем таблицы
cur.execute('''
CREATE TABLE without_index (
    id INTEGER PRIMARY KEY,
    value TEXT
)
''')

cur.execute('''
CREATE TABLE with_index (
    id INTEGER PRIMARY KEY,
    value TEXT
)
''')

# Создаем индекс на столбце value для таблицы with_index
cur.execute('''
CREATE INDEX idx_value ON with_index(value)
''')
print(cur.execute("PRAGMA index_list('without_index');").fetchall())
# Функция для заполнения таблицы данными
def populate_table(table_name, num_records):
    for i in range(num_records):
        cur.execute(f'''
        INSERT INTO {table_name} (value)
        VALUES (?)
        ''', (f'value_{i}',))
    conn.commit()

# Заполняем таблицы большим количеством данных
NUM_RECORDS = 100000
populate_table('without_index', NUM_RECORDS)
populate_table('with_index', NUM_RECORDS)

# Функция для измерения времени выполнения запроса
def measure_query_time(table_name, value):
    start_time = time.time()
    cur.execute(f'''
    SELECT * FROM {table_name}
    WHERE value = ?
    ''', (value,))
    cur.fetchall()
    end_time = time.time()
    return end_time - start_time

# Измеряем время выполнения запроса для обоих таблиц
value_to_search = 'value_99999'
time_without_index = measure_query_time('without_index', value_to_search)
time_with_index = measure_query_time('with_index', value_to_search)

print(f'Time without index: {time_without_index:.8f} seconds')
print(f'Time with index: {time_with_index:.8f} seconds')

# Закрываем соединение
conn.close()
