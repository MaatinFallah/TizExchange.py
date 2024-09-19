from tkinter import *
import sqlite3
from PIL import Image, ImageTk
import requests
import bs4
import datetime

# admin123
connect = sqlite3.connect('TizExchange')
cursor = connect.cursor()

# cursor.execute("create table User (Name , Password, Id_number)")
# cursor.execute('create table Currency (Name, Price)')
#
# cursor.execute("insert into Currency values ('BTC', '')")
# cursor.execute("insert into Currency values ('ETH', '')")
# cursor.execute("insert into Currency values ('DOGE', '')")
# cursor.execute("insert into Currency values ('NOT', '')")
# cursor.execute("insert into Currency values ('TON', '')")

# cursor.execute('select * from User')
# print(cursor.fetchall())

Login_image = Image.open('images/login.jpg')
Signin_image = Image.open('images/signin.jpg')
Exchange_image = Image.open('images/exchange2.jpg')
bitcoin = Image.open('images/bitcoin.png')

User_n = ''


def Exchange():
    global User_n

    root = Tk()
    root.title('TizExchange-MainMenu')
    root.attributes('-fullscreen', True)
    root.iconbitmap('images/exchange.ico')

    image = ImageTk.PhotoImage(Exchange_image)
    background = Label(root, image=image)
    background.pack()

    btc = requests.get('https://nobitex.ir/btc/')
    btc_soup = bs4.BeautifulSoup(btc.text, 'lxml')
    btc_price = btc_soup.select(".text-body-bold-medium")[2].getText()

    eth = requests.get('https://nobitex.ir/eth/')
    eth_soup = bs4.BeautifulSoup(eth.text, 'lxml')
    eth_price = eth_soup.select(".text-body-bold-medium")[2].getText()

    doge = requests.get('https://nobitex.ir/doge/')
    doge_soup = bs4.BeautifulSoup(doge.text, 'lxml')
    doge_price = doge_soup.select(".text-body-bold-medium")[2].getText()

    ton = requests.get('https://nobitex.ir/ton/')
    ton_soup = bs4.BeautifulSoup(ton.text, 'lxml')
    ton_price = ton_soup.select(".text-body-bold-medium")[2].getText()

    notc = requests.get('https://nobitex.ir/not/')
    notc_soup = bs4.BeautifulSoup(notc.text, 'lxml')
    not_price = notc_soup.select(".text-body-bold-medium")[2].getText()

    def config():
        btc = requests.get('https://nobitex.ir/btc/')
        btc_soup = bs4.BeautifulSoup(btc.text, 'lxml')
        btc_price = btc_soup.select(".text-body-bold-medium")[2].getText()

        eth = requests.get('https://nobitex.ir/eth/')
        eth_soup = bs4.BeautifulSoup(eth.text, 'lxml')
        eth_price = eth_soup.select(".text-body-bold-medium")[2].getText()

        doge = requests.get('https://nobitex.ir/doge/')
        doge_soup = bs4.BeautifulSoup(doge.text, 'lxml')
        doge_price = doge_soup.select(".text-body-bold-medium")[2].getText()

        ton = requests.get('https://nobitex.ir/ton/')
        ton_soup = bs4.BeautifulSoup(ton.text, 'lxml')
        ton_price = ton_soup.select(".text-body-bold-medium")[2].getText()

        notc = requests.get('https://nobitex.ir/not/')
        notc_soup = bs4.BeautifulSoup(notc.text, 'lxml')
        not_price = notc_soup.select(".text-body-bold-medium")[2].getText()

        display1.config(text=f'Current BTC Price :\t\t\t{btc_price}\tIR/Toman')
        display2.config(text=f'Current ETH Price :\t\t\t{eth_price}\tIR/Toman')
        display3.config(text=f'Current DOGE Price :\t\t\t{doge_price}\t\tIR/Toman')
        display4.config(text=f'Current TON Price :\t\t\t{ton_price}\t\tIR/Toman')
        display5.config(text=f'Current NOT Price :\t\t\t{not_price}\t\tIR/Toman')

        root.after(10000, config)

    def destroy1():
        root.destroy()
        btc_page()

    def destroy2():
        root.destroy()
        eth_page()

    def destroy3():
        root.destroy()
        doge_page()

    def destroy4():
        root.destroy()
        ton_page()

    def destroy5():
        root.destroy()
        not_page()

    def btc_page():
        root = Tk()
        root.title('TizExchange-BTC')
        root.attributes('-fullscreen', True)
        Exchange_image = Image.open('images/exchange2.jpg')

        def go_back():
            root.destroy()
            Exchange()

        def main_menu():
            root.destroy()
            Exchange()

        def about_me():
            pass

        def exit_window():
            root.destroy()

        def config_b():

            btc = requests.get('https://nobitex.ir/btc/')
            btc_soup = bs4.BeautifulSoup(btc.text, 'lxml')
            btc_price = btc_soup.select(".text-body-bold-medium")[2].getText()

            Price.config(text=f'Current BTC Price:\t{btc_price}\t\tIR/Toman\t\tLast Updated: {datetime.datetime.now()}')

            root.after(10000, config_b)

        image = ImageTk.PhotoImage(Exchange_image)
        background = Label(root, image=image)
        background.pack()

        Price = (Label(root,
                       text=f'Current BTC Price:\t{btc_price}\t\tIR/Toman\t   Price Last Updated: {datetime.datetime.now()}',
                       width=100, height=5, bg='silver', fg='black', font=('Arial', 13, 'bold'), anchor='w'))
        Price.place(x=0, y=100)

        Menu = Label(root, text=f'\t   {User_n}',
                     font=('Arial', 12, 'bold'), bg='gainsboro', fg='black', height=20, width=25, anchor='nw',
                     justify='left')
        Menu.place(x=1250, y=100)

        Go_back = Button(root, text='Go Back', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white', command=go_back)
        Go_back.place(x=1325, y=200)

        MainMenu = Button(root, text='Main Menu', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white', command=main_menu)
        MainMenu.place(x=1325, y=300)

        About = Button(root, text='About Me', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white', command=about_me)
        About.place(x=1325, y=425)

        def change():
            if text1.cget('text') == 'BTC':
                text1.config(text='IR/Toman')
                text2.config(text='BTC')
            else:
                text1.config(text='BTC')
                text2.config(text='IR/Toman')

        def calculate():
            if not entry1.get().isdigit():
                error1.config(text='you should only enter a number'.title())
            else:
                if entry1.get() != '':
                    number = int(entry1.get())
                    clean_str = ''
                    for i in btc_price:
                        if i != ',':
                            clean_str += i

                    clean_btc = int(clean_str)

                    if text1.cget('text') == 'BTC':
                        Answer.config(text=(number * clean_btc))
                    else:
                        Answer.config(text=(number / clean_btc))

        calculator_back = Label(root, bg='silver', width=175, height=25)
        calculator_back.place(x=0, y=250)

        text1 = Label(root, text='IR/Toman', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text1.place(x=230, y=350)

        text2 = Label(root, text='BTC', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text2.place(x=950, y=350)

        entry1 = Entry(root, font=('Arial', 15), justify='center')
        entry1.place(x=150, y=400)

        Answer = Label(root, text='', bg='white', fg='black', justify='center', font=('Arial', 15))
        Answer.place(x=970, y=400)

        error1 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11, 'bold'))
        error1.place(x=250, y=475)

        error2 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11))
        error2.place(x=950, y=475)

        change = Button(root, text='Change Currency\'s', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=change)
        change.place(x=570, y=400)

        submit = Button(root, text='Calculate', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'), command=calculate)
        submit.place(x=590, y=500)

        Exchanges = Label(root,
                          text='want to trade crypto? check these exchanges out !\n\n\n\n\n\n\n\n\n\t\thttps://sarmayex.com/\t\t\t\t\t\thttps://nobitex.ir/\t\t\t\t\t\thttps://wallex.ir/'.title(),
                          font=('Arial', 12, 'bold'), bg='silver', fg='black', width=200, height=10, anchor='nw',
                          justify='left')
        Exchanges.place(x=0, y=670)

        root.after(10000, config_b)
        root.mainloop()

    def eth_page():
        root = Tk()
        root.title('TizExchange-ETH')
        root.attributes('-fullscreen', True)
        Exchange_image = Image.open('images/exchange2.jpg')

        def go_back():
            root.destroy()
            Exchange()

        def main_menu():
            root.destroy()
            Exchange()

        def about_me():
            pass

        def exit_window():
            root.destroy()

        def config_b():
            eth = requests.get('https://nobitex.ir/eth/')
            eth_soup = bs4.BeautifulSoup(eth.text, 'lxml')
            eth_price = eth_soup.select(".text-body-bold-medium")[2].getText()

            Price.config(text=f'Current ETH Price:\t{eth_price}\t\tIR/Toman\t\tLast Update: {datetime.datetime.now()}')

            root.after(10000, config_b)

        image = ImageTk.PhotoImage(Exchange_image)
        background = Label(root, image=image)
        background.pack()

        Price = (Label(root,
                       text=f'Current ETH Price:\t{eth_price}\t\tIR/Toman\t   Price Last Updated: {datetime.datetime.now()}',
                       width=100, height=5, bg='silver', fg='black', font=('Arial', 13, 'bold'), anchor='w'))
        Price.place(x=0, y=100)

        Menu = Label(root, text=f'\t   {User_n}',
                     font=('Arial', 12, 'bold'), bg='gainsboro', fg='black', height=20, width=25, anchor='nw',
                     justify='left')
        Menu.place(x=1250, y=100)

        Go_back = Button(root, text='Go Back', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                         command=go_back)
        Go_back.place(x=1325, y=200)

        MainMenu = Button(root, text='Main Menu', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                          command=main_menu)
        MainMenu.place(x=1325, y=300)

        About = Button(root, text='About Me', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                       command=about_me)
        About.place(x=1325, y=425)

        def change():
            if text1.cget('text') == 'ETH':
                text1.config(text='IR/Toman')
                text2.config(text='ETH')
            else:
                text1.config(text='ETH')
                text2.config(text='IR/Toman')

        def calculate():
            if not entry1.get().isdigit():
                error1.config(text='you should only enter a number'.title())
            else:
                if entry1.get() != '':
                    number = int(entry1.get())
                    clean_str = ''
                    for i in eth_price:
                        if i != ',':
                            clean_str += i

                    clean_eth = int(clean_str)

                    if text1.cget('text') == 'ETH':
                        Answer.config(text=(number * clean_eth))
                    else:
                        Answer.config(text=(number / clean_eth))

        calculator_back = Label(root, bg='silver', width=175, height=25)
        calculator_back.place(x=0, y=250)

        text1 = Label(root, text='IR/Toman', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text1.place(x=230, y=350)

        text2 = Label(root, text='ETH', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text2.place(x=950, y=350)

        entry1 = Entry(root, font=('Arial', 15), justify='center')
        entry1.place(x=150, y=400)

        Answer = Label(root, text='', bg='white', fg='black', justify='center', font=('Arial', 15))
        Answer.place(x=970, y=400)

        error1 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11, 'bold'))
        error1.place(x=250, y=475)

        error2 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11))
        error2.place(x=950, y=475)

        change = Button(root, text='Change Currency\'s', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=change)
        change.place(x=570, y=400)

        submit = Button(root, text='Calculate', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=calculate)
        submit.place(x=590, y=500)

        Exchanges = Label(root,
                          text='want to trade crypto? check these exchanges out !\n\n\n\n\n\n\n\n\n\t\thttps://sarmayex.com/\t\t\t\t\t\thttps://nobitex.ir/\t\t\t\t\t\thttps://wallex.ir/'.title(),
                          font=('Arial', 12, 'bold'), bg='silver', fg='black', width=200, height=10, anchor='nw',
                          justify='left')
        Exchanges.place(x=0, y=670)

        root.after(10000, config_b)
        root.mainloop()

    def doge_page():
        root = Tk()
        root.title('TizExchange-DOGE')
        root.attributes('-fullscreen', True)
        Exchange_image = Image.open('images/exchange2.jpg')

        def go_back():
            root.destroy()
            Exchange()

        def main_menu():
            root.destroy()
            Exchange()

        def about_me():
            pass

        def exit_window():
            root.destroy()

        def config_b():
            doge = requests.get('https://nobitex.ir/doge/')
            doge_soup = bs4.BeautifulSoup(doge.text, 'lxml')
            doge_price = doge_soup.select(".text-body-bold-medium")[2].getText()

            Price.config(
                text=f'Current DOGE Price:\t{doge_price}\t\tIR/Toman\t\tLast Update: {datetime.datetime.now()}')

            root.after(10000, config_b)

        image = ImageTk.PhotoImage(Exchange_image)
        background = Label(root, image=image)
        background.pack()

        Price = (Label(root,
                       text=f'Current DOGE Price:\t{doge_price}\t\tIR/Toman\t   Price Last Updated: {datetime.datetime.now()}',
                       width=100, height=5, bg='silver', fg='black', font=('Arial', 13, 'bold'), anchor='w'))
        Price.place(x=0, y=100)

        Menu = Label(root, text=f'\t   {User_n}',
                     font=('Arial', 12, 'bold'), bg='gainsboro', fg='black', height=20, width=25, anchor='nw',
                     justify='left')
        Menu.place(x=1250, y=100)

        Go_back = Button(root, text='Go Back', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                         command=go_back)
        Go_back.place(x=1325, y=200)

        MainMenu = Button(root, text='Main Menu', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                          command=main_menu)
        MainMenu.place(x=1325, y=300)

        About = Button(root, text='About Me', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                       command=about_me)
        About.place(x=1325, y=425)

        def change():
            if text1.cget('text') == 'DOGE':
                text1.config(text='IR/Toman')
                text2.config(text='DOGE')
            else:
                text1.config(text='DOGE')
                text2.config(text='IR/Toman')

        def calculate():
            if not entry1.get().isdigit():
                error1.config(text='you should only enter a number'.title())
            else:
                if entry1.get() != '':
                    number = int(entry1.get())
                    clean_str = ''
                    for i in doge_price:
                        if i != ',':
                            clean_str += i

                    clean_doge = int(clean_str)

                    if text1.cget('text') == 'DOGE':
                        Answer.config(text=(number * clean_doge))
                    else:
                        Answer.config(text=(number / clean_doge))

        calculator_back = Label(root, bg='silver', width=175, height=25)
        calculator_back.place(x=0, y=250)

        text1 = Label(root, text='IR/Toman', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text1.place(x=230, y=350)

        text2 = Label(root, text='DOGE', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text2.place(x=950, y=350)

        entry1 = Entry(root, font=('Arial', 15), justify='center')
        entry1.place(x=150, y=400)

        Answer = Label(root, text='', bg='white', fg='black', justify='center', font=('Arial', 15))
        Answer.place(x=970, y=400)

        error1 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11, 'bold'))
        error1.place(x=250, y=475)

        error2 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11))
        error2.place(x=950, y=475)

        change = Button(root, text='Change Currency\'s', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=change)
        change.place(x=570, y=400)

        submit = Button(root, text='Calculate', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=calculate)
        submit.place(x=590, y=500)

        Exchanges = Label(root,
                          text='want to trade crypto? check these exchanges out !\n\n\n\n\n\n\n\n\n\t\thttps://sarmayex.com/\t\t\t\t\t\thttps://nobitex.ir/\t\t\t\t\t\thttps://wallex.ir/'.title(),
                          font=('Arial', 12, 'bold'), bg='silver', fg='black', width=200, height=10, anchor='nw',
                          justify='left')
        Exchanges.place(x=0, y=670)

        root.after(10000, config_b)
        root.mainloop()

    def ton_page():
        root = Tk()
        root.title('TizExchange-TON')
        root.attributes('-fullscreen', True)
        Exchange_image = Image.open('images/exchange2.jpg')

        def go_back():
            root.destroy()
            Exchange()

        def main_menu():
            root.destroy()
            Exchange()

        def about_me():
            pass

        def exit_window():
            root.destroy()

        def config_b():
            ton = requests.get('https://nobitex.ir/ton/')
            ton_soup = bs4.BeautifulSoup(ton.text, 'lxml')
            ton_price = ton_soup.select(".text-body-bold-medium")[2].getText()

            Price.config(text=f'Current TON Price:\t{ton_price}\t\tIR/Toman\t\tLast Update: {datetime.datetime.now()}')

            root.after(10000, config_b)

        image = ImageTk.PhotoImage(Exchange_image)
        background = Label(root, image=image)
        background.pack()

        Price = (Label(root,
                       text=f'Current TON Price:\t{ton_price}\t\tIR/Toman\t   Price Last Updated: {datetime.datetime.now()}',
                       width=100, height=5, bg='silver', fg='black', font=('Arial', 13, 'bold'), anchor='w'))
        Price.place(x=0, y=100)

        Menu = Label(root, text=f'\t   {User_n}',
                     font=('Arial', 12, 'bold'), bg='gainsboro', fg='black', height=20, width=25, anchor='nw',
                     justify='left')
        Menu.place(x=1250, y=100)

        Go_back = Button(root, text='Go Back', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                         command=go_back)
        Go_back.place(x=1325, y=200)

        MainMenu = Button(root, text='Main Menu', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                          command=main_menu)
        MainMenu.place(x=1325, y=300)

        About = Button(root, text='About Me', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                       command=about_me)
        About.place(x=1325, y=425)

        def change():
            if text1.cget('text') == 'TON':
                text1.config(text='IR/Toman')
                text2.config(text='TON')
            else:
                text1.config(text='TON')
                text2.config(text='IR/Toman')

        def calculate():
            if not entry1.get().isdigit():
                error1.config(text='you should only enter a number'.title())
            else:
                if entry1.get() != '':
                    number = int(entry1.get())
                    clean_str = ''
                    for i in ton_price:
                        if i != ',':
                            clean_str += i

                    clean_ton = int(clean_str)

                    if text1.cget('text') == 'TON':
                        Answer.config(text=(number * clean_ton))
                    else:
                        Answer.config(text=(number / clean_ton))

        calculator_back = Label(root, bg='silver', width=175, height=25)
        calculator_back.place(x=0, y=250)

        text1 = Label(root, text='IR/Toman', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text1.place(x=230, y=350)

        text2 = Label(root, text='TON', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text2.place(x=950, y=350)

        entry1 = Entry(root, font=('Arial', 15), justify='center')
        entry1.place(x=150, y=400)

        Answer = Label(root, text='', bg='white', fg='black', justify='center', font=('Arial', 15))
        Answer.place(x=970, y=400)

        error1 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11, 'bold'))
        error1.place(x=250, y=475)

        error2 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11))
        error2.place(x=950, y=475)

        change = Button(root, text='Change Currency\'s', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=change)
        change.place(x=570, y=400)

        submit = Button(root, text='Calculate', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=calculate)
        submit.place(x=590, y=500)

        Exchanges = Label(root,
                          text='want to trade crypto? check these exchanges out !\n\n\n\n\n\n\n\n\n\t\thttps://sarmayex.com/\t\t\t\t\t\thttps://nobitex.ir/\t\t\t\t\t\thttps://wallex.ir/'.title(),
                          font=('Arial', 12, 'bold'), bg='silver', fg='black', width=200, height=10, anchor='nw',
                          justify='left')
        Exchanges.place(x=0, y=670)

        root.after(10000, config_b)
        root.mainloop()

    def not_page():
        root = Tk()
        root.title('TizExchange-NOT')
        root.attributes('-fullscreen', True)
        Exchange_image = Image.open('images/exchange2.jpg')

        def go_back():
            root.destroy()
            Exchange()

        def main_menu():
            root.destroy()
            Exchange()

        def about_me():
            pass

        def exit_window():
            root.destroy()

        def config_b():
            notc = requests.get('https://nobitex.ir/not/')
            notc_soup = bs4.BeautifulSoup(notc.text, 'lxml')
            not_price = notc_soup.select(".text-body-bold-medium")[2].getText()

            Price.config(text=f'Current NOT Price:\t{not_price}\t\tIR/Toman\t\tLast Update: {datetime.datetime.now()}')

            root.after(10000, config_b)

        image = ImageTk.PhotoImage(Exchange_image)
        background = Label(root, image=image)
        background.pack()

        Price = (Label(root,
                       text=f'Current NOT Price:\t{not_price}\t\tIR/Toman\t   Price Last Updated: {datetime.datetime.now()}',
                       width=100, height=5, bg='silver', fg='black', font=('Arial', 13, 'bold'), anchor='w'))
        Price.place(x=0, y=100)

        Menu = Label(root, text=f'\t   {User_n}',
                     font=('Arial', 12, 'bold'), bg='gainsboro', fg='black', height=20, width=25, anchor='nw',
                     justify='left')
        Menu.place(x=1250, y=100)

        Go_back = Button(root, text='Go Back', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                         command=go_back)
        Go_back.place(x=1325, y=200)

        MainMenu = Button(root, text='Main Menu', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                          command=main_menu)
        MainMenu.place(x=1325, y=300)

        About = Button(root, text='About Me', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white',
                       command=about_me)
        About.place(x=1325, y=425)

        def change():
            if text1.cget('text') == 'NOT':
                text1.config(text='IR/Toman')
                text2.config(text='NOT')
            else:
                text1.config(text='NOT')
                text2.config(text='IR/Toman')

        def calculate():
            if not entry1.get().isdigit():
                error1.config(text='you should only enter a number'.title())
            else:
                if entry1.get() != '':
                    number = int(entry1.get())
                    clean_str = ''
                    for i in not_price:
                        if i != ',':
                            clean_str += i

                    clean_not = int(clean_str)

                    if text1.cget('text') == 'NOT':
                        Answer.config(text=(number * clean_not))
                    else:
                        Answer.config(text=(number / clean_not))

        calculator_back = Label(root, bg='silver', width=175, height=25)
        calculator_back.place(x=0, y=250)

        text1 = Label(root, text='IR/Toman', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text1.place(x=230, y=350)

        text2 = Label(root, text='NOT', font=('Arial', 11, 'bold'), bg='silver', fg='black')
        text2.place(x=950, y=350)

        entry1 = Entry(root, font=('Arial', 15), justify='center')
        entry1.place(x=150, y=400)

        Answer = Label(root, text='', bg='white', fg='black', justify='center', font=('Arial', 15))
        Answer.place(x=970, y=400)

        error1 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11, 'bold'))
        error1.place(x=250, y=475)

        error2 = Label(root, text='', bg='silver', fg='white', font=('Arial', 11))
        error2.place(x=950, y=475)

        change = Button(root, text='Change Currency\'s', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=change)
        change.place(x=570, y=400)

        submit = Button(root, text='Calculate', bg='deepskyblue', fg='white', font=('Arial', 9, 'bold'),
                        command=calculate)
        submit.place(x=590, y=500)

        Exchanges = Label(root,
                          text='want to trade crypto? check these exchanges out !\n\n\n\n\n\n\n\n\n\t\thttps://sarmayex.com/\t\t\t\t\t\thttps://nobitex.ir/\t\t\t\t\t\thttps://wallex.ir/'.title(),
                          font=('Arial', 12, 'bold'), bg='silver', fg='black', width=200, height=10, anchor='nw',
                          justify='left')
        Exchanges.place(x=0, y=670)

        root.after(10000, config_b)
        root.mainloop()

    def Logout():
        root.destroy()
        Login()

    def prev_destroy():
        root.destroy()
        profile()

    def profile():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.title('TizExchange-Profile')

        Exchange_image = Image.open('images/exchange2.jpg')
        User_image = Image.open('images/car (1).png')

        image = ImageTk.PhotoImage(Exchange_image)
        back_ground = Label(root, image=image)
        back_ground.pack()

        lst = cursor.execute('select * from user')

        for i in lst:
            if User_n in i:
                Id = i[2]
                password = i[1]

        border = Label(root, text=f'\n\n\n\n\n\n\n\n\nUserName : \t\t{User_n}\n\n\n\n\n\n\n\n\nPassword :\t\t{password}\n\n\n\n\n\n\n\n\nID :\t\t\t{Id}', bg='silver', fg='black', font=('Arial', 15, 'bold'), anchor='nw',justify='left', height=29 , width=50)
        border.place(x=500, y=150)

        def go_back():
            root.destroy()
            Exchange()

        GoBack = Button(root, text='Go Back', font=('Arial', 12, 'bold'), bg='deepskyblue', fg='white', width=15, command=go_back)
        GoBack.place(x=925, y=180)

        image2 = ImageTk.PhotoImage(User_image)
        user = Label(root, image=image2)
        user.place(x=733, y=180)

        root.mainloop()

    Menu = Label(root, text=f'\n\t       Welcome {User_n}', font=('Arial', 15, 'bold'), bg='gainsboro', fg='black', height=30, width=37, anchor='nw')
    Menu.place(x=1067, y=100)

    Profile = Button(root, text='See Profile', justify='center', bg='deepskyblue', fg='white', font=('Arial', 15, 'bold'), width=30, command=prev_destroy)
    Profile.place(x=1110, y=375)

    LogOut = Button(root, text='Log Out', justify='center', font=('Arial', 15, 'bold'), bg='deepskyblue', fg='white', width=30, command=Logout)
    LogOut.place(x=1110, y=575)

    ################################################
    display1 = Label(root, border=20, text=f'Current BTC Price:\t\t\t{btc_price}\tIR/Toman', bg='silver', width=100,
                     height=5, anchor='w', font=('Arial', 13, 'bold'))
    display1.place(x=0, y=100)
    button1 = Button(root, text=' Click to see Details', bg='DeepSkyBlue', fg='white', width=20, height=6,
                     font=('Arial', 8, 'bold'), command=destroy1)
    button1.place(x=880, y=120)
    ################################################
    display2 = Label(root, border=20, text=f'Current ETH Price:\t\t\t{eth_price}\t IR/Toman', bg='silver', width=100,
                     height=5,
                     anchor='w', font=('Arial', 13, 'bold'))
    display2.place(x=0, y=250)
    button2 = Button(root, text=' Click to see Details', bg='DeepSkyBlue', fg='white', width=20, height=6,
                     font=('Arial', 8, 'bold'), command=destroy2)
    button2.place(x=880, y=270)
    ################################################
    display3 = Label(root, border=20, text=f'Current DOGE Price:\t\t\t{doge_price}\t\tIR/Toman', bg='silver', width=100,
                     height=5,
                     anchor='w', font=('Arial', 13, 'bold'))
    display3.place(x=0, y=400)
    button3 = Button(root, text=' Click to see Details', bg='DeepSkyBlue', fg='white', width=20, height=6,
                     font=('Arial', 8, 'bold'), command=destroy3)
    button3.place(x=880, y=420)
    ################################################
    display4 = Label(root, border=20, text=f'Current TON Price:\t\t\t{ton_price}\t\tIR/Toman', bg='silver', width=100,
                     height=5,
                     anchor='w', font=('Arial', 13, 'bold'))
    display4.place(x=0, y=550)
    button4 = Button(root, text=' Click to see Details', bg='DeepSkyBlue', fg='white', width=20, height=6,
                     font=('Arial', 8, 'bold'), command=destroy4)
    button4.place(x=880, y=570)
    ################################################
    display5 = Label(root, border=20, text=f'Current NOT Price:\t\t\t{not_price}\t\tIR/Toman', bg='silver', width=100,
                     height=5,
                     anchor='w', font=('Arial', 13, 'bold'))
    display5.place(x=0, y=700)
    button5 = Button(root, text=' Click to see Details', bg='DeepSkyBlue', fg='white', width=20, height=6,
                     font=('Arial', 8, 'bold'), command=destroy5)
    button5.place(x=880, y=720)
    #################################################

    root.after(10000, config)
    root.mainloop()


def Login():
    root = Tk()
    root.title('TizExchange-Login')
    root.attributes('-fullscreen', True)
    # root.geometry('1000x1000+250+250')

    image = ImageTk.PhotoImage(Login_image)

    background = Label(root, image=image)
    background.place(x=-2, y=-2)

    welcome = Label(root, text='Welcome to TizExchange! Please Log into your account ', font=('Arial', 12, 'bold'),
                    justify='center')
    welcome.pack()

    def exit_window():
        root.destroy()

    Exit = Button(root, text='Exit', command=exit_window)
    Exit.place(x=1505, y=0)

    user = Label(root, text='Enter Your UserName: ', font=('Arial', 10, 'bold'))
    user.place(x=600, y=200)

    def page():
        root.destroy()
        Signin()

    UserName = Entry(root)
    UserName.place(x=750, y=200)

    passw = Label(root, text='Enter Your Password: ', font=('Arial', 10, 'bold'))
    passw.place(x=600, y=300)

    def LogIn():
        global User_n
        In = False
        if UserName != '' and Password != '':
            Passw = Password.get()
            Usern = UserName.get()
            tuples = cursor.execute('select * from User')
            lst = cursor.fetchall()
            for i in lst:
                if Passw in i and Usern in i:
                    In = True
                    root.destroy()
                    User_n = Usern
                    Exchange()
                if i == lst[-1] and Passw not in i and Usern not in i:
                    Error.config(text='Username or Password Invalid')

    def show():
        if Password.cget('show') == '*':
            Password.config(show='')
        else:
            Password.config(show='*')

    Password = Entry(root, show='*')
    Password.place(x=750, y=300)
    Error = Label(root, font=('Arial', 10, 'bold'))
    Error.place(x=750, y=355)

    LogIn = Button(root, text='Log In', width=30, font=('Arial', 8, 'bold'), command=LogIn)
    LogIn.place(x=625, y=450)
    show = Checkbutton(root, text='Show', command=show)
    show.place(x=900, y=300)

    SignIn = Button(root, text='Dont Have An Account ? Make One !', width=30, font=('Arial', 8, 'bold'), command=page)
    SignIn.place(x=625, y=550)

    root.iconbitmap(r'D:\ZaUnknown\Programming\pythonProject\TizExchange\images\exchange.ico')
    root.mainloop()


def Signin():
    sign = Tk()
    sign.title('TizExchange-SignIn')
    sign.iconbitmap('images/exchange.ico')
    sign.attributes('-fullscreen', True)
    # sign.geometry('500x500+250+250')

    image = ImageTk.PhotoImage(Signin_image)
    background_image = Label(sign, image=image)
    background_image.place(x=-2, y=-2)

    welcome = Label(sign, text='Create Your Account By Filling Out These Forms ', font=('Arial', 12, 'bold'),
                    justify='center')
    welcome.pack()

    def exit_window():
        sign.destroy()

    Exit = Button(sign, text='Exit', command=exit_window)
    Exit.place(x=1505, y=0)

    user = Label(sign, text='Enter Your UserName: ', font=('Arial', 10, 'bold'))
    user.place(x=600, y=100)

    def page():
        sign.destroy()
        Login()

    def user_check():
        for i in cursor.execute('select Name from User'):
            if UserName.get() in i:
                print(i)
        if 8 > len(UserName.get()) or 16 < len(UserName.get()):
            UserError.config(text='your user name should be from 8 to 16 character long'.title())

        else:
            UserError.config(text='')
            UserName.config(state=DISABLED)

    UserName = Entry(sign)
    UserName.place(x=750, y=100)
    UserError = Label(sign, text='', font=('Arial', 10, 'bold'))
    UserError.place(x=750, y=150)
    UserSubmit = Button(sign, text='Submit', command=user_check)
    UserSubmit.place(x=900, y=100)

    passw = Label(sign, text='Enter Your Password: ', font=('Arial', 10, 'bold'))
    passw.place(x=600, y=200)

    def pass_submit():
        if 8 > len(Password.get()):
            PassError.config(text='your password should be at least 8 characters long'.title())
        else:
            Password.config(state=DISABLED)

    def show():
        if Password.cget('show') == '*':
            Password.config(show='')
        else:
            Password.config(show='*')

    Password = Entry(sign, show='*')
    Password.place(x=750, y=200)
    PassSubmit = Button(sign, text='submit', command=pass_submit)
    PassSubmit.place(x=900, y=200)
    PassError = Label(sign, text='', font=('Arial', 10, 'bold'))
    PassError.place(x=750, y=250)
    PassShow = Checkbutton(sign, text='Show', command=show)
    PassShow.place(x=950, y=200)

    id = Label(sign, text='Enter You Id Number: ', font=('Arial', 10, 'bold'))
    id.place(x=600, y=300)

    def id_submit():
        if len(Id.get()) != 10 or not Id.get().isdigit():
            IdError.config(text='your social Id number should be 10 character long and only contain numbers'.title())
        else:
            Id.config(state=DISABLED)

    Id = Entry(sign)
    Id.place(x=750, y=300)
    IdSubmit = Button(sign, text='Submit', command=id_submit)
    IdSubmit.place(x=900, y=300)
    IdError = Label(sign, text='', font=('Arial', 10, 'bold'))
    IdError.place(x=750, y=350)

    def captcha():
        if Password.get != '' and UserName.get() != '' and Id.get() != '':
            ID = Id.get()
            password = Password.get()
            name = UserName.get()

            cursor.execute(f"insert into User values ('{name}', '{password}', '{ID}')")
            connect.commit()
            sign.destroy()
            Login()

    SignIn = Button(sign, text='Create Account ', width=30, font=('Arial', 8, 'bold'), command=captcha)
    SignIn.place(x=625, y=450)
    LogIn = Button(sign, text='Already Have An Account ? Log In !', width=30, font=('Arial', 8, 'bold'), command=page)
    LogIn.place(x=625, y=550)

    sign.mainloop()



Login()
