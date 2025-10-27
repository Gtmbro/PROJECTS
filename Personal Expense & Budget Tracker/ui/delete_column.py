"""
Features of delete_column function:-
1. Gives user option to delete whole column ( curently not available ) or just their values.
2. If user selectes option to delete the values of a column,
   then gives the option to select the available column (excluding Index column),
   then deletes the values of a corresponding column.
"""
def delete_column():
    file_sorter()

    win = ctk.CTkToplevel(root)
    win.title("Delete Column")

    input_frame = ctk.CTkFrame(win)
    input_frame.pack(fill="both", expand=True)

    df = pd.read_csv(filename)

    available_columns = df.columns.tolist()
    columns_count = len(available_columns)

    #input_frame configuration
    for i in range(4):
        input_frame.rowconfigure(i, weight=1)
        input_frame.columnconfigure(i, weight=1)

    '''Deleting whole column might cause error apology'''
    def apology():
        apology = choice.get().strip()

        messagebox.showwarning("Warning",f"Request '{apology}' might cause an error!!")
        win.destroy()

    #To delete whole column ( Not recommended, so not available )
    def delete_whole_column():
        file_sorter()

        win2 = ctk.CTkToplevel(win)
        win2.title("Delete Whole Column")

        columns_display_frame = ctk.CTkFrame(win2)
        columns_display_frame.pack(fill="both", expand=True)

        delete_whole_column_frame = ctk.CTkFrame(win2)
        delete_whole_column_frame.pack(fill="both", expand=True)

        #columns_display_frame configuration
        for i in range(columns_count+1):
            columns_display_frame.rowconfigure(i, weight=1)
            columns_display_frame.columnconfigure(i, weight=1)

        #delete_whole_column_frame configuration
        for i in range(1):
            delete_whole_column_frame.rowconfigure(i, weight=1)
            delete_whole_column_frame.columnconfigure(i, weight=1)

        #To execute the operation
        def validate_and_submit():
            try:
                df = pd.read_csv(filename)

                value = choice.get()

                df = df.drop(columns = value)

                df.to_csv(filename, index=False)

                messagebox.showinfo("Success",f"Column '{value}' has been deleted successfully.")
                win2.destroy()

                file_correcter()

            except ValueError:
                win2.destroy()
                messagebox.showwarning("Error","Some error occured!!")

        try:
            choice = ctk.StringVar(value="")

            ctk.CTkLabel(columns_display_frame, text="Choose the column to delete:").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

            for i, column in enumerate(available_columns, start=1):
                ctk.CTkRadioButton(columns_display_frame, text=f"{i}. {column}", variable=choice, value=column, command=validate_and_submit).grid(row=i, column=0, sticky='nsew', padx=10, pady=10)

            ctk.CTkButton(delete_whole_column_frame, text="Exit", command=lambda:destroyer(win2)).grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
            
        except ValueError:
            win.destroy()
            messagebox.showwarning("Error","Some error occured!!")

    #To delete the values only
    def delete_values_only():
        file_sorter()

        win2 = ctk.CTkToplevel(win)
        win2.title("Delete Values Only")

        columns_display_frame = ctk.CTkFrame(win2)
        columns_display_frame.pack(fill="both", expand=True)

        delete_values_only_frame = ctk.CTkFrame(win2)
        delete_values_only_frame.pack(fill="both", expand=True)

        #columns_display_frame configuration
        for i in range(columns_count+1):
            columns_display_frame.rowconfigure(i, weight=1)
            columns_display_frame.columnconfigure(i, weight=1)

        #delete_values_only_frame configuration
        for i in range(1):
            delete_values_only_frame.rowconfigure(i, weight=1)
            delete_values_only_frame.columnconfigure(i, weight=1)

        #To execute the operation
        def validate_and_submit():
            try:
                df = pd.read_csv(filename)

                column = choice.get()

                df[column] = ""

                df.to_csv(filename, index=False)

                messagebox.showinfo("Success",f"Values of column '{column}' has been deleted successfully.")
                win2.destroy()

                file_correcter()

            except ValueError:
                win2.destroy()
                messagebox.showwarning("Error","Some error occured!!")

        try:
            choice = ctk.StringVar(value="")

            ctk.CTkLabel(columns_display_frame, text="Choose the column whose values you wanna delete:").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

            for i,column in enumerate(available_columns, start=1):
                if column != "Index":
                    ctk.CTkRadioButton(columns_display_frame, text=column,variable=choice, value=column, command=validate_and_submit).grid(row=i, column=0, sticky='nsew', padx=10, pady=10)

            ctk.CTkButton(delete_values_only_frame, text="Exit", command=lambda:destroyer(win2)).grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        except ValueError:
            win2.destroy()
            messagebox.showwarning("Error","Some error occured!!")

    try:
        choice = ctk.StringVar(value="")

        ctk.CTkLabel(input_frame, text="Choose one option: ").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkRadioButton(input_frame, text="Delete whole column",variable=choice, value="Delete whole column", command=apology).grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        ctk.CTkRadioButton(input_frame, text="Delete the values only", variable=choice, value="Delete values only", command=delete_values_only).grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkButton(input_frame, text="Exit", command = lambda:destroyer(win)).grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

    except ValueError:
        messagebox.showwarning("Error","Error occured..")
        win.destroy()
