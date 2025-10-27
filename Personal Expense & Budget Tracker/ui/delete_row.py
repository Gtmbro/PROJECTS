"""
Features of delete_row function:-
1. Lets user select the category they want to delete and delets the corresponding row.
"""
def delete_row():
    file_sorter()

    win = ctk.CTkToplevel(root)
    win.title("Delete Row")

    delete_row_frame = ctk.CTkFrame(win)
    delete_row_frame.pack(fill="both", expand=True)

    df = pd.read_csv(filename)

    available_rows = df["Category"].values
    rows_count = len(available_rows)

    available_indexes = df["Index"].values

    #delete_row_frame configuration
    for i in range(rows_count+3):
        delete_row_frame.rowconfigure(i, weight=1)
        delete_row_frame.rowconfigure(i, weight=1)

    #To execute the operation
    def validate_and_submit():
        try:
            df = pd.read_csv(filename)

            index = index_var.get()

            df = df[df["Index"] != index]
            df.to_csv(filename, index=False)

            file_correcter()

            win.destroy()
            messagebox.showinfo("Success",f"Row with index '{index}' has been deleted.")

        except ValueError:
            win.destroy()
            messagebox.showwarning("Error","Some error occured!!")

    try:
        index_var = ctk.IntVar()

        ctk.CTkLabel(delete_row_frame, text="Choose the category of the row you want to delete:").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        for i, category in enumerate(available_rows, start=1):
            ctk.CTkRadioButton(delete_row_frame, text=category, variable=index_var, value=i).grid(row=i, column=0, sticky='nsew', padx=10, pady=10)

        r = rows_count + 1

        ctk.CTkButton(delete_row_frame, text="Submit", command=validate_and_submit).grid(row=r, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkButton(delete_row_frame, text="Exit", command = lambda:destroyer(win)).grid(row=r+1, column=0, sticky='nsew', padx=5, pady=5)

    except ValueError:
        messagebox.showwarning("Error","Error occured!!")
        win.destroy()
