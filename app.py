import tkinter
from tkinter import messagebox
import file_handler


class AnxietyExposureWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Anxiety Exposure Tracker")
        self.window.geometry("500x500")
        self.window.iconbitmap("anxiety_exposure.ico")
        self.score = 0

        self.score_label = tkinter.Label(self.window, text=f"Score: {self.score}", font=(None, 20))
        self.score_label.pack(pady=30)

        # Scrollable listbox
        self.scrollbar_frame = tkinter.Frame(self.window)
        self.scrollbar = tkinter.Scrollbar(self.scrollbar_frame, orient=tkinter.VERTICAL)

        self.listbox = tkinter.Listbox(self.scrollbar_frame, width=55,
                                       yscrollcommand=self.scrollbar.set, selectmode=tkinter.SINGLE,
                                       font=("TkFixedFont", 10))
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.listbox.pack(pady=20)
        self.scrollbar_frame.pack(side=tkinter.TOP)

        # Buttons
        self.performed_button = tkinter.Button(self.window, text="Performed", width=15)
        self.performed_button.pack(pady=30, side=tkinter.TOP)

        self.buttons_frame = tkinter.Frame(self.window)

        self.edit_button = tkinter.Button(self.buttons_frame, text="Edit", width=10)
        self.edit_button.pack(padx=30, side=tkinter.LEFT)

        self.add_button = tkinter.Button(self.buttons_frame, text="Add", width=10, command=self.add_button)
        self.add_button.pack(padx=30, side=tkinter.LEFT)

        self.delete_button = tkinter.Button(self.buttons_frame, text="Delete", width=10)
        self.delete_button.pack(padx=30, side=tkinter.LEFT)

        self.buttons_frame.pack(side=tkinter.TOP)

        self.info_label = tkinter.Label(self.window, width=200,
                                        text="The challenge is used to determine difficult you find the exposure.\n"
                                             "The wins is used to track how many times you've done the exposure.")

        self.refresh_list()

    def add_button(self):
        AddWindow()
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tkinter.END)

        data = file_handler.read_from_file()

        for element in data:
            parts = element.split(",")
            description = parts[0]
            difficulty = parts[1]
            performed_num = parts[2]
            self.listbox.insert(tkinter.END,
                                f"{description:<30} | Challenge: [{difficulty:^3}] Wins: [{performed_num:^3}]")

    def start(self):
        self.window.mainloop()


class AddWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Anxiety Exposure Tracker")
        self.window.geometry("470x350")
        self.window.minsize(width=470, height=350)
        self.window.iconbitmap("anxiety_exposure.ico")

        # Entry Descriptions
        self.entry_description_frame = tkinter.Frame(self.window)
        self.description_label = tkinter.Label(self.entry_description_frame, text="Description", width=20)
        self.description_label.pack(side=tkinter.LEFT, padx=10)
        self.difficulty_label = tkinter.Label(self.entry_description_frame, text="Difficulty", width=20)
        self.difficulty_label.pack(side=tkinter.RIGHT, padx=(75, 10))
        self.entry_description_frame.pack(side=tkinter.TOP, pady=30)

        # Entries
        self.entries_frame = tkinter.Frame(self.window)
        self.description_text = tkinter.Text(self.entries_frame, width=20, height=5)
        self.description_text.pack(side=tkinter.LEFT, padx=30)
        self.difficulty_scale = tkinter.Scale(self.entries_frame, width=15, from_=10, to=1)
        self.difficulty_scale.pack(side=tkinter.LEFT, padx=30)
        self.entries_frame.pack(side=tkinter.TOP)

        # Buttons
        self.buttons_frame = tkinter.Frame(self.window)
        self.add_button = tkinter.Button(self.buttons_frame, text="Add", width=10, command=self.add_to_file)
        self.add_button.pack(side=tkinter.LEFT, padx=10)
        self.cancel_button = tkinter.Button(self.buttons_frame, text="Cancel", width=10, command=self.close)
        self.cancel_button.pack(side=tkinter.LEFT, padx=10)
        self.buttons_frame.pack(side=tkinter.TOP, pady=30)

        self.info_label = tkinter.Label(self.window, width=200,
                                        text="Use low numbers for things you find really easy.\n"
                                             "Use high numbers for things you find really difficult."
                                             "\nYou cannot use commas in your description."
                                             "\nTry to keep your description short.")
        self.info_label.pack(side=tkinter.BOTTOM)
        self.window.mainloop()

    def add_to_file(self):
        description = self.description_text.get("1.0", tkinter.END).strip('\n').strip('\t')
        if "," in description:
            messagebox.showerror(
                "There was a comma in the description\nPlease remove any commas from your description.")
        elif len(description) > 50:
            messagebox.showerror("Your description goes over 50 characters. Please try to keep it short.")
        else:
            data = file_handler.read_from_file()
            print(data)
            data_to_write = f"{description},{self.difficulty_scale.get()},0"
            data.append(data_to_write)
            file_handler.write_to_file(data)
            self.close()

    def close(self):
        self.window.destroy()
        del self


AnxietyExposureWindow().start()
