import tkinter as tk
from tkinter import ttk, messagebox
import database as db
from datetime import date

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool & Spare Parts Inventory Tracker (Upgraded)")
        self.root.geometry("1200x650")

        db.init_db()

        # <--- ADDED: สร้างฟังก์ชันสำหรับ validate ข้อมูล
        self.vcmd_int = (self.root.register(self.validate_integer), '%P')
        self.vcmd_float = (self.root.register(self.validate_float), '%P')

        self.create_widgets()
        self.populate_treeview()

    # <--- ADDED: ฟังก์ชันสำหรับตรวจสอบว่าเป็นตัวเลขจำนวนเต็มหรือไม่
    def validate_integer(self, value_if_allowed):
        if value_if_allowed == "":
            return True
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False

    # <--- ADDED: ฟังก์ชันสำหรับตรวจสอบว่าเป็นเลขทศนิยมหรือไม่
    def validate_float(self, value_if_allowed):
        if value_if_allowed == "":
            return True
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False

    def create_widgets(self):
        form_frame = tk.LabelFrame(self.root, text="Item Details")
        form_frame.pack(fill="x", padx=10, pady=5)

        # --- Row 0 ---
        tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Part Number:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.part_number_entry = tk.Entry(form_frame, width=20)
        self.part_number_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Location:").grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.location_entry = tk.Entry(form_frame, width=30)
        self.location_entry.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        
        # --- Row 1 ---
        tk.Label(form_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.quantity_entry = tk.Entry(form_frame, width=10, validate='key', validatecommand=self.vcmd_int)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Min Quantity:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.min_quantity_entry = tk.Entry(form_frame, width=10, validate='key', validatecommand=self.vcmd_int)
        self.min_quantity_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        tk.Label(form_frame, text="Supplier:").grid(row=1, column=4, padx=5, pady=5, sticky="w")
        self.supplier_entry = tk.Entry(form_frame, width=30)
        self.supplier_entry.grid(row=1, column=5, padx=5, pady=5, sticky="w")

        # --- Row 2 ---
        tk.Label(form_frame, text="Price:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.price_entry = tk.Entry(form_frame, width=10, validate='key', validatecommand=self.vcmd_float)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        tk.Label(form_frame, text="Date Added (YYYY-MM-DD):").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.date_added_entry = tk.Entry(form_frame, width=20)
        self.date_added_entry.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        self.date_added_entry.insert(0, date.today().isoformat()) # ใส่วันที่ปัจจุบันเป็นค่าเริ่มต้น


        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", padx=10, pady=5)
        # ... (ส่วนปุ่มเหมือนเดิม)
        tk.Button(button_frame, text="Add Item", command=self.add_item).pack(side="left", padx=5)
        tk.Button(button_frame, text="Update Selected", command=self.update_item).pack(side="left", padx=5)
        tk.Button(button_frame, text="Delete Selected", command=self.delete_item).pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields).pack(side="left", padx=5)

        search_frame = tk.LabelFrame(self.root, text="Search")
        search_frame.pack(fill="x", padx=10, pady=5)
        # ... (ส่วนค้นหาเหมือนเดิม)
        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side="left", padx=5, pady=5)
        tk.Button(search_frame, text="Search", command=self.search_items).pack(side="left", padx=5)
        tk.Button(search_frame, text="Show All", command=self.populate_treeview).pack(side="left", padx=5)

        tree_frame = tk.Frame(self.root)
        tree_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # <--- CHANGED: เพิ่มคอลัมน์ใหม่ใน Treeview
        columns = ("ID", "Name", "Part Number", "Location", "Qty", "Min Qty", "Supplier", "Price", "Date Added", "Last Updated")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        
        # <--- CHANGED: ปรับความกว้างคอลัมน์
        self.tree.column("ID", width=40, anchor="center")
        self.tree.column("Name", width=200)
        self.tree.column("Part Number", width=120)
        self.tree.column("Location", width=120)
        self.tree.column("Qty", width=60, anchor="center")
        self.tree.column("Min Qty", width=70, anchor="center")
        self.tree.column("Supplier", width=120)
        self.tree.column("Price", width=80, anchor="e")
        self.tree.column("Date Added", width=100, anchor="center")
        self.tree.column("Last Updated", width=120, anchor="center")

        for col in columns:
            self.tree.heading(col, text=col)
        
        self.tree.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)

    def populate_treeview(self, items=None):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        if items is None:
            items = db.view_all_items()
            
        for item in items:
            quantity = item[4]
            min_quantity = item[5] if item[5] is not None else 0
            tag = 'low_stock' if quantity <= min_quantity and quantity > 0 else 'normal'
            if quantity == 0:
                tag = 'out_of_stock'

            self.tree.insert("", "end", values=item, tags=(tag,))
        
        self.tree.tag_configure('low_stock', background='orange')
        self.tree.tag_configure('out_of_stock', background='#FF7F7F') # สีแดงอ่อน
        self.tree.tag_configure('normal', background='')


    def add_item(self):
        if not self.name_entry.get() or not self.quantity_entry.get():
            messagebox.showerror("Error", "Name and Quantity are required fields.")
            return
        
        # <--- CHANGED: ส่งข้อมูลใหม่เข้าไปในฟังก์ชัน
        db.add_item(
            self.name_entry.get(),
            self.part_number_entry.get(),
            self.location_entry.get(),
            int(self.quantity_entry.get()),
            int(self.min_quantity_entry.get() or 0),
            self.supplier_entry.get(),
            float(self.price_entry.get() or 0.0),
            self.date_added_entry.get()
        )
        messagebox.showinfo("Success", "Item added successfully.")
        self.clear_fields()
        self.populate_treeview()

    def update_item(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to update.")
            return
        
        item_id = self.tree.item(selected_item)['values'][0]
        
        # <--- CHANGED: ส่งข้อมูลใหม่เข้าไปในฟังก์ชัน
        db.update_item(
            item_id,
            self.name_entry.get(),
            self.part_number_entry.get(),
            self.location_entry.get(),
            int(self.quantity_entry.get()),
            int(self.min_quantity_entry.get() or 0),
            self.supplier_entry.get(),
            float(self.price_entry.get() or 0.0),
            self.date_added_entry.get()
        )
        messagebox.showinfo("Success", "Item updated successfully.")
        self.clear_fields()
        self.populate_treeview()

    def delete_item(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to delete.")
            return

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this item?"):
            item_id = self.tree.item(selected_item)['values'][0]
            db.delete_item(item_id)
            messagebox.showinfo("Success", "Item deleted successfully.")
            self.clear_fields()
            self.populate_treeview()

    def search_items(self):
        query = self.search_entry.get()
        if not query:
            self.populate_treeview()
            return
        items = db.search_item(query)
        self.populate_treeview(items)

    def on_item_select(self, event):
        selected_item = self.tree.focus()
        if not selected_item:
            return
        
        item = self.tree.item(selected_item)['values']
        self.clear_fields()
        
        # <--- CHANGED: โหลดข้อมูลจากคอลัมน์ใหม่มาใส่ใน Entry
        self.name_entry.insert(0, item[1])
        self.part_number_entry.insert(0, item[2])
        self.location_entry.insert(0, item[3])
        self.quantity_entry.insert(0, item[4])
        self.min_quantity_entry.insert(0, item[5] if item[5] is not None else "")
        self.supplier_entry.insert(0, item[6] if item[6] is not None else "")
        self.price_entry.insert(0, item[7] if item[7] is not None else "")
        self.date_added_entry.insert(0, item[8] if item[8] is not None else "")
    
    def clear_fields(self):
        self.name_entry.delete(0, "end")
        self.part_number_entry.delete(0, "end")
        self.location_entry.delete(0, "end")
        self.quantity_entry.delete(0, "end")
        self.min_quantity_entry.delete(0, "end")
        self.search_entry.delete(0, "end")
        # <--- ADDED: ล้างข้อมูลใน Entry ใหม่
        self.supplier_entry.delete(0, "end")
        self.price_entry.delete(0, "end")
        self.date_added_entry.delete(0, "end")
        # ใส่วันที่ปัจจุบันกลับเข้าไป
        self.date_added_entry.insert(0, date.today().isoformat())
        if self.tree.focus():
            self.tree.selection_remove(self.tree.focus())

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()