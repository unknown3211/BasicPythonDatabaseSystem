import customtkinter as ctk
from gui import *

s_width = 800
s_height = 600

app = ctk.CTk()
app.title("MYSQL Database System")
app.geometry(f"{s_width}x{s_height}")

HandleConnect(app)
handleQuery(app)

app.mainloop()