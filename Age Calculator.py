import tkinter as tk
from datetime import datetime, date
import calendar

window = tk.Tk()
window.title("Age Calculator")

# main widgets
name = tk.Label(window, text="Name", font="Calibre, 12").grid(column=0, row=0, padx=10)
nameE = tk.Entry()
nameE.grid(column=1, row=0, ipadx=10, padx=10, sticky="e")
# age data
year = tk.Label(window, text="Year", font="Calibre, 12").grid(column=0, row=1, padx=10)
yearE = tk.Entry()
yearE.grid(column=1, row=1, ipadx=10, padx=10, sticky="e")
month = tk.Label(window, text="Month", font="Calibre, 12").grid(column=0, row=2, padx=10)
monthE = tk.Entry()
monthE.grid(column=1, row=2, ipadx=10, padx=10, sticky="e")
day = tk.Label(window, text="Date", font="Calibre, 12").grid(column=0, row=3, padx=10)
dayE = tk.Entry()
dayE.grid(column=1, row=3, ipadx=10, padx=10, sticky="e")


# functions

def age_cal():
	user = nameE.get()
	years = yearE.get()
	months = monthE.get()
	days = dayE.get()
	current_date = datetime.now().date()
	birth_date = date(int(years), int(months), int(days))
	result = f"Hey {user.title()}! {calculation(current_date, birth_date)}"
	title = tk.Text(font="Helvetica, 12", width=10, height=5, wrap="word")
	title.grid(column=0, row=7, columnspan=2, padx=5, pady=5, sticky="news", ipadx=15, ipady=5)
	title.delete(1.0, "end")
	title.insert(tk.END, result)


def get_day():
	# repeated code :(
	user = nameE.get()
	years = yearE.get()
	months = monthE.get()
	day_s = dayE.get()
	birth_date = date(int(years), int(months), int(day_s))
	# have to repeat the above code bcz it wasn't working earlier
	day_nm = calendar.day_name(birth_date.weekday())
	msg = f"Hey {user}! The day on which you were born is-\n{day_nm}"
	title = tk.Text(font="Calibre, 14", height=10, width=5)
	title.grid(column=0, row=7, columnspan=2, padx=5, pady=5, sticky="news")
	title.delete(1.0, "end")
	title.insert(tk.END, msg)


def calculation(first, second):
	days = first - second
	n_days = days.days
	years = int(n_days / 365.25)
	months = int((n_days % 365.25) / 30)
	return f"Your age as of today is {years} year(s), {months} month(s)"


# buttons are here
age_btn = tk.Button(window, text="Get Age", bg="green", fg="white", command=age_cal)
age_btn.grid(column=0, row=4, columnspan=2, padx=2, pady=2, sticky="news")
# day_btn = tk.Button(window, text="Get Day", bg="blue", fg="white", command=get_day)
# day_btn.grid(column=0, row=5, columnspan=2, padx=2, pady=2, sticky="news")
exit_btn = tk.Button(text="Exit", bg="grey", fg="white", command=lambda: window.destroy())
exit_btn.grid(column=0, row=6, columnspan=2, padx=2, pady=2, sticky="news")


# for setting focus on name entry
nameE.focus_set()

window.mainloop()

'''
days = 1329
years = days/365
weeks = (days % 365) / 7
days = days - ((years * 365) + (weeks * 7))
'''
