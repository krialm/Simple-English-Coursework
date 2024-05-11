# Coursework Report

## 1. Introduction

### a. What is your application?

The application is a simple English learning tool. It uses a graphical user interface to display random words from a selected topic to the user. The user can then attempt to translate the word.

### b. How to run the program?

To run the program, you need to have Python installed on your machine. After that, you can run the program by executing the main script in your terminal or command prompt.

### c. How to use the program?

Once the program is running, you can select a topic and set a timer. The program will then display random words from the selected topic at the interval set by the timer.

## 2. Body/Analysis

### a. Explain how the program covers (implements) functional requirements

The program implements the functional requirements through several classes and methods. The `App` class is the main class that controls the application. It uses the Singleton design pattern to ensure that only one instance of the class is created. The `AppConfigurator` abstract base class defines the methods that the `App` class needs to implement. These methods include loading user data, loading words, creating a user, and setting up the window.

Here is a snippet of the code:

```python
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
