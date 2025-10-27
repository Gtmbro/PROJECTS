"""
Features of show_total function:-
1. Gives users 2 options:
   -> Compare amounts of the categories in 7 available graphs, which includes 2 features:
        - Select the categories.
        - Include all categories.

   -> Show the total spent.
2. If user chooses to compare amounts in graph,
   lets user select the graph they want.
"""
def show_total():
    win = ctk.CTkToplevel(root)
    win.title("Show Total")

    input_frame = ctk.CTkFrame(win)
    input_frame.pack(fill="both", expand=True)

    total_display_frame = ctk.CTkFrame(win)
    total_display_frame.pack(fill="both", expand=True)

    #input_frame configuration
    for i in range(4):
        input_frame.rowconfigure(i, weight=1)
        input_frame.columnconfigure(i, weight=1)

    #total_display_frame configuration
    for i in range(1):
        total_display_frame.rowconfigure(i, weight=1)
        total_display_frame.columnconfigure(i, weight=1)

    #To display the comparison in graph
    def graph_deployer():
        win2 = ctk.CTkToplevel(win)
        win2.title("Compare Categories In Graph")

        input_frame = ctk.CTkFrame(win2)
        input_frame.pack(fill="both", expand=True)

        bars = ["pie","line","bar","box","barh","area","hist"]
        bars_count = len(bars)

        #input_frame configuration
        for i in range(bars_count+4):
            input_frame.rowconfigure(i, weight=1)
            input_frame.columnconfigure(i, weight=1)

        #To deploy the graph
        def validate_and_submit():
            try:
                graph = graph_type.get()
                category_choice = category_selection_var.get()

                if not graph:
                    messagebox.showwarning("Error", "Please select a graph type.")
                    return

                df = pd.read_csv(filename)
                available_categories = df["Category"].unique()

                # Create a new window
                win3 = ctk.CTkToplevel(win2)
                win3.title("Deploy Graph")

                graph_deploy_frame = ctk.CTkFrame(win3)
                graph_deploy_frame.pack(fill="both", expand=True)

                if category_choice == "Select categories":
                    ctk.CTkLabel(graph_deploy_frame, text="Select categories:").grid(row=0, column=0, padx=10, pady=10)
                    selected_vars = {}

                    for i, category in enumerate(available_categories, start=1):
                        var = ctk.BooleanVar()
                        ctk.CTkCheckBox(graph_deploy_frame, text=category, variable=var).grid(row=i, column=0, padx=10, pady=5)
                        selected_vars[category] = var

                    def deploy_graph():
                        selected = [cat for cat, var in selected_vars.items() if var.get()]
                        if not selected:
                            messagebox.showwarning("Error", "Please select at least one category.")
                            return

                        data = df[df["Category"].isin(selected)].groupby("Category")["Amount"].sum()

                        plt.figure()
                        if graph == "pie":
                            data.plot(kind="pie", autopct='%1.1f%%')
                        else:
                            data.plot(kind=graph)

                        plt.title("Category vs Amount")
                        plt.xlabel("Category")
                        plt.ylabel("Amount")
                        plt.show()

                    ctk.CTkButton(graph_deploy_frame, text="Show Graph", command=deploy_graph).grid(row=len(available_categories)+1, column=0, padx=10, pady=10)
                    ctk.CTkButton(graph_deploy_frame, text="Exit", command=lambda: destroyer(win3)).grid(row=len(available_categories)+2, column=0, padx=10, pady=10)

                else:
                    data = df.groupby("Category")["Amount"].sum()
                    plt.figure()
                    if graph == "pie":
                        data.plot(kind="pie", autopct='%1.1f%%')
                    else:
                        data.plot(kind=graph)
                    plt.title("Category vs Amount")
                    plt.xlabel("Category")
                    plt.ylabel("Amount")
                    plt.show()

            except Exception as e:
                messagebox.showwarning("Error", f"Some error occurred: {e}")
                if 'win3' in locals():
                    win3.destroy()

        try:
            #Categories selection
            category_selection_var = ctk.StringVar()

            ctk.CTkLabel(input_frame, text="Choose appropriate option:").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

            ctk.CTkRadioButton(input_frame, text="Select Categories", variable=category_selection_var, value="Select categories").grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
            ctk.CTkRadioButton(input_frame, text="Include all categories", variable=category_selection_var, value="Include all categories").grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

            #Graph type selection
            graph_type = ctk.StringVar()

            ctk.CTkLabel(input_frame, text="Select the graph type:").grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

            for i, bar in enumerate(bars, start=4):
                ctk.CTkRadioButton(input_frame, text=bar.capitalize(), variable=graph_type, value=bar).grid(row=i, column=0, sticky='nsew', padx=10, pady=10)

            r = bars_count + 4
            ctk.CTkButton(input_frame, text="Submit", command = validate_and_submit).grid(row=r, column=0, sticky='nsew', padx=10, pady=10)

            ctk.CTkButton(input_frame, text="Exit", command = lambda:destroyer(win2)).grid(row=r, column=1, sticky='nsew', padx=10, pady=10)

        except ValueError:
            win2.destroy()
            messagebox.showwarning("Error","Some error occured!!")

    #To simply display the total spent
    def total_counter():
        try:
            df = pd.read_csv(filename)

            Amounts = df["Amount"]
            total = 0

            for Amount in Amounts:
                total += Amount
            
            ctk.CTkLabel(total_display_frame, text=f"Your total spent is {total}").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        except ValueError:
            messagebox.showwarning("Error","Error occured!!")
            win.destroy()

    try:
        ctk.CTkLabel(input_frame, text="Choose appropriate option: ").grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkRadioButton(input_frame, text="See category-wise spendings in graph", command=graph_deployer).grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        ctk.CTkRadioButton(input_frame, text="See just total number", command=total_counter).grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        ctk.CTkButton(input_frame, text="Exit", command = lambda:destroyer(win)).grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        
    except ValueError:
        messagebox.showwarning("Error","Error occured during the process!!")
        win.destroy()
