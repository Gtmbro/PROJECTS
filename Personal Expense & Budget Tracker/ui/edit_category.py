"""
Features of edit_category function:-
1. Gives options to choose from available indexes and columns (except Index and Date) and asks for new value.
2. Giving new value is required.
"""
def edit_category():
    file_sorter()

    win = ctk.CTkToplevel(root)
    win.title("Edit Category")

    df = pd.read_csv(filename)

    indexes_frame = ctk.CTkFrame(win)
    indexes_frame.pack(fill="both", expand=True)

    columns_frame = ctk.CTkFrame(win)
    columns_frame.pack(fill="both", expand=True)

    submit_frame = ctk.CTkFrame(win)
    submit_frame.pack(fill="both", expand=True)

    df = pd.read_csv(filename)

    available_indexes = df["Index"].values
    indexes_count = len(available_indexes)

    available_columns = df.columns
    columns_count = len(available_columns)

    #indexes_frame configuration
    for i in range(indexes_count+1):
        indexes_frame.rowconfigure(i, weight=1)
        indexes_frame.rowconfigure(i, weight=1)

    #columns_frame configuration
    for i in range(columns_count+1):
        columns_frame.rowconfigure(i, weight=1)
        columns_frame.rowconfigure(i, weight=1)

    #submit_frame configuration
    for i in range(2):
        submit_frame.rowconfigure(i, weight=1)
        submit_frame.rowconfigure(i, weight=1)

    #To execute the operation
    def validate_and_submit():
        try:
            df = pd.read_csv(filename)

            index = index_var.get()
            column = column_var.get()
            value = value_var.get().strip().capitalize()

            if not value:
                messagebox.showwarning("Error","New value not entered..\nPlease enter everything..")
                return

            c.edit_entry(index, column, value)
            win.destroy()

            file_correcter()

            messagebox.showinfo("Success",f"Updated column '{column}' of index '{index}' to '{value}'.")

        except ValueError:
            messagebox.showwarning("Error","Error occured!!")
            win.destroy()

    try:
        validate_cmd = win.register(validate_int)

        index_var = ctk.IntVar()
        ctk.CTkLabel(indexes_frame, text="Choose the index:").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        for i,index in enumerate(available_indexes, start=1):
            ctk.CTkRadioButton(indexes_frame, text=index, variable=index_var, value=index).grid(row=i, column=0, sticky='nsew', padx=10, pady=10)

        column_var = ctk.StringVar()
        ctk.CTkLabel(columns_frame, text="Choose the column: ").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        for i,column in enumerate(available_columns, start=1):
            if column != "Index" and column != "Date":
                ctk.CTkRadioButton(columns_frame, text=column, variable=column_var, value=column).grid(row=i, column=0, sticky='nsew', padx=10, pady=10)

        value_var = ctk.StringVar()
        ctk.CTkLabel(submit_frame, text="Enter new value: ").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        ctk.CTkEntry(submit_frame, textvariable=value_var).grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        
        ctk.CTkButton(submit_frame, text="Submit", command=validate_and_submit).grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkButton(submit_frame, text="Exit", command = lambda:destroyer(win)).grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

    except ValueError:
        messagebox.showwarning("Error","Error detected..")
        win.destroy()
