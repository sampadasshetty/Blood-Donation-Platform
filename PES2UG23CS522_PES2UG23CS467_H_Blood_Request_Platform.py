import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import mysql.connector
from datetime import datetime, date
from ttkthemes import ThemedTk

class BloodDonationPlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Donation & Request Management System")
        self.root.geometry("1200x700")
        
        # Database connection
        self.db = None
        self.cursor = None
        
        # Color scheme
        self.bg_color = "#f0f0f0"
        self.primary_color = "#c41e3a"  # Blood red
        self.secondary_color = "#ffffff"
        self.text_color = "#333333"
        
        self.create_connection()
        self.create_main_interface()
        
    def create_connection(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysqlsam#",  # Change this
                database="mini_project"
            )
            self.cursor = self.db.cursor()
            messagebox.showinfo("Success", "Connected to Database Successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Database Connection Failed: {str(e)}")
            
    def create_main_interface(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🩸 BLOOD DONATION PLATFORM", 
                              font=("Arial", 24, "bold"), bg=self.primary_color, 
                              fg="white")
        title_label.pack(pady=20)
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left sidebar - Menu
        sidebar = tk.Frame(main_container, bg=self.secondary_color, width=200, relief=tk.RAISED, bd=2)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        sidebar.pack_propagate(False)
        
        menu_title = tk.Label(sidebar, text="MENU", font=("Arial", 14, "bold"), 
                             bg=self.primary_color, fg="white", pady=10)
        menu_title.pack(fill=tk.X)
        
        # Menu buttons
        menu_items = [
            ("👤 Donor Management", self.donor_management),
            ("🏥 Hospital Management", self.hospital_management),
            ("📋 Blood Requests", self.blood_request_management),
            ("💉 Donations", self.donation_management),
            ("🤒 Patients", self.patient_management),
            ("📊 Reports", self.reports),
            ("🔍 Queries", self.advanced_queries),
            ("⚙️ Procedures/Functions", self.test_procedures_functions)
        ]
        
        for text, command in menu_items:
            btn = tk.Button(sidebar, text=text, command=command, 
                          font=("Arial", 11), bg=self.secondary_color,
                          fg=self.text_color, relief=tk.FLAT, anchor="w",
                          padx=20, pady=10, cursor="hand2")
            btn.pack(fill=tk.X, pady=2)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.primary_color, fg="white"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.secondary_color, fg=self.text_color))
        
        # Right content area
        self.content_frame = tk.Frame(main_container, bg=self.bg_color)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Welcome screen
        self.show_welcome()
        
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
    def show_welcome(self):
        self.clear_content()
        welcome_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        welcome_frame.pack(expand=True)
        
        welcome_text = """
        Welcome to Blood Donation Platform
        
        🩸 Save Lives, Donate Blood 🩸
        
        Use the menu to navigate through:
        • Donor Management
        • Hospital Management
        • Blood Requests
        • Donation Records
        • Reports and Analytics
        """
        
        label = tk.Label(welcome_frame, text=welcome_text, font=("Arial", 16),
                        bg=self.bg_color, fg=self.text_color, justify=tk.CENTER)
        label.pack(pady=50)
        
    # DONOR MANAGEMENT
    def donor_management(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="👤 DONOR MANAGEMENT", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        # Notebook for tabs
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Add Donor
        add_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(add_tab, text="Add Donor")
        
        form_frame = tk.Frame(add_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        fields = [
            ("First Name:", "first_name"),
            ("Last Name:", "last_name"),
            ("Age:", "age"),
            ("Gender:", "gender"),
            ("Address:", "address"),
            ("Contact:", "contact")
        ]
        
        entries = {}
        for i, (label_text, field_name) in enumerate(fields):
            tk.Label(form_frame, text=label_text, font=("Arial", 11), 
                    bg=self.secondary_color).grid(row=i, column=0, sticky="w", padx=20, pady=10)
            
            if field_name == "gender":
                entries[field_name] = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], 
                                                   font=("Arial", 11), width=30)
            else:
                entries[field_name] = tk.Entry(form_frame, font=("Arial", 11), width=32)
            entries[field_name].grid(row=i, column=1, padx=20, pady=10)
        
        def add_donor():
            try:
                self.cursor.callproc('sp_add_donor', [
                    entries['address'].get(),
                    entries['first_name'].get(),
                    entries['last_name'].get(),
                    int(entries['age'].get()),
                    entries['gender'].get(),
                    entries['contact'].get()
                ])
                self.db.commit()
                messagebox.showinfo("Success", "Donor added successfully!")
                for entry in entries.values():
                    if isinstance(entry, tk.Entry):
                        entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add donor: {str(e)}")
        
        tk.Button(form_frame, text="Add Donor", command=add_donor, 
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=len(fields), column=0, 
                                                        columnspan=2, pady=20)
        
        # Tab 2: View Donors
        view_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(view_tab, text="View Donors")
        
        # Treeview
        tree_frame = tk.Frame(view_tab)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("ID", "Name", "Age", "Gender", "Contact", "Status")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", 
                           yscrollcommand=scrollbar.set)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        scrollbar.config(command=tree.yview)
        tree.pack(fill=tk.BOTH, expand=True)
        
        def refresh_donors():
            for item in tree.get_children():
                tree.delete(item)
            
            query = """
            SELECT d.D_id, CONCAT(d.First_Name, ' ', d.Last_Name) AS Name, 
                   d.Age, d.Gender, dc.Contact, r.Status
            FROM Donor d
            JOIN Donor_Contact dc ON d.D_id = dc.D_id
            LEFT JOIN Register r ON d.D_id = r.D_id
            """
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                tree.insert("", tk.END, values=row)
        
        tk.Button(view_tab, text="🔄 Refresh", command=refresh_donors,
                 bg=self.primary_color, fg="white", font=("Arial", 11),
                 cursor="hand2", padx=15, pady=5).pack(pady=10)
        
        refresh_donors()
        
        # Tab 3: Update Donor
        update_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(update_tab, text="Update Donor")
        
        update_frame = tk.Frame(update_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        update_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        tk.Label(update_frame, text="Donor ID:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        donor_id_entry = tk.Entry(update_frame, font=("Arial", 11), width=32)
        donor_id_entry.grid(row=0, column=1, padx=20, pady=10)
        
        tk.Label(update_frame, text="New Address:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        new_address_entry = tk.Entry(update_frame, font=("Arial", 11), width=32)
        new_address_entry.grid(row=1, column=1, padx=20, pady=10)
        
        tk.Label(update_frame, text="New Age:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=2, column=0, sticky="w", padx=20, pady=10)
        new_age_entry = tk.Entry(update_frame, font=("Arial", 11), width=32)
        new_age_entry.grid(row=2, column=1, padx=20, pady=10)
        
        def update_donor():
            try:
                query = """UPDATE Donor SET Address = %s, Age = %s WHERE D_id = %s"""
                self.cursor.execute(query, (new_address_entry.get(), 
                                           int(new_age_entry.get()), 
                                           int(donor_id_entry.get())))
                self.db.commit()
                messagebox.showinfo("Success", "Donor updated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update: {str(e)}")
        
        tk.Button(update_frame, text="Update Donor", command=update_donor,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=3, column=0, 
                                                        columnspan=2, pady=20)
        
        # Tab 4: Delete Donor
        delete_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(delete_tab, text="Delete Donor")
        
        delete_frame = tk.Frame(delete_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        delete_frame.pack(pady=20, padx=20)
        
        tk.Label(delete_frame, text="Enter Donor ID to Delete:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=0, padx=20, pady=20)
        delete_id_entry = tk.Entry(delete_frame, font=("Arial", 11), width=20)
        delete_id_entry.grid(row=0, column=1, padx=20, pady=20)
        
        def delete_donor():
            if messagebox.askyesno("Confirm", "Are you sure you want to delete this donor?"):
                try:
                    # Delete from related tables first
                    self.cursor.execute("DELETE FROM Donor_Contact WHERE D_id = %s", 
                                      (int(delete_id_entry.get()),))
                    self.cursor.execute("DELETE FROM Register WHERE D_id = %s", 
                                      (int(delete_id_entry.get()),))
                    self.cursor.execute("DELETE FROM Donation WHERE D_id = %s", 
                                      (int(delete_id_entry.get()),))
                    self.cursor.execute("DELETE FROM Donor WHERE D_id = %s", 
                                      (int(delete_id_entry.get()),))
                    self.db.commit()
                    messagebox.showinfo("Success", "Donor deleted successfully!")
                    delete_id_entry.delete(0, tk.END)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete: {str(e)}")
        
        tk.Button(delete_frame, text="Delete Donor", command=delete_donor,
                 bg="#d32f2f", fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=1, column=0, 
                                                        columnspan=2, pady=20)
    
    # HOSPITAL MANAGEMENT
    def hospital_management(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="🏥 HOSPITAL MANAGEMENT", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add Hospital Tab
        add_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(add_tab, text="Add Hospital")
        
        form_frame = tk.Frame(add_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        fields = [
            ("Hospital Name:", "name"),
            ("City:", "city"),
            ("State:", "state"),
            ("Pincode:", "pincode"),
            ("Contact:", "contact")
        ]
        
        entries = {}
        for i, (label_text, field_name) in enumerate(fields):
            tk.Label(form_frame, text=label_text, font=("Arial", 11),
                    bg=self.secondary_color).grid(row=i, column=0, sticky="w", padx=20, pady=10)
            entries[field_name] = tk.Entry(form_frame, font=("Arial", 11), width=32)
            entries[field_name].grid(row=i, column=1, padx=20, pady=10)
        
        def add_hospital():
            try:
                query = """INSERT INTO Hospital (Name, City, State, Pincode) 
                          VALUES (%s, %s, %s, %s)"""
                self.cursor.execute(query, (entries['name'].get(), entries['city'].get(),
                                           entries['state'].get(), entries['pincode'].get()))
                h_id = self.cursor.lastrowid
                
                contact_query = """INSERT INTO Hospital_Contact (Contact, H_id) VALUES (%s, %s)"""
                self.cursor.execute(contact_query, (entries['contact'].get(), h_id))
                
                self.db.commit()
                messagebox.showinfo("Success", f"Hospital added successfully! ID: {h_id}")
                for entry in entries.values():
                    entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add hospital: {str(e)}")
        
        tk.Button(form_frame, text="Add Hospital", command=add_hospital,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=len(fields), column=0, 
                                                        columnspan=2, pady=20)
        
        # View Hospitals Tab
        view_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(view_tab, text="View Hospitals")
        
        tree_frame = tk.Frame(view_tab)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("ID", "Name", "City", "State", "Pincode", "Contact")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings",
                           yscrollcommand=scrollbar.set)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        scrollbar.config(command=tree.yview)
        tree.pack(fill=tk.BOTH, expand=True)
        
        def refresh_hospitals():
            for item in tree.get_children():
                tree.delete(item)
            
            query = """
            SELECT h.H_id, h.Name, h.City, h.State, h.Pincode, hc.Contact
            FROM Hospital h
            LEFT JOIN Hospital_Contact hc ON h.H_id = hc.H_id
            """
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                tree.insert("", tk.END, values=row)
        
        tk.Button(view_tab, text="🔄 Refresh", command=refresh_hospitals,
                 bg=self.primary_color, fg="white", font=("Arial", 11),
                 cursor="hand2", padx=15, pady=5).pack(pady=10)
        
        refresh_hospitals()
    
    # BLOOD REQUEST MANAGEMENT
    def blood_request_management(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="📋 BLOOD REQUEST MANAGEMENT", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create Request Tab
        create_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(create_tab, text="Create Request")
        
        form_frame = tk.Frame(create_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        tk.Label(form_frame, text="Blood Type:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        blood_type_combo = ttk.Combobox(form_frame, 
                                       values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                                       font=("Arial", 11), width=30)
        blood_type_combo.grid(row=0, column=1, padx=20, pady=10)
        
        tk.Label(form_frame, text="Quantity (Units):", font=("Arial", 11),
                bg=self.secondary_color).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        quantity_entry = tk.Entry(form_frame, font=("Arial", 11), width=32)
        quantity_entry.grid(row=1, column=1, padx=20, pady=10)
        
        tk.Label(form_frame, text="Hospital ID:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=2, column=0, sticky="w", padx=20, pady=10)
        hospital_id_entry = tk.Entry(form_frame, font=("Arial", 11), width=32)
        hospital_id_entry.grid(row=2, column=1, padx=20, pady=10)
        
        def create_request():
            try:
                self.cursor.callproc('sp_process_blood_request', [
                    blood_type_combo.get(),
                    int(quantity_entry.get()),
                    int(hospital_id_entry.get())
                ])
                self.db.commit()
                messagebox.showinfo("Success", "Blood request created successfully!")
                blood_type_combo.set('')
                quantity_entry.delete(0, tk.END)
                hospital_id_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create request: {str(e)}")
        
        tk.Button(form_frame, text="Create Request", command=create_request,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=3, column=0, 
                                                        columnspan=2, pady=20)
        
        # View Requests Tab
        view_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(view_tab, text="View Requests")
        
        tree_frame = tk.Frame(view_tab)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("Request ID", "Blood Type", "Quantity", "Date", "Status", "Hospital")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings",
                           yscrollcommand=scrollbar.set)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        scrollbar.config(command=tree.yview)
        tree.pack(fill=tk.BOTH, expand=True)
        
        def refresh_requests():
            for item in tree.get_children():
                tree.delete(item)
            
            query = """
            SELECT br.Request_Id, br.Blood_type, br.Quantity, br.Request_date, 
                   br.Status, h.Name
            FROM Blood_Request br
            JOIN Hospital h ON br.H_id = h.H_id
            ORDER BY br.Request_date DESC
            """
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                tree.insert("", tk.END, values=row)
        
        tk.Button(view_tab, text="🔄 Refresh", command=refresh_requests,
                 bg=self.primary_color, fg="white", font=("Arial", 11),
                 cursor="hand2", padx=15, pady=5).pack(pady=10)
        
        refresh_requests()
        
        # Update Status Tab
        update_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(update_tab, text="Update Status")
        
        update_frame = tk.Frame(update_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        update_frame.pack(pady=20, padx=20)
        
        tk.Label(update_frame, text="Request ID:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        request_id_entry = tk.Entry(update_frame, font=("Arial", 11), width=32)
        request_id_entry.grid(row=0, column=1, padx=20, pady=10)
        
        tk.Label(update_frame, text="New Status:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        status_combo = ttk.Combobox(update_frame, 
                                   values=["Pending", "Approved", "Fulfilled", "Rejected"],
                                   font=("Arial", 11), width=30)
        status_combo.grid(row=1, column=1, padx=20, pady=10)
        
        def update_status():
            try:
                self.cursor.callproc('sp_update_request_status', [
                    int(request_id_entry.get()),
                    status_combo.get()
                ])
                self.db.commit()
                messagebox.showinfo("Success", "Request status updated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update status: {str(e)}")
        
        tk.Button(update_frame, text="Update Status", command=update_status,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=2, column=0, 
                                                        columnspan=2, pady=20)
    
    # DONATION MANAGEMENT
    def donation_management(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="💉 DONATION MANAGEMENT", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Record Donation Tab
        record_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(record_tab, text="Record Donation")
        
        form_frame = tk.Frame(record_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        tk.Label(form_frame, text="Donor ID:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        donor_id_entry = tk.Entry(form_frame, font=("Arial", 11), width=32)
        donor_id_entry.grid(row=0, column=1, padx=20, pady=10)
        
        tk.Label(form_frame, text="Hospital ID:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        hospital_id_entry = tk.Entry(form_frame, font=("Arial", 11), width=32)
        hospital_id_entry.grid(row=1, column=1, padx=20, pady=10)
        
        tk.Label(form_frame, text="Quantity (Units):", font=("Arial", 11),
                bg=self.secondary_color).grid(row=2, column=0, sticky="w", padx=20, pady=10)
        quantity_entry = tk.Entry(form_frame, font=("Arial", 11), width=32)
        quantity_entry.grid(row=2, column=1, padx=20, pady=10)
        
        def record_donation():
            try:
                self.cursor.callproc('sp_record_donation', [
                    int(donor_id_entry.get()),
                    int(hospital_id_entry.get()),
                    int(quantity_entry.get())
                ])
                self.db.commit()
                messagebox.showinfo("Success", "Donation recorded successfully!")
                donor_id_entry.delete(0, tk.END)
                hospital_id_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to record donation: {str(e)}")
        
        tk.Button(form_frame, text="Record Donation", command=record_donation,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=3, column=0, 
                                                        columnspan=2, pady=20)
        
        # View Donations Tab
        view_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(view_tab, text="View Donations")
        
        tree_frame = tk.Frame(view_tab)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("Donation ID", "Donor Name", "Hospital", "Date", "Quantity")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings",
                           yscrollcommand=scrollbar.set)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        scrollbar.config(command=tree.yview)
        tree.pack(fill=tk.BOTH, expand=True)
        
        def refresh_donations():
            for item in tree.get_children():
                tree.delete(item)
            
            query = """
            SELECT don.Donation_id, CONCAT(d.First_Name, ' ', d.Last_Name) AS Donor_Name,
                   h.Name AS Hospital_Name, don.Donation_date, don.Quantity
            FROM Donation don
            INNER JOIN Donor d ON don.D_id = d.D_id
            INNER JOIN Hospital h ON don.H_id = h.H_id
            ORDER BY don.Donation_date DESC
            """
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                tree.insert("", tk.END, values=row)
        
        tk.Button(view_tab, text="🔄 Refresh", command=refresh_donations,
                 bg=self.primary_color, fg="white", font=("Arial", 11),
                 cursor="hand2", padx=15, pady=5).pack(pady=10)
        
        refresh_donations()
    
    # PATIENT MANAGEMENT
    def patient_management(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="🤒 PATIENT MANAGEMENT", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add Patient Tab
        add_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(add_tab, text="Add Patient")
        
        form_frame = tk.Frame(add_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        fields = [
            ("First Name:", "first_name"),
            ("Last Name:", "last_name"),
            ("Age:", "age"),
            ("Disease:", "disease"),
            ("Blood Type Needed:", "blood_type"),
            ("Hospital ID:", "hospital_id")
        ]
        
        entries = {}
        for i, (label_text, field_name) in enumerate(fields):
            tk.Label(form_frame, text=label_text, font=("Arial", 11),
                    bg=self.secondary_color).grid(row=i, column=0, sticky="w", padx=20, pady=10)
            
            if field_name == "blood_type":
                entries[field_name] = ttk.Combobox(form_frame, 
                                                   values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                                                   font=("Arial", 11), width=30)
            else:
                entries[field_name] = tk.Entry(form_frame, font=("Arial", 11), width=32)
            entries[field_name].grid(row=i, column=1, padx=20, pady=10)
        
        def add_patient():
            try:
                query = """INSERT INTO Patient (First_Name, Last_Name, Age, Disease, H_id, Request_bloodtype)
                          VALUES (%s, %s, %s, %s, %s, %s)"""
                self.cursor.execute(query, (entries['first_name'].get(), entries['last_name'].get(),
                                           int(entries['age'].get()), entries['disease'].get(),
                                           int(entries['hospital_id'].get()), entries['blood_type'].get()))
                self.db.commit()
                messagebox.showinfo("Success", "Patient added successfully!")
                for entry in entries.values():
                    if isinstance(entry, tk.Entry):
                        entry.delete(0, tk.END)
                    else:
                        entry.set('')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add patient: {str(e)}")
        
        tk.Button(form_frame, text="Add Patient", command=add_patient,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).grid(row=len(fields), column=0, 
                                                        columnspan=2, pady=20)
        
        # View Patients Tab
        view_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(view_tab, text="View Patients")
        
        tree_frame = tk.Frame(view_tab)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("Patient ID", "Name", "Age", "Disease", "Blood Type", "Hospital")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings",
                           yscrollcommand=scrollbar.set)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        scrollbar.config(command=tree.yview)
        tree.pack(fill=tk.BOTH, expand=True)
        
        def refresh_patients():
            for item in tree.get_children():
                tree.delete(item)
            
            query = """
            SELECT p.Patient_Id, CONCAT(p.First_Name, ' ', p.Last_Name) AS Name,
                   p.Age, p.Disease, p.Request_bloodtype, h.Name
            FROM Patient p
            INNER JOIN Hospital h ON p.H_id = h.H_id
            """
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                tree.insert("", tk.END, values=row)
        
        tk.Button(view_tab, text="🔄 Refresh", command=refresh_patients,
                 bg=self.primary_color, fg="white", font=("Arial", 11),
                 cursor="hand2", padx=15, pady=5).pack(pady=10)
        
        refresh_patients()
    
    # REPORTS
    def reports(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="📊 REPORTS & ANALYTICS", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Hospital Report Tab
        hospital_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(hospital_tab, text="Hospital Donation Report")
        
        input_frame = tk.Frame(hospital_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        input_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(input_frame, text="Hospital ID:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=0, padx=10, pady=10)
        h_id_entry = tk.Entry(input_frame, font=("Arial", 11), width=15)
        h_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(input_frame, text="Start Date (YYYY-MM-DD):", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=2, padx=10, pady=10)
        start_date_entry = tk.Entry(input_frame, font=("Arial", 11), width=15)
        start_date_entry.grid(row=0, column=3, padx=10, pady=10)
        
        tk.Label(input_frame, text="End Date (YYYY-MM-DD):", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=4, padx=10, pady=10)
        end_date_entry = tk.Entry(input_frame, font=("Arial", 11), width=15)
        end_date_entry.grid(row=0, column=5, padx=10, pady=10)
        
        def generate_report():
            try:
                self.cursor.callproc('sp_hospital_donation_report', [
                    int(h_id_entry.get()),
                    start_date_entry.get(),
                    end_date_entry.get()
                ])
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "=" * 80 + "\n")
                result_text.insert(tk.END, "HOSPITAL DONATION REPORT\n")
                result_text.insert(tk.END, "=" * 80 + "\n\n")
                
                for result in self.cursor.stored_results():
                    rows = result.fetchall()
                    if rows:
                        for row in rows:
                            result_text.insert(tk.END, f"Hospital Name: {row[0]}\n")
                            result_text.insert(tk.END, f"Total Donors: {row[1]}\n")
                            result_text.insert(tk.END, f"Total Donations: {row[2]}\n")
                            result_text.insert(tk.END, f"Total Units Collected: {row[3]}\n")
                            result_text.insert(tk.END, f"First Donation: {row[4]}\n")
                            result_text.insert(tk.END, f"Last Donation: {row[5]}\n")
                    else:
                        result_text.insert(tk.END, "No data found for the specified period.\n")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate report: {str(e)}")
        
        tk.Button(input_frame, text="Generate Report", command=generate_report,
                 bg=self.primary_color, fg="white", font=("Arial", 11, "bold"),
                 cursor="hand2", padx=20, pady=8).grid(row=0, column=6, padx=10, pady=10)
        
        result_text = scrolledtext.ScrolledText(hospital_tab, height=20, font=("Courier", 10))
        result_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        result_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        def generate_report():
            try:
                self.cursor.callproc('sp_hospital_donation_report', [
                    int(h_id_entry.get()),
                    start_date_entry.get(),
                    end_date_entry.get()
                ])
                
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "=" * 80 + "\n")
                result_text.insert(tk.END, "HOSPITAL DONATION REPORT\n")
                result_text.insert(tk.END, "=" * 80 + "\n\n")
                
                for result in self.cursor.stored_results():
                    rows = result.fetchall()
                    if rows:
                        for row in rows:
                            result_text.insert(tk.END, f"Hospital Name: {row[0]}\n")
                            result_text.insert(tk.END, f"Total Donors: {row[1]}\n")
                            result_text.insert(tk.END, f"Total Donations: {row[2]}\n")
                            result_text.insert(tk.END, f"Total Units Collected: {row[3]}\n")
                            result_text.insert(tk.END, f"First Donation: {row[4]}\n")
                            result_text.insert(tk.END, f"Last Donation: {row[5]}\n")
                    else:
                        result_text.insert(tk.END, "No data found for the specified period.\n")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate report: {str(e)}")
        
        tk.Button(input_frame, text="Generate Report", command=generate_report,
                 bg=self.primary_color, fg="white", font=("Arial", 11),
                 cursor="hand2", padx=15, pady=5).grid(row=0, column=6, padx=10, pady=10)
        
        # Aggregate Statistics Tab
        stats_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(stats_tab, text="Aggregate Statistics")
        
        result_frame = tk.Frame(stats_tab, bg=self.bg_color)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_area = scrolledtext.ScrolledText(result_frame, height=25, font=("Courier", 10))
        text_area.pack(fill=tk.BOTH, expand=True)
        
        def show_statistics():
            text_area.delete(1.0, tk.END)
            
            try:
                # Hospital Statistics
                text_area.insert(tk.END, "=" * 100 + "\n")
                text_area.insert(tk.END, "HOSPITAL STATISTICS\n")
                text_area.insert(tk.END, "=" * 100 + "\n\n")
                
                query = """
                SELECT h.Name AS Hospital, 
                       COALESCE(COUNT(don.Donation_id), 0) AS Donations,
                       COALESCE(SUM(don.Quantity), 0) AS Total_Units, 
                       COALESCE(AVG(don.Quantity), 0) AS Avg_Units
                FROM Hospital h
                LEFT JOIN Donation don ON h.H_id = don.H_id
                GROUP BY h.H_id, h.Name
                ORDER BY Total_Units DESC
                """
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                
                text_area.insert(tk.END, f"{'Hospital':<35} {'Donations':<15} {'Total Units':<15} {'Avg Units':<15}\n")
                text_area.insert(tk.END, "-" * 100 + "\n")
                
                if rows:
                    for row in rows:
                        hosp_name = str(row[0])[:34]  # Truncate long names
                        donations = row[1] if row[1] else 0
                        total_units = row[2] if row[2] else 0
                        avg_units = float(row[3]) if row[3] else 0.0
                        text_area.insert(tk.END, f"{hosp_name:<35} {donations:<15} {total_units:<15} {avg_units:<15.2f}\n")
                else:
                    text_area.insert(tk.END, "No hospital data available.\n")
                
                
                # Blood Type Demand
                text_area.insert(tk.END, "\n" + "=" * 100 + "\n")
                text_area.insert(tk.END, "BLOOD TYPE DEMAND ANALYSIS\n")
                text_area.insert(tk.END, "=" * 100 + "\n\n")
                
                query = """
                SELECT Blood_type, 
                       COUNT(*) AS Total_Requests, 
                       SUM(Quantity) AS Units_Requested,
                       SUM(CASE WHEN Status = 'Approved' THEN 1 ELSE 0 END) AS Approved,
                       SUM(CASE WHEN Status = 'Pending' THEN 1 ELSE 0 END) AS Pending
                FROM Blood_Request
                GROUP BY Blood_type
                ORDER BY Units_Requested DESC
                """
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                
                text_area.insert(tk.END, f"{'Blood Type':<15} {'Requests':<15} {'Units':<15} {'Approved':<15} {'Pending':<15}\n")
                text_area.insert(tk.END, "-" * 100 + "\n")
                
                if rows:
                    for row in rows:
                        text_area.insert(tk.END, f"{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<15} {str(row[3]):<15} {str(row[4]):<15}\n")
                else:
                    text_area.insert(tk.END, "No blood requests found.\n")
                
                
                # Donor Statistics
                text_area.insert(tk.END, "\n" + "=" * 100 + "\n")
                text_area.insert(tk.END, "TOP DONORS\n")
                text_area.insert(tk.END, "=" * 100 + "\n\n")
                
                query = """
                SELECT CONCAT(d.First_Name, ' ', d.Last_Name) AS Donor, 
                       d.Age, d.Gender,
                       COALESCE(COUNT(don.Donation_id), 0) AS Donations, 
                       COALESCE(SUM(don.Quantity), 0) AS Total_Units
                FROM Donor d
                LEFT JOIN Donation don ON d.D_id = don.D_id
                GROUP BY d.D_id, d.First_Name, d.Last_Name, d.Age, d.Gender
                ORDER BY Total_Units DESC
                LIMIT 10
                """
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                
                text_area.insert(tk.END, f"{'Donor Name':<30} {'Age':<10} {'Gender':<10} {'Donations':<15} {'Total Units':<15}\n")
                text_area.insert(tk.END, "-" * 100 + "\n")
                
                if rows:
                    for row in rows:
                        donor_name = str(row[0])[:29]  # Truncate long names
                        age = row[1] if row[1] else 0
                        gender = str(row[2])[:9] if row[2] else "N/A"
                        donations = row[3] if row[3] else 0
                        total_units = row[4] if row[4] else 0
                        text_area.insert(tk.END, f"{donor_name:<30} {age:<10} {gender:<10} {donations:<15} {total_units:<15}\n")
                else:
                    text_area.insert(tk.END, "No donor data available.\n")
                    
            except Exception as e:
                text_area.insert(tk.END, f"\nError generating statistics: {str(e)}\n")
                messagebox.showerror("Error", f"Failed to generate statistics: {str(e)}")
        
        tk.Button(stats_tab, text="🔄 Show Statistics", command=show_statistics,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).pack(pady=10)
        
        show_statistics()
    
    # ADVANCED QUERIES
    def advanced_queries(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="🔍 ADVANCED QUERIES", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        queries = [
            ("Donors Above Average", """
                SELECT d.D_id, d.First_Name, d.Last_Name, COUNT(don.Donation_id) AS Total_Donations
                FROM Donor d
                JOIN Donation don ON d.D_id = don.D_id
                GROUP BY d.D_id, d.First_Name, d.Last_Name
                HAVING COUNT(don.Donation_id) > (
                    SELECT AVG(donation_count)
                    FROM (
                        SELECT COUNT(*) AS donation_count
                        FROM Donation
                        GROUP BY D_id
                    ) AS avg_donations
                )
            """),
            ("Hospitals with Pending Requests", """
                SELECT h.H_id, h.Name, h.City
                FROM Hospital h
                WHERE h.H_id IN (
                    SELECT DISTINCT H_id
                    FROM Blood_Request
                    WHERE Status = 'Pending'
                )
            """),
            ("Eligible Donors for Next Donation", """
                SELECT d.D_id, d.First_Name, d.Last_Name, d.Age
                FROM Donor d
                WHERE d.D_id IN (
                    SELECT D_id
                    FROM Donation
                    GROUP BY D_id
                    HAVING MAX(Donation_date) < DATE_SUB(CURDATE(), INTERVAL 90 DAY)
                )
            """),
            ("Donors Who Haven't Donated", """
                SELECT d.D_id, d.First_Name, d.Last_Name
                FROM Donor d
                WHERE d.D_id NOT IN (
                    SELECT DISTINCT D_id
                    FROM Donation
                )
            """),
            ("Complete Donation Ecosystem", """
                SELECT don.Donation_id, don.Donation_date, don.Quantity,
                       CONCAT(d.First_Name, ' ', d.Last_Name) AS Donor_Name,
                       dc.Contact AS Donor_Contact,
                       h.Name AS Hospital_Name, hc.Contact AS Hospital_Contact,
                       r.Status AS Registration_Status
                FROM Donation don
                INNER JOIN Donor d ON don.D_id = d.D_id
                INNER JOIN Donor_Contact dc ON d.D_id = dc.D_id
                INNER JOIN Hospital h ON don.H_id = h.H_id
                INNER JOIN Hospital_Contact hc ON h.H_id = hc.H_id
                INNER JOIN Register r ON d.D_id = r.D_id AND h.H_id = r.H_id
                LIMIT 20
            """),
            ("Monthly Donation Trends", """
                SELECT YEAR(Donation_date) AS Year, MONTH(Donation_date) AS Month,
                       COUNT(*) AS Total_Donations, SUM(Quantity) AS Total_Units,
                       COUNT(DISTINCT D_id) AS Unique_Donors
                FROM Donation
                GROUP BY YEAR(Donation_date), MONTH(Donation_date)
                ORDER BY Year DESC, Month DESC
            """)
        ]
        
        for query_name, query_sql in queries:
            tab = tk.Frame(notebook, bg=self.bg_color)
            notebook.add(tab, text=query_name)
            
            # Query display
            query_frame = tk.Frame(tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
            query_frame.pack(fill=tk.X, padx=10, pady=10)
            
            query_text = scrolledtext.ScrolledText(query_frame, height=8, font=("Courier", 9))
            query_text.pack(fill=tk.X, padx=10, pady=10)
            query_text.insert(tk.END, query_sql.strip())
            query_text.config(state=tk.DISABLED)
            
            # Results frame
            result_frame = tk.Frame(tab)
            result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            scrollbar = ttk.Scrollbar(result_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            result_tree = ttk.Treeview(result_frame, yscrollcommand=scrollbar.set)
            scrollbar.config(command=result_tree.yview)
            result_tree.pack(fill=tk.BOTH, expand=True)
            
            def execute_query(sql=query_sql, tree=result_tree):
                try:
                    self.cursor.execute(sql)
                    rows = self.cursor.fetchall()
                    
                    # Clear previous results
                    for item in tree.get_children():
                        tree.delete(item)
                    
                    if rows:
                        # Setup columns
                        columns = [desc[0] for desc in self.cursor.description]
                        tree['columns'] = columns
                        tree['show'] = 'headings'
                        
                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=120)
                        
                        # Insert data
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                        
                        messagebox.showinfo("Success", f"Query executed successfully! {len(rows)} rows returned.")
                    else:
                        messagebox.showinfo("Info", "Query executed but no results found.")
                except Exception as e:
                    messagebox.showerror("Error", f"Query execution failed: {str(e)}")
            
            tk.Button(tab, text="▶ Execute Query", command=lambda sql=query_sql, tree=result_tree: execute_query(sql, tree),
                     bg=self.primary_color, fg="white", font=("Arial", 11, "bold"),
                     cursor="hand2", padx=20, pady=8).pack(pady=5)
    
    # PROCEDURES AND FUNCTIONS
    def test_procedures_functions(self):
        self.clear_content()
        
        title = tk.Label(self.content_frame, text="⚙️ PROCEDURES & FUNCTIONS", 
                        font=("Arial", 18, "bold"), bg=self.bg_color)
        title.pack(pady=10)
        
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Functions Tab
        func_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(func_tab, text="Test Functions")
        
        func_frame = tk.Frame(func_tab, bg=self.bg_color)
        func_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        result_text = scrolledtext.ScrolledText(func_frame, height=25, font=("Courier", 10))
        result_text.pack(fill=tk.BOTH, expand=True)
        
        def test_functions():
            result_text.delete(1.0, tk.END)
            
            # Test Function 1: Check donor eligibility
            result_text.insert(tk.END, "=" * 100 + "\n")
            result_text.insert(tk.END, "FUNCTION 1: Check Donor Eligibility\n")
            result_text.insert(tk.END, "=" * 100 + "\n\n")
            
            query = """
            SELECT D_id, First_Name, Last_Name, Age, fn_check_donor_eligibility(Age) AS Eligibility
            FROM Donor
            """
            self.cursor.execute(query)
            result_text.insert(tk.END, f"{'ID':<10} {'Name':<25} {'Age':<10} {'Eligibility':<20}\n")
            result_text.insert(tk.END, "-" * 100 + "\n")
            for row in self.cursor.fetchall():
                name = f"{row[1]} {row[2]}"
                result_text.insert(tk.END, f"{row[0]:<10} {name:<25} {row[3]:<10} {row[4]:<20}\n")
            
            # Test Function 2: Total donations by donor
            result_text.insert(tk.END, "\n" + "=" * 100 + "\n")
            result_text.insert(tk.END, "FUNCTION 2: Total Donations by Donor\n")
            result_text.insert(tk.END, "=" * 100 + "\n\n")
            
            query = """
            SELECT D_id, First_Name, Last_Name, fn_get_donor_total_donations(D_id) AS Total_Donations
            FROM Donor
            """
            self.cursor.execute(query)
            result_text.insert(tk.END, f"{'ID':<10} {'Name':<30} {'Total Donations':<20}\n")
            result_text.insert(tk.END, "-" * 100 + "\n")
            for row in self.cursor.fetchall():
                name = f"{row[1]} {row[2]}"
                result_text.insert(tk.END, f"{row[0]:<10} {name:<30} {row[3]:<20}\n")
            
            # Test Function 3: Days since last donation
            result_text.insert(tk.END, "\n" + "=" * 100 + "\n")
            result_text.insert(tk.END, "FUNCTION 3: Days Since Last Donation & Donor Status\n")
            result_text.insert(tk.END, "=" * 100 + "\n\n")
            
            query = """
            SELECT D_id, First_Name, Last_Name, 
                   fn_days_since_last_donation(D_id) AS Days_Since,
                   fn_get_donor_status(D_id) AS Status
            FROM Donor
            """
            self.cursor.execute(query)
            result_text.insert(tk.END, f"{'ID':<10} {'Name':<25} {'Days Since':<15} {'Status':<30}\n")
            result_text.insert(tk.END, "-" * 100 + "\n")
            for row in self.cursor.fetchall():
                name = f"{row[1]} {row[2]}"
                result_text.insert(tk.END, f"{row[0]:<10} {name:<25} {row[3]:<15} {row[4]:<30}\n")
            
            # Test Function 4: Hospital total units
            result_text.insert(tk.END, "\n" + "=" * 100 + "\n")
            result_text.insert(tk.END, "FUNCTION 4: Hospital Total Blood Units\n")
            result_text.insert(tk.END, "=" * 100 + "\n\n")
            
            query = """
            SELECT H_id, Name, fn_hospital_total_units(H_id) AS Total_Units
            FROM Hospital
            """
            self.cursor.execute(query)
            result_text.insert(tk.END, f"{'ID':<10} {'Hospital Name':<35} {'Total Units':<20}\n")
            result_text.insert(tk.END, "-" * 100 + "\n")
            for row in self.cursor.fetchall():
                result_text.insert(tk.END, f"{row[0]:<10} {str(row[1]):<35} {row[2]:<20}\n")
            
            # Test Function 5: Pending requests count
            result_text.insert(tk.END, "\n" + "=" * 100 + "\n")
            result_text.insert(tk.END, "FUNCTION 5: Pending Requests Count\n")
            result_text.insert(tk.END, "=" * 100 + "\n\n")
            
            query = """
            SELECT H_id, Name, fn_pending_requests_count(H_id) AS Pending_Requests
            FROM Hospital
            """
            self.cursor.execute(query)
            result_text.insert(tk.END, f"{'ID':<10} {'Hospital Name':<35} {'Pending Requests':<20}\n")
            result_text.insert(tk.END, "-" * 100 + "\n")
            for row in self.cursor.fetchall():
                result_text.insert(tk.END, f"{row[0]:<10} {str(row[1]):<35} {row[2]:<20}\n")
        
        tk.Button(func_tab, text="🔄 Test All Functions", command=test_functions,
                 bg=self.primary_color, fg="white", font=("Arial", 12, "bold"),
                 cursor="hand2", padx=20, pady=10).pack(pady=10)
        
        test_functions()
        
        # Available Donors Procedure Tab
        proc_tab = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(proc_tab, text="Available Donors by Blood Type")
        
        input_frame = tk.Frame(proc_tab, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        input_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(input_frame, text="Blood Type:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=0, padx=10, pady=10)
        blood_type_combo = ttk.Combobox(input_frame, 
                                       values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                                       font=("Arial", 11), width=15)
        blood_type_combo.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(input_frame, text="Hospital ID:", font=("Arial", 11),
                bg=self.secondary_color).grid(row=0, column=2, padx=10, pady=10)
        h_id_entry = tk.Entry(input_frame, font=("Arial", 11), width=15)
        h_id_entry.grid(row=0, column=3, padx=10, pady=10)
        
        result_frame = tk.Frame(proc_tab)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(result_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("Donor ID", "First Name", "Last Name", "Age", "Gender", "Contact", "Last Donation")
        proc_tree = ttk.Treeview(result_frame, columns=columns, show="headings",
                                yscrollcommand=scrollbar.set)
        
        for col in columns:
            proc_tree.heading(col, text=col)
            proc_tree.column(col, width=120)
        
        scrollbar.config(command=proc_tree.yview)
        proc_tree.pack(fill=tk.BOTH, expand=True)
        
        def get_available_donors():
            try:
                for item in proc_tree.get_children():
                    proc_tree.delete(item)
                
                # Note: This procedure doesn't exist in the schema, using equivalent query
                query = """
                SELECT d.D_id, d.First_Name, d.Last_Name, d.Age, d.Gender, 
                       dc.Contact, r.Last_donation_date
                FROM Donor d
                JOIN Donor_Contact dc ON d.D_id = dc.D_id
                JOIN Register r ON d.D_id = r.D_id AND r.H_id = %s
                WHERE r.Status = 'Active'
                AND (r.Last_donation_date IS NULL OR 
                     DATEDIFF(CURDATE(), r.Last_donation_date) >= 90)
                """
                self.cursor.execute(query, (int(h_id_entry.get()),))
                
                rows = self.cursor.fetchall()
                if rows:
                    for row in rows:
                        proc_tree.insert("", tk.END, values=row)
                    messagebox.showinfo("Success", f"Found {len(rows)} available donors!")
                else:
                    messagebox.showinfo("Info", "No available donors found.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to fetch donors: {str(e)}")
        
        tk.Button(input_frame, text="Get Available Donors", command=get_available_donors,
                 bg=self.primary_color, fg="white", font=("Arial", 11),
                 cursor="hand2", padx=15, pady=5).grid(row=0, column=4, padx=10, pady=10)
    
    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()


# Main execution
if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Modern theme
    app = BloodDonationPlatform(root)
    root.mainloop()
