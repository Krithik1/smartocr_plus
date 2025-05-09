import re
import tkinter as tk
from tkinter import messagebox
import webbrowser
from smart_ocr.translate import translate_text
import sv_ttk

def callback_open_url(url):
    webbrowser.open(url)

def callback_address(address):
    google_maps_url = f"https://www.google.com/maps/search/{address.replace(' ', '+')}"
    webbrowser.open(google_maps_url)
    
def process_links_and_addresses(text):
    url_pattern = r'(https?://(?:www\.)?[a-zA-Z0-9./?=&%_-]+)'
    address_pattern = r'[0-9A-Za-z]+ [a-zA-Z, \n]+(?:\d{5}(?:-\d{4})?|[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d)'

    links = re.findall(url_pattern, text)  # Find all URLs
    addresses = re.findall(address_pattern, text)  # Find all addresses
    addresses = list(map(lambda x: x.replace('\n', ' '), addresses))
    return links, addresses

def show_popup(text):
    root = tk.Tk()
    root.title("SmartOCR+")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()
    
    links, addresses = process_links_and_addresses(text)

    tk.Label(frame, text="Extracted Text:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
    text_box = tk.Text(frame, wrap="word", height=10, width=60)
    text_box.insert("1.0", text)
    text_box.config(state="disabled")
    text_box.pack()
    
    if len(links) > 0:
        tk.Label(frame, text="Extracted Links:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        for link in links:
            link_label = tk.Label(frame, text=link, font=("Segoe UI", 10, "bold"), fg="blue", cursor="hand2")
            link_label.pack(pady=(0, 10))
            link_label.bind("<Button-1>", lambda e, url=link: callback_open_url(url))

    if len(addresses) > 0:
        tk.Label(frame, text="Extracted Addresses:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        for address in addresses:
            address_label = tk.Label(frame, text=address, font=("Segoe UI", 10, "bold"), fg="blue", cursor="hand2")
            address_label.pack(pady=(0, 10))
            address_label.bind("<Button-1>", lambda e, address=address: callback_address(address))

    translated = translate_text(text)
    if translated:
        tk.Label(frame, text="Translated Text:", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10,0))
        trans_box = tk.Text(frame, wrap="word", height=10, width=60)
        trans_box.insert("1.0", translated)
        trans_box.config(state="disabled")
        trans_box.pack()
        
    def find_text(event=None):
        search_popup = tk.Toplevel(root)
        search_popup.title("Find Text")

        tk.Label(search_popup, text="Find:").pack(padx=10, pady=5)
        search_entry = tk.Entry(search_popup, width=30)
        search_entry.pack(padx=10, pady=5)

        def highlight():
            search_term = search_entry.get()
            search_popup.destroy()
            text_box.tag_remove("highlight", "1.0", "end")
            if search_term:
                start_pos = "1.0"
                while True:
                    start_pos = text_box.search(search_term, start_pos, stopindex="end")
                    if not start_pos:
                        break
                    end_pos = f"{start_pos}+{len(search_term)}c"
                    text_box.tag_add("highlight", start_pos, end_pos)
                    start_pos = end_pos
                text_box.tag_config("highlight", background="yellow", foreground="black")

        tk.Button(search_popup, text="Find", command=highlight).pack(pady=10)
        search_entry.bind("<Return>", lambda event: highlight())

    root.bind("<Control-f>", find_text)

    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=10)

    def copy_text():
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")

    def search_text():
        query = text.strip().replace('\n', ' ')
        webbrowser.open(f"https://www.google.com/search?q={query}")

    def define_word():
        word = text.strip().split()[0]
        webbrowser.open(f"https://www.dictionary.com/browse/{word}")

    tk.Button(btn_frame, text="Copy", command=copy_text).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Search", command=search_text).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Find", command=find_text).pack(side="left", padx=5)

    if len(text.strip().split()) == 1:
        tk.Button(btn_frame, text="Define", command=define_word).pack(side="left", padx=5)
        
    sv_ttk.set_theme("dark")

    root.mainloop()
