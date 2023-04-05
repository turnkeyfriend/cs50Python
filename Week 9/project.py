import googlemaps
import requests
import html5lib
import bs4
import sqlite3
import os
import tkinter as tk
import webbrowser
import os.path

db_file_path = os.path.join(os.getcwd(), "state_forests.db")

if os.path.isfile(db_file_path):
    print("state_forests.db already exists, skipping database creation.")
else:
    gmaps = googlemaps.Client(key="INSERT API KEY HERE")

    db_file_path = os.path.join(os.getcwd(), "state_forests.db")
    conn = sqlite3.connect(db_file_path)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS state_forests
                (name text, url text, region text, latitude real, longitude real, driving_distance real, camping text)""")

    class Region():
        def __init__(self, regionsite):
            self.regionsite = regionsite
            self.state_forests = {}

        def get_state_forest_locations(self, origin):
            for name, url in self.state_forests.items():
                places_result = gmaps.places(f"{name}, new york")
                if places_result["results"]:
                    latitude = places_result["results"][0]["geometry"]["location"]["lat"]
                    longitude = places_result["results"][0]["geometry"]["location"]["lng"]

                    distance_matrix = gmaps.distance_matrix(origins=origin,
                                                            destinations=f"{latitude},{longitude}",
                                                            mode="driving",
                                                            units="imperial")
                    if distance_matrix["rows"][0]["elements"][0]["status"] == "OK":
                        driving_distance = distance_matrix["rows"][0]["elements"][0]["distance"]["text"]
                    else:
                        driving_distance = None

                else:
                    latitude = None
                    longitude = None
                    driving_distance = None

                response = requests.get(url)

                soup = bs4.BeautifulSoup(response.content, "html5lib")

                camping_section = soup.find("h4", text="Camping")
                camping = ""
                if camping_section:
                    next_sibling = camping_section.find_next_sibling()
                    while next_sibling and next_sibling.name != "h4":
                        if next_sibling.name == "p":
                            camping += str(next_sibling.get_text()) + "\n"
                        next_sibling = next_sibling.find_next_sibling()
                else:
                    print("Working")


                c.execute("REPLACE INTO state_forests VALUES (?, ?, ?, ?, ?, ?, ?)", (name, url, self.region_name, latitude, longitude, driving_distance, camping))


        def get_state_forest_links(self):
            request = requests.get(self.regionsite)
            html = bs4.BeautifulSoup(request.content, "html5lib")
            forests = html.find_all("a")
            for link in forests:
                if "state forest" in link.text.lower():
                    url = "https://www.dec.ny.gov" + link.get("href")
                    name = link.text.strip()
                    self.state_forests[name] = url


    URL = "https://www.dec.ny.gov/outdoor/82098.html"
    request = requests.get(URL)
    html = bs4.BeautifulSoup(request.content, "html.parser")

    regions = {}

    for link in html.find_all("a"):
        if "region" in link.text.lower():
            region_text = link.text.lower().split(" - ")
            region_number = int(region_text[1].split()[1])
            region_url = link.get("href")
            region_name = region_text[0]
            regions[region_number] = {"url": f"https://www.dec.ny.gov{region_url}", "name": region_name}

    print(f"\nRetrieving State forest information...")

    for region_number, region_data in regions.items():
        region_name = region_data["name"]
        region_url = region_data["url"]
        print(f"\nAdding '{region_name} - {region_number}' into the database.")
        region = Region(region_url)
        region.region_name = region_name
        region.get_state_forest_links()
        region.get_state_forest_locations("43.168902, -78.696849")

    conn.commit()
    conn.close()



os.chdir(os.path.dirname(os.path.abspath(__file__)))
conn = sqlite3.connect("state_forests.db")
c = conn.cursor()

if conn is None:
    print("Error: Failed to load database")
else:
    print("Database loaded successfully")

root = tk.Tk()
root.geometry("800x400")
root.title("State Forests")

headers = ["Sort by Name", "Sort by Distance"]
header_buttons = []
for header in headers:
    button = tk.Button(root, text=header)
    header_buttons.append(button)

header_buttons[0].place(x=0, y=0, width=300, height=30)
header_buttons[1].place(x=300, y=0, width=300, height=30)

region_map = {
    "Region 1 - Long Island": "long island",
    "Region 2 - New York City": "new york city",
    "Region 3 - Lower Hudson Valley": "lower hudson valley",
    "Region 4 - Capital Region/Northern Catskills": "capital region/ northern catskills",
    "Region 5 - Eastern Adirondacks/Lake Champlain": "eastern adirondacks/ lake champlain",
    "Region 6 - Western Adirondack/Upper Mohawk Valley/Eastern Lake Ontario": "western adirondacks/ upper mohawk valley/ eastern lake ontario",
    "Region 7 - Central New York": "central new york",
    "Region 8 - Rochester/Western Finger Lakes": "rochester/ western finger lakes",
    "Region 9 - Western New York": "western new york"
}

selected_region = tk.StringVar(root)
selected_region.set(list(region_map.keys())[0])
region_dropdown = tk.OptionMenu(root, selected_region, *region_map)
region_dropdown.place(x=0, y=30, width=300, height=30)

forest_listbox = tk.Listbox(root, width=50, height=20)
forest_listbox.place(x=0, y=60, width=350, height=340)

camping_textbox = tk.Text(root, width=50, height=20, wrap="word")
camping_textbox.place(x=352, y=60, width=450, height=340)

def populate_camping_textbox(event):
    index = forest_listbox.curselection()[0]
    forest_info = forest_listbox.get(index)
    name, distance = forest_info.split(" (")
    camping_info = c.execute("SELECT camping FROM state_forests WHERE name=?", (name,)).fetchone()[0]
    camping_textbox.delete("1.0", tk.END)
    camping_textbox.tag_config("left", justify="left")
    camping_textbox.insert(tk.END, f"{camping_info}")


def populate_forests(region):
    forest_listbox.delete(0, tk.END)

    conn = sqlite3.connect("state_forests.db")
    c = conn.cursor()
    c.execute("SELECT name, driving_distance, latitude, longitude, camping FROM state_forests WHERE region=?", (region_map[region],))
    forests = c.fetchall()
    conn.close()

    for forest in forests:
        name, distance, latitude, longitude, camping = forest
        formatted_entry = f"{name} ({distance})"
        forest_listbox.insert(tk.END, formatted_entry)
        forest_listbox.bind("<<ListboxSelect>>", populate_camping_textbox)
    forest_listbox.bind("<Double-Button-1>", lambda event: open_directions())


def open_directions():
    index = forest_listbox.curselection()[0]
    forest_info = forest_listbox.get(index)
    name, distance = forest_info.split(" (")
    conn = sqlite3.connect("state_forests.db")
    c = conn.cursor()
    latitude, longitude = c.execute("SELECT latitude, longitude FROM state_forests WHERE name=?", (name,)).fetchone()
    conn.close()
    url = f"https://www.google.com/maps/dir/?api=1&destination={latitude},{longitude}"
    webbrowser.open_new_tab(url)

def sort_listbox(column):
    forest_listbox.delete(0, tk.END)
    c.execute(f"SELECT name, driving_distance FROM state_forests WHERE region=? ORDER BY CAST({column} AS INTEGER)", (region_map[selected_region.get()],))
    forests = c.fetchall()
    for forest in forests:
        name, distance = forest
        forest_listbox.insert(tk.END, f"{name} ({distance})")

def cheese_one():
    db_file_path = os.path.join(os.getcwd(), "state_forests.db")

    if os.path.isfile(db_file_path):
        return "cheese_one passed"

def cheese_two():
    db_file_path = os.path.join(os.getcwd(), "state_forests.db")

    if os.path.isfile(db_file_path):
        return "cheese_two passed"

def cheese_three():
    db_file_path = os.path.join(os.getcwd(), "state_forests.db")

    if os.path.isfile(db_file_path):
        return "cheese_three passed"

header_buttons[0].config(command=lambda: sort_listbox("name"))
header_buttons[1].config(command=lambda: sort_listbox("driving_distance"))

selected_region.trace("w", lambda *args: populate_forests(selected_region.get()))
populate_forests(selected_region.get())

root.mainloop()
conn.close()
