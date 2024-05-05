import pandas as pd
from tkinter import *
import customtkinter # библиотека для работы с интерфейсом
from random import randint
import os
import json
from abc import ABC, abstractmethod, ABCMeta

# хуйня для полиморфизма что-бы использовать функционал и переписовать методы в других классах
class AppConfigurator(ABC):
    @abstractmethod # декоратор используем фунции только всередине
    def load_user_data(self, filename):
        pass

    @abstractmethod
    def load_words(self, testing_path=None):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def setting_window(self):
        pass

# хуйня которая проверяет что был создан только один обект класса
class SingletonMeta(ABCMeta):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class App(AppConfigurator, metaclass=SingletonMeta): # UserConfigurator, ABC, metaclass=SingletonMeta - 
    def __init__(self):
        customtkinter.set_appearance_mode("Dark") 
        self.df = pd.DataFrame() # датафрейм - структура данных в которой храняться слова
        self.timer = 5 # эта хуйня испольуеться дальше в этом класе по этому это инкапсуляция
        self.words_indexes = []
        self.window_width = 400 # эта хуйня испольуеться дальше в этом класе по этому это инкапсуляция
        self.window_height = 120 # эта хуйня испольуеться дальше в этом класе по этому это инкапсуляция
        self.is_new_user = True 
        self.user_data_path = 'user_data.json'
        files = os.listdir('topics')
        self.topics = []
        # убираем из названия файлов .xlsx
        for i in files:
            self.topics.append(i.replace('.xlsx', ''))
        

        # елси до этого не был создан юзер мы создаем его
        if not os.path.exists(self.user_data_path):
            self.setting_window()

        # если до этого юзер былсозда мы подгружаем дату с файла    
        else:
            self.is_new_user = False
            user_data = self.load_user_data(self.user_data_path)
            self.topic = user_data['topic']
            self.timer = user_data['timer']
            self.window_position = user_data['window_position']
            self.load_words()
            self.start_app()

    # полиморфизм
    def load_user_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return data

    # полиморфизм 
    def load_words(self, testing_path=None):
        if testing_path is not None:
            return pd.read_excel(testing_path)

        self.df = pd.read_excel(fr'topics/{self.topic}.xlsx') # инкапсуляция


    # полиморфизм
    def create_user(self):
        self.df = pd.read_excel(f'topics/{self.topics_var.get()}.xlsx') # инкапсуляция
        with open(self.user_data_path, "w") as file:
            json.dump({'topic': self.topics_var.get(), 'timer': self.timer.get(), 'window_position': self.window_position}, file)
        self.root.destroy()
        self.start_app()

    def setting_window(self):
        self.root = customtkinter.CTk() # окно
        self.root.title("Simple Dimple English🍪")
        screen_width = self.root.winfo_screenwidth() # ширина экрана
        screen_height = self.root.winfo_screenheight() # длина экрана
        self.x_position = (screen_width - self.window_width) // 2 # центр экрана инкапсуляция
        self.y_position = (screen_height - self.window_height) // 2 # инкапсуляция
        self.window_position = f"{self.x_position}+{self.y_position}"
        self.root.geometry(f'400x120+{self.window_position}') # размер и позиция окна
        
        frame = customtkinter.CTkFrame(self.root) # часть в окне со всеми хуйнюшками 
        frame.pack(fill='both', expand=True) # запихиваем зуйнбшку в окно

        self.timer = StringVar(value=self.timer)
        self.topics_var = StringVar(value=self.topics[0]) 

        choose_topic_label = customtkinter.CTkLabel(frame, text="Choose the topic:")
        choose_topic_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=W)  
        combobox = customtkinter.CTkComboBox(frame,width=170, variable=self.topics_var, values=self.topics)
        combobox.grid(row=0, column=1, columnspan=2, padx=20, pady=5, sticky=W+E)  
        timer_entry = customtkinter.CTkEntry(frame, width=50, textvariable=self.timer)
        timer_entry.grid(row=2, column=1, pady=5, sticky=W)  
        timer_label = customtkinter.CTkLabel(frame, text='Timer (in min)')
        timer_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)  
        continue_button = customtkinter.CTkButton(frame, text="Continue", command=self.create_user)
        continue_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        self.root.mainloop() # отображение окошка


    def get_word(self):
        word_ind = randint(0, len(self.df))
        while True:
            if word_ind not in self.words_indexes:
                self.words_indexes.append(word_ind)
                return word_ind
            word_ind = randint(0, len(self.df))

    def start_timer(self):
        self.root.withdraw()
        if self.is_new_user: 
            self.root.after(int(60*float(self.timer.get())*1000), self.start_app)
        else:
            self.root.after(int(60*float(self.timer)*1000), self.start_app)

    
    def start_app(self):
        self.root = customtkinter.CTk() 
        self.root.title("Simple Dimple English🍪")
        self.root.geometry(f'450x150+{self.window_position}')
        frame = customtkinter.CTkFrame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)  
        word_ind = self.get_word() # рандомное слово которое не использовалось
        label_font = ("Arial", 14, "bold")
        word = customtkinter.CTkLabel(frame, text=f'{self.df.iat[word_ind, 0]}', font=label_font)# инкапсуляция
        word.grid(row=0, column=0, sticky='e', padx=10, pady=10)  
        translation = customtkinter.CTkLabel(frame, text=f'{self.df.iat[word_ind, 1]}', font=label_font)# инкапсуляция
        translation.grid(row=0, column=2, sticky='e', padx=10, pady=10)
        got_it_button = customtkinter.CTkButton(frame, text="Got It!", command=self.start_timer)
        got_it_button.grid(column=1, row=3, pady=20) 
        self.root.mainloop()

if __name__ == '__main__':
    user = App() # при создании обекта класса выполняеться программа
