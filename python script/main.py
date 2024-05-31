from browser import browser, NoButton, NoInputName
from threading import Thread
import customtkinter
from tkinter.ttk import Spinbox
from tkinter import messagebox
from datetime import datetime
from webbrowser import open as wopen
from selenium.common.exceptions import InvalidArgumentException



def date_now(): return str(datetime.now()).split(" ")[0].replace("-", ".")
def time_now(): return str(datetime.now()).split(" ")[1].split(".")[0]
def create_time(): return f'{date_now()} - {time_now()}'

class UI:
	customtkinter.set_appearance_mode("System")
	customtkinter.set_default_color_theme("blue")
	app = customtkinter.CTk()
	app.title("VSpammer")
	app.geometry("200x240")
	app.resizable(False, False)

	buffer = []

	nicks: str = None
	link: str = None
	threads_count: int = 1
	console: customtkinter.CTkTextbox = None


	def get_obj(self, name: str):
		for obj in self.buffer:
			if obj["name"] == name:return obj["obj"]


	def start_click(self):
		try:self.threads_count = int(self.get_obj("th_count").get())
		except ValueError:
			messagebox.showerror("Ошибка", "Укажите число потоков.")
			return
		self.nicks = self.get_obj("name_entry").get() if self.get_obj("name_entry").get() else None
		if self.get_obj("link_entry").get():
			self.link = self.get_obj("link_entry").get()
			self.clear()
			self.buildV2()
			for i in range(self.threads_count):
				Thread(target=self.main, args=(i+1,)).start()
		else:
			messagebox.showerror("Ошибка", "Укажите ссылку на тест.")
			return



	def clear(self):
		for obj in self.buffer:
			obj["obj"].destroy()
		self.buffer=list()


	def out(self, text):
		self.console.configure(state='normal')
		self.console.insert('end', f"\n[{create_time()}] {text}")
		self.console.configure(state='disabled')



	def buildV1(self):
		name_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="Ник (не обязательно)")
		link_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="Ссылка на тест")
		th_count = Spinbox(master=self.app, from_=1, to=100, width=5)
		th_lbl = customtkinter.CTkLabel(master=self.app, text="Коло-во потоков:")
		button = customtkinter.CTkButton(master=self.app, text="Запустить", command=self.start_click)
		name_entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
		link_entry.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)
		th_lbl.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
		th_count.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
		button.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

		for obj in [name_entry, link_entry, th_count, button, th_lbl]:
			for name, value in locals().items():
				if value is obj:
					self.buffer.append({"obj": obj, "name": name})
	
	def buildV2(self):
		self.app.geometry("800x600")
		self.app.title("VSpammer : Vseosvita test spammer")
		self.console = customtkinter.CTkTextbox(master=self.app, width=750, height=500)
		self.console.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
		self.console.configure(state='disabled')
		customtkinter.CTkButton(master=self.app, text="github", command=lambda: wopen("https://github.com/xXxCLOTIxXx")).place(relx=0.2, rely=0.95, anchor=customtkinter.CENTER)
		customtkinter.CTkButton(master=self.app, text="telegram", command=lambda: wopen("https://t.me/DxsarzUnion")).place(relx=0.4, rely=0.95, anchor=customtkinter.CENTER)
		customtkinter.CTkButton(master=self.app, text="discord", command=lambda: wopen("https://discord.gg/GtpUnsHHT4")).place(relx=0.6, rely=0.95, anchor=customtkinter.CENTER)
		customtkinter.CTkButton(master=self.app, text="youtube", command=lambda: wopen("https://www.youtube.com/@Xsarzy")).place(relx=0.8, rely=0.95, anchor=customtkinter.CENTER)



	
	def main(self, num: int):
		self.out(f"Запущен поток [{num}]")
		while True:
			b = browser()
			try:
				b.start_test(link=self.link, nick=self.nicks)
				self.out(f"[{num}]Тест запущен.")
			except (NoButton, NoInputName):
				self.out(f"[{num}]Не обнаружены элементы запуска. возможно указана неверная ссылка.")
			except InvalidArgumentException:
				self.out(f"[{num}]Некорректная ссылка.")
				break
			finally:
				b.browser.quit()






if __name__ == "__main__":
	ui = UI()
	ui.buildV1()
	UI().app.mainloop()