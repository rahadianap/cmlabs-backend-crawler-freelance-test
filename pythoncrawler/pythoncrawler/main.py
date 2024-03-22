import scrapy
import requests
from bs4 import BeautifulSoup
import tkinter
import customtkinter


def parse(response):
    url = response.url
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    file = open('index_link.html', 'w', encoding="utf-8")
    for item in soup.find_all('a'):
        data = item.get('href')
        file.write(data)
        file.write("\n")
    # self.html_file.write(response.text)
    file.close()


customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Title')

label = customtkinter.CTkLabel(app, text='Insert Link')
label.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

button = customtkinter.CTkButton(app, text='Start Crawling', command=parse('https://cmlabs.co/'))

app.mainloop()
