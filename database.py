import sqlite3
from datetime import datetime, date

def init_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    # <--- CHANGED: เพิ่มคอลัมน์ใหม่ supplier, price, date_added
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        part_number TEXT,
        location TEXT,
        quantity INTEGER NOT NULL,
        min_quantity INTEGER,
        supplier TEXT,
        price REAL,
        date_added TEXT,
        last_updated TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# <--- CHANGED: เพิ่ม parameter สำหรับรับข้อมูลใหม่
def add_item(name, part_number, location, quantity, min_quantity, supplier, price, date_added):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    timestamp = datetime.now()
    # ถ้าไม่ได้กรอกวันที่มา ให้ใช้วันที่ปัจจุบัน
    if not date_added:
        date_added = date.today().isoformat()
        
    cursor.execute("""
        INSERT INTO inventory (name, part_number, location, quantity, min_quantity, supplier, price, date_added, last_updated) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, part_number, location, quantity, min_quantity, supplier, price, date_added, timestamp))
    conn.commit()
    conn.close()

def view_all_items():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    # <--- CHANGED: จัดรูปแบบวันที่ให้อ่านง่าย และดึงข้อมูลคอลัมน์ใหม่
    cursor.execute("""
        SELECT id, name, part_number, location, quantity, min_quantity, supplier, price, 
               date_added, STRFTIME('%Y-%m-%d %H:%M', last_updated) 
        FROM inventory
    """)
    items = cursor.fetchall()
    conn.close()
    return items

# <--- CHANGED: เพิ่ม parameter สำหรับอัปเดตข้อมูลใหม่
def update_item(item_id, name, part_number, location, quantity, min_quantity, supplier, price, date_added):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    timestamp = datetime.now()
    if not date_added:
        date_added = date.today().isoformat()
        
    cursor.execute("""
        UPDATE inventory
        SET name = ?, part_number = ?, location = ?, quantity = ?, min_quantity = ?, 
            supplier = ?, price = ?, date_added = ?, last_updated = ?
        WHERE id = ?
    """, (name, part_number, location, quantity, min_quantity, supplier, price, date_added, timestamp, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

def search_item(query):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    # <--- CHANGED: ทำให้สามารถค้นหาจาก Supplier ได้ด้วย
    cursor.execute("""
        SELECT id, name, part_number, location, quantity, min_quantity, supplier, price, 
               date_added, STRFTIME('%Y-%m-%d %H:%M', last_updated) 
        FROM inventory WHERE name LIKE ? OR part_number LIKE ? OR supplier LIKE ?
    """, ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
    items = cursor.fetchall()
    conn.close()
    return items

if __name__ == '__main__':
    init_db()