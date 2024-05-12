# Simple-Dimle-English Course Work Report
## 1. Introduction

### a. What is Simple-Dimle-English?

Simple-Dimle-English is a simple English learning tool which can make your English study journey more enjoyable and efficient. It uses a graphical user interface to display random words from a selected topic to the user.

### b. How to run the program?

To run the program on your machine should be installed python and next libraries:

- pandas
- tkinter
- customtkinter
- openpyxl

Then you need to run user.py file. 

### c. How to use the program?

Once the program is running, you can select one of 5 prepared topics and set a timer.

![image](https://github.com/krialm/Simple-Dimle-English/assets/93251167/9fc8787d-56f6-4629-afeb-210904d66976)

The program will then display random words from the selected topic at the interval set by the timer.

Your data will be saved into json file and during the next usage all your data will be loaded. 

You can change parameters at any time pressing the button 'Change parameters'

![image](https://github.com/krialm/Simple-Dimle-English/assets/93251167/f87b45a0-caee-4f39-8408-70962bb04290)


## 2. Body/Analysis

### Explain how the program covers (implements) functional requirements

#### Object-Oriented Programming (OOP) Concepts:

### 1. Encapsulation:
   
- Data (df, timer, words_indexes, topics) and methods (load_user_data, create_user, etc.) are encapsulated within the App class.
  
``` python

    def __init__(self):
        customtkinter.set_appearance_mode("Dark") 
        self.df = pd.DataFrame()
        self.timer = 5
        self.words_indexes = []
        self.window_width = 400
        self.window_height = 120 
        self.is_new_user = True 
        self.user_data_path = 'user_data.json'
        files = os.listdir('topics')
        self.topics = []
```

- User data is stored in a user_data.json file, hiding access details from other parts of the code.

### 2. Inheritance:
   
   - The main class App inherits class AppConfigurator. A base class AppConfigurator with abstract methods for core functionalities like load_user_data, load_words, create_user, and setting_window. These methods define the expected behavior without implementation details.
  
``` python
class App(AppConfigurator, metaclass=SingletonMeta):
```

### 3. Polymorphism:

- The load_words method takes an optional testing_path argument, demonstrating how a single method can perform different actions based on provided data.

``` python
    def load_words(self, testing_path=None):
        if testing_path is not None:
            return pd.read_excel(testing_path)

        self.df = pd.read_excel(fr'topics/{self.topic}.xlsx')
```

- The get_word method uses a loop to ensure unique words presented during practice, exhibiting a variation in behavior based on specific conditions.

``` python
    def get_word(self):
        word_ind = randint(0, len(self.df)-1)
        while True:
            if word_ind not in self.words_indexes:
                self.words_indexes.append(word_ind)
                return word_ind
            word_ind = randint(0, len(self.df))
```

### 4. Abstraction:

- The AppConfigurator class serves as an abstract base class, defining the core functionalities required for user data management, word loading, and user interface creation. By employing abstract methods (load_user_data, load_words, create_user, and setting_window), it establishes a blueprint for child classes to inherit and implement. This approach fosters code reusability and promotes a well-structured foundation for future program extensions.

``` python
class AppConfigurator(ABC):
    @abstractmethod
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
```

## Used design patterns: 
### 1. Singleton:
- This pattern is implemented through the SingletonMeta metaclass. This metaclass restricts the creation of the App class to a single instance throughout the program's lifetime. Here's why this is beneficial:

``` python
class SingletonMeta(ABCMeta):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
```

### 2. Decorator:

- Using decoration pattern we created and modifyed method from AppConfigurator class and used decoratos do define abstract methods.

``` python 
@abstractmethod
```

### Testing:

#### Challenges with Unit Testing GUI Applications:

- Direct User Interaction: GUI applications rely heavily on user input and interaction with visual elements, which can't be easily replicated in unit tests.
  
-Graphical Interface Logic: The logic for handling window resizing, layout adjustments, and interaction with UI components is often intertwined with the UI code itself, making unit isolation difficult.

- State Management: Testing different UI states (e.g., active/inactive buttons, error messages) can be challenging within a unit testing framework.

The provided code demonstrates unit tests for a few specific functions within the App class:

``` python
import unittest
import pandas as pd
from user import App

class TestApp(unittest.TestCase):


    def test_load_App_data(self):
        # Test loading App data from a file
        data = App.load_user_data(App,'user_data.json') # 
        self.assertIsInstance(data, dict) # если все ок то загружаем словать
        self.assertEqual(data['topic'], 'Programming_Vocabulary')
        self.assertEqual(data['timer'], "5")
        self.assertEqual(data['window_position'], '520+390')


    def test_load_words(self):
        df = App.load_words(App, '/Users/togzhandikhan/Documents/Simple-Dimle-English/topics/Medical_Vocabulary.xlsx')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iat[1, 0], "diagnosis")
        self.assertEqual(df.iat[1, 1], "диагноз")



if __name__ == '__main__':
    unittest.main()
```

![image](https://github.com/krialm/Simple-Dimle-English/assets/93251167/d1e39eb1-64cf-4d6f-bacd-f2aaef364990)


## Results 

- This program successfully builds a flashcard application for learning English vocabulary using libraries like pandas and customtkinter.

- Users can choose topics, view random words with translations, and control the time interval between words.

- A challenge faced during development might be designing a user-friendly interface that integrates effectively with the data management functionalities.

Int the future will be added the features such as:

- User-Created Flashcards: Empower users to create their own flashcards. This can involve adding new words and translations directly within the application, allowing for personalized vocabulary sets based on specific needs or interests.

- Custom Dataset Creation: Enable users to build their own datasets. This could involve importing vocabulary lists from external files or creating them directly in the application. Users could then choose their preferred datasets for practicing.

## Conclusion:

In conclusion, Simple-Dimple-English program demonstrate the creation of a functional flashcard application for learning English vocabulary. Users can select topics, view random words with translations, and control the pace of learning through a timer function. A key challenge involved balancing an intuitive interface with the underlying data structures.

Looking forward, the program holds promise for further development. Future iterations could empower users to create their own flashcards and datasets, fostering personalized learning experiences. Additionally, functionalities like progress tracking and text-to-speech integration could enhance the overall learning effectiveness. By incorporating user-generated content and advanced features, this program has the potential to become a comprehensive and adaptable tool for vocabulary acquisition.

## Sources:

pandas documentation - https://pandas.pydata.org/docs/

customtkinter documentation -https://github.com/topics/customtkinter

tkinter documentation - https://docs.python.org/3/library/tk.html

unittest documentation - https://docs.python.org/3/library/unittest.html
