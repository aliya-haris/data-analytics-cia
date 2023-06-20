The Language Learning Tutor:
This application, "The Language Learning Tutor" is an interactive Spanish learning tutor that allows users to learn Spanish words by inputting English words and receiving their corresponding Spanish translations using the Google Translate API. Users can sign up with a username and password or login to their existing account and continue learning. The words learned by each user are stored in a CSV file of their respective names and later accessed to create personalised quizzes and track the progress of learning. 

Function descriptions:

1. sign_up: This function registers a new user by taking their username and password as inputs so that their learning and progress is logged. The sign up function appends the new username and password to the existing CSV file titled, login.csv and creates a new file if it does not exist.
   
2. login: This function authenticates the user by checking if their username is present in the existing CSV file, login.csv and if user exists, the function then verifies the user's password. This is acheived by comparing the entered username with the stored usernames, prompting for the correct password and allowing user to proceed if the password  matches.

3. learn: This function translates the provided English word to Spanish by utilising the 'GoogleTranslator' class from the 'deep_translator' library.

4. save_words: This function creates a user-specific CSV file by naming the file with the user's name and appends the learned English words along with their Spanish translations to the specific file for further access and use.

5. display: This function collects and displays the English words along with their corresponding Spanish translations for a specific user. This is done by reading the user-specific CSV file, creating a pandas DataFrame and printing it if required.

6. quiz: This function randomly selects words from the user's CSV file and asks the user to provide the Spanish translations for the learned English words. Further, it keeps track of the number of words attempted, the correct responses and the incorrect responses.

7. progress: This function displays the user-specific number of words attempted, the correct responses and the incorrect responses by storing the counted values in a dictionary 'counter' to assess the user's learning.

8. main: This function provides a menu-driven interface for users to sign up, login, learn translations, take quizzes, display learned words, view their progress and exit the program.


Working:

Upon entering the program, the menu is displayed,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/05e8f14c-fc4b-4d49-b718-f9d548468492)


If the user selects 1,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/79ede876-683c-4c0c-86fb-83cb89606823)


If the user selects 2,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/7b408482-dc07-4866-b83f-a245aab607e5)

The created usernames and passwords are stored in the login.csv file,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/a666d7b5-89a6-44a5-a09b-d9f5513947d5)


However, if the password is incorrect,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/90f1797d-eb7d-49a9-a5b7-eaf23b3d733a)

And, if the user does not exist,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/1bbd5cd5-3a40-4101-bc25-4bb80a8c704a)


After signing up or logging in succesfully, the possible functions are displayed,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/32881a5d-701b-4d18-a558-20f4bb25e671)

When the user selects 3,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/1b674ba6-9a59-45e8-b890-bf6b1a28c695)

A file with the user's name is created and the words are appended into the file,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/90a4aba1-949d-4f5a-8cbe-a6322bae05de)

When the user selects 4,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/1bddf501-e8d8-4516-a4ab-eb79de8f0e8b)


When the user selects 5,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/48f0e0e4-1f88-4d41-a45c-652c9ae45397)

When the user selects 6, 

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/8844bcc0-5d4b-46f5-9e1a-86de542a728b)

When the user selects 7,

![image](https://github.com/aliya-haris/data-analytics-cia/assets/118895322/50785ad1-9310-4fbe-a417-8b58c37c8a7f)
