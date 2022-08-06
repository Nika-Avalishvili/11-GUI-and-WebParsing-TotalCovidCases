from tkinter import *
from tkinter import ttk
import customtkinter


import requests
from bs4 import BeautifulSoup
resp = requests.get("https://www.worldometers.info/coronavirus/")
cont = resp.text

soup = BeautifulSoup(cont, "html.parser")
recovered_data = soup.find_all('tr')

countries_data = {}

for i in recovered_data:
    countries_data[i.find_all()[2].text.capitalize()]=i.find_all()[3].text



### --- Back_end --- ###
def country_name(event):
    if entry1.get() == '':
        entry2.configure(text = 'Fill country field', text_color = 'gray', text_font = ('arial',16))
    else:
        entry2.configure(text = f"{countries_data[entry1.get().capitalize()]}", text_color = 'black', text_font = ('arial',16, 'bold'))


### --- Front_end --- ###
window = customtkinter.CTk()
window.geometry('700x300')

window.title("Covid statistic")

top_frame = Frame(window)
top_frame.pack(padx = 10, pady = 40)


title1 = customtkinter.CTkLabel(top_frame,
                                    text = 'Country',
                                    text_font = ('arial', 16),
                                    text_color = '#111',
                                    bg_color = None,
                                    fg_color = None)
title1.grid(row = 0, column = 0, padx=10, pady=4)


entry1 = customtkinter.CTkEntry(top_frame,
                                    placeholder_text="Enter country: ",
                                    placeholder_text_color = 'black',
                                    width = 190,
                                    height = 30,
                                    border_width = 1,
                                    corner_radius = 5,
                                    fg_color = '#eee',
                                    bg_color = None,
                                    text_color = '#111',
                                    text_font = ('arial',16))
entry1.grid(row = 1 , column = 0, padx=10, pady=10)
entry1.bind("<KeyRelease>", country_name)

title2 = customtkinter.CTkLabel(top_frame,
                                    text = 'Total Cases',
                                    text_font = ('arial', 16),
                                    text_color = '#111',
                                    bg_color = None,
                                    fg_color = None)
title2.grid(row = 0, column = 1, padx=10, pady=4)


entry2 = customtkinter.CTkLabel(top_frame,
                                    text="Fill country field",
                                    text_color = 'gray',
                                    width = 190,
                                    height = 30,
                                    fg_color = '#eee',
                                    bg_color = None,
                                    text_font = ('arial',16))
entry2.grid(row = 1 , column = 1, padx=10, pady=10)


window.mainloop()
