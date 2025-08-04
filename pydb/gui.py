import customtkinter as ctk
from files import *
from db import *

dbconnect = None
query_result = None

def HandleConnect(app):
    def on_button_click():
        global dbconnect
        dbconnect = connect_to_db(
            dbinfo["db"]["host"],
            dbinfo["db"]["user"],
            dbinfo["db"]["password"],
            dbinfo["db"]["database"]
        )

    button = ctk.CTkButton(app, text="Connect To Database", command=on_button_click)
    button.pack(pady=20)

def handleQuery(app):
    def on_fetch_click():
        global query_result
        query = q_entry.get()
        if dbconnect:
            query_result = select_from_db(dbconnect, query)
            if query_result:
                print("Results:", query_result)
            else:
                print("No Results Found")
        else:
            print("Database Not Connected")

    ctk.CTkLabel(app, text="Enter Query (Select Only)").pack()
    q_entry = ctk.CTkEntry(app)
    q_entry.pack()

    button = ctk.CTkButton(app, text="Fetch Data", command=on_fetch_click)
    button.pack(pady=20)