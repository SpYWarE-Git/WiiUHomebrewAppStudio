import tkinter as tk

# Functions

# Aroma Plugin

# Metadata
def apSetMetadata():
    name = name_entry.get()
    author = author_entry.get()
    version = version_entry.get()
    desc = desc_entry.get()
    print(f"Name: {name}, Author: {author}, Version: {version}, Desc.: {desc}.")
    aromaplmeta.destroy()

# Back
def apBack():
    aromaplmeta.destroy()
    selecthbtype.deiconify()

# Apps

# Only legacy

# Metadata
def olMetadata():
    selecthbtype.destroy()

# Windows

# Aroma Plugin

# Metadata
def apMetadata():
    global aromaplmeta, name_entry, author_entry, version_entry, desc_entry
    selecthbtype.withdraw()
    aromaplmeta = tk.Tk()
    aromaplmeta.title("Wii U Homebrew App Studio")
    aromaplmeta.geometry("350x270")
    tk.Label(aromaplmeta, text="Name of app/plugin").pack()
    name_entry = tk.Entry(aromaplmeta)
    name_entry.pack()
    tk.Label(aromaplmeta, text="Author").pack()
    author_entry = tk.Entry(aromaplmeta)
    author_entry.pack()
    tk.Label(aromaplmeta, text="Version (v*.*.*)").pack()
    version_entry = tk.Entry(aromaplmeta)
    version_entry.pack()
    tk.Label(aromaplmeta, text="Description").pack()
    desc_entry = tk.Entry(aromaplmeta)
    desc_entry.pack()
    tk.Button(aromaplmeta, text="Set metadata", command=apSetMetadata).pack(pady=10)
    tk.Button(aromaplmeta, text="Back", command=apBack).pack(pady=10)

# Legacy

# Metadata

# Select type of HOMEBREW
selecthbtype = tk.Tk()
selecthbtype.title("Wii U Homebrew App Studio")
selecthbtype.geometry("350x205")
tk.Label(selecthbtype, text="Select type of Homebrew").pack()
tk.Button(selecthbtype, text="Only legacy", command=olMetadata).pack()
tk.Button(selecthbtype, text="Aroma Plugin", command=apMetadata).pack()

# Main loop
selecthbtype.mainloop()
