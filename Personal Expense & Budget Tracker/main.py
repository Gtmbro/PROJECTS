import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("600x400")
root.title("Personal Expense and Budget Tracker")

#root configuration
for i in range(7):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)


"""
Features available:-
1. Add new category.
2. Edit the values of any category that user wants.
3. Delete any row that user wants.
4. Delete the values of any column.
   Deleting any column is not available for now.
5. Lets user compare amounts of categories in graph or,
   Simply see the total spent.
"""
ctk.CTkLabel(root, text="Choose preferred action:").grid(row=0, column=1, sticky='nsew',padx=10, pady=10)

ctk.CTkRadioButton(root, text="Add a category", command=add_category).grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
ctk.CTkRadioButton(root, text="Edit the values of a category", command=edit_category).grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
ctk.CTkRadioButton(root, text="Delete a row(horizontal)", command=delete_row).grid(row=3, column=0, sticky='nsew', padx=5, pady=5)
ctk.CTkRadioButton(root, text="Delete a column(vertical)", command=delete_column).grid(row=4, column=0, sticky='nsew', padx=5, pady=5)
ctk.CTkRadioButton(root, text="Show total spent", command=show_total).grid(row=5, column=0, sticky='nsew', padx=5, pady=5)

#Option to exit the program
ctk.CTkButton(root, text="Exit", command=lambda:destroyer(root)).grid(row=6, column=0, sticky='nsew', padx=5, pady=5)

root.mainloop()
