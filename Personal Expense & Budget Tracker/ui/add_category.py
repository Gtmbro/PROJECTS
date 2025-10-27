"""
Features of add_category function:-
1. Takes category, amount, date and notes from users via submit button.
   Here, category and amount are required and date and notes are optional.
"""
def add_category():
    win = ctk.CTkToplevel(root)
    win.title("Add Category")

    add_category_frame = ctk.CTkFrame(win)
    add_category_frame.pack(fill="both", expand=True)

    #add_category_frame configuration
    for i in range(7):
        add_category_frame.rowconfigure(i, weight=1)
        add_category_frame.rowconfigure(i, weight=1)

    #To execute the operation
    def validate_and_submit():
        try:
            category = category_entry.get().strip().capitalize()
            amount = float(amount_entry.get())
            date = date_entry.get().strip()
            notes = note_entry.get().strip()

            if not category:
                messagebox.showwarning("Error","Category is needed!!")
                return 
            
            if not amount:
                messagebox.showwarning("Error","Amount is needed!!")
                return 
            
            if not date:
                current_time = datetime.now()
                date = current_time.strftime("%Y:%m:%d")

            if not notes:
                notes = " "

            index = index_finder()
            c.add_entry(index, date, category, amount, notes)
            c.create_file()

            messagebox.showinfo("Success",f"Category '{category}' has been added..")
            win.destroy()

        except ValueError:
            messagebox.showwarning("Error","Error occured!!")
            win.destroy()

    try:
        ctk.CTkLabel(add_category_frame, text="Enter the appropriate values: ").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        category_entry = ctk.CTkEntry(add_category_frame, placeholder_text="Category")
        category_entry.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        validate_cmd = win.register(validate_float)

        amount_entry = ctk.CTkEntry(add_category_frame, placeholder_text="Amount")
        amount_entry.configure(validate="key", validatecommand = (validate_cmd, "%P"))
        amount_entry.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkLabel(add_category_frame, text="Optional entries:-").grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        
        date_entry = ctk.CTkEntry(add_category_frame, placeholder_text="Date in YYYY:MM:DD format")
        date_entry.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)

        note_entry = ctk.CTkEntry(add_category_frame, placeholder_text="Notes")
        note_entry.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)
        
        ctk.CTkButton(add_category_frame, text="Add", command=validate_and_submit).grid(row=6, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkButton(add_category_frame, text="Exit", command = lambda:destroyer(win)).grid(row=6, column=1, sticky='nsew', padx=10, pady=10)
 
    except ValueError:
        messagebox.showwarning("Error","Some error occured!!")
        win.destroy()
