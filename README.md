The Language Learning Tutor:
This application, "The Language Learning Tutor" is an interactive Spanish learning tutor that allows users to learn Spanish words by inputting English words and receiving their corresponding Spanish translations using the Google Translate API. Users can sign up with a username and password or login to their existing account and continue learning. The words learned by each user are stored in a CSV file of their respective names and later accessed to create personalised quizzes and track the progress of learning. 

Function descriptions:

1. sign_up: This function registers a new user by takin their username and password as inputs so that their learning and progress is logged. The sign up function appends the new username and password to the existing CSV file titled, login.csv and creates a new file if it does not exist.
   
2. login: This fucntion authenticates the user by checking if their username is present in the existing CSV file, login.csv and if user exists, the function then verifies the user's password. This is acheived by comparing the entered username with the stored usernames, prompting for the correct password and allowing user to proceed if the password  matches.

3. learn: This function translates the provided English word to Spanish by utilising the 'GoogleTranslator' class from the 'deep_translator' library.

4. save_words: This function creates a user-specific CSV file by naming the file with the user's name and appends the learned English words along with their Spanish translations to the specific file for further access and use.

5. display: This function collects and displays the English words along with their corresponding Spanish translations for a specific user. This is done by reading the user-specific CSV file, creating a pandas DataFrame and printing it if required.

6. quiz: This function randomly words from the specific user's CSV file and asks the user to provide the Spanish translations for the learned English words. Further, it keeps track of the number of words attempted, the correct responses and the incorrect responses.

7. progress: This function displays the user-specific number of words attempted, the correct responses and the incorrect responses by storing the counted values in a dictionary 'counter' to assess the user's learning.

8. main: This function provides a menu-driven interface for users to sign up, login, learn translations, take quizzes, display learned words, view their progress and exit the program.


Upon entering the program, the menu is displayed,





If the user selects 1,






If the user selects 2,






if the password is incorrect,

if the user does not exist,


After signing up or loggin in succesfully, the possible functions are displayed,


When the user selects 3,




When the user selects 4,




When the user selects 5,



When the user selects 6, 



When the user selects 7,



When the user selects 8,


