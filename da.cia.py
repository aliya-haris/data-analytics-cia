import csv
import os
import pandas as pd

def sign_up(username, password):
    with open("C:\\Users\\aliya\\OneDrive\\Documents\\login.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        
def login(username):
    with open("C:\\Users\\aliya\\OneDrive\\Documents\\login.csv", 'r') as file:
        check = file.readlines()
        for row in check:
            saved_name, saved_pass = row.strip().split(',')
            if saved_name == username:
                saved_password = saved_pass
                break
            else:
                print("User does not exist. Proceed to sign up.")
        while True:
            password = input(">>> Password: ")
            if password == saved_password:
                print("\n▸ Successfully logged in. Continue your learning journey.")
                break
            else:
                print("Incorrect password. Try again.")

from deep_translator import GoogleTranslator
def learn(word):
        result = GoogleTranslator(source = 'en', target = 'es').translate(word)
        return result
    
def save_words(username, learned):
    filename = f"C:\\Users\\aliya\\OneDrive\\Documents\\{username}_words.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline = '') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["English Word", "Spanish Translation"])
        writer.writerows(learned)
                   
def display(username, print_df = True):
        filename = f"C:\\Users\\aliya\\OneDrive\\Documents\\{username}_words.csv"
        if os.path.isfile(filename):
            eng_words = []
            translations = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                headers = next(reader)
                for row in reader:
                    eng_words.append(row[0])
                    translations.append(row[1])
            data = {"English Word": eng_words,"Spanish Translation": translations}
            df = pd.DataFrame(data, index = range(1, len(eng_words) + 1))
            if print_df:
                print("\nLearned words: ")
                print()
                print(df)
            return df
        else:
            return "You have not started your learning journey. Proceed to the learning panel to begin."
    

def quiz(username, counter):
    df = display(username, print_df = False)
    if df is not None:
        filename = f"C:\\Users\\aliya\\OneDrive\\Documents\\{username}_words.csv"
        if os.path.isfile(filename):
            words_for_quiz = df.sample(n=max(1, len(df)))
            print("\n⚬ Good luck with remembering!")
            print("⚬ Translate the displayed English words to Spanish: ")    
            for i, row in words_for_quiz.iterrows():
                word = row['English Word']
                correct_translation = row['Spanish Translation']
                user_translation = input(f"\nTranslation of '{word}': ")
                counter['Word Count'] += 1
                
                if user_translation.lower() == correct_translation.lower():
                    counter['Correct Count'] += 1
                    print("\n--> Correct answer!")
                else:
                    counter['Incorrect Count'] += 1
                    print(f"\n--> Incorrect. The correct translation is {correct_translation}")       
        else:
            print("You have not started your learning journey. Proceed to the learning panel to begin.")
    else:
        print("Proceed to the learning panel to learn words before taking the quiz.")
    
def progress(username, counter):
    print("\nResults:")
    print(f"Number of words attempted: {counter['Word Count']}")
    print(f"Number of correct answers: {counter['Correct Count']}")
    print(f"Number of incorrect answers: {counter['Incorrect Count']}")

    
def main():
    verified = False
    counter = {'Word Count': 0, 'Correct Count': 0, 'Incorrect Count': 0}
    print("╔══════════════════════════════════════════╗\n")
    print("║       THE LANGUAGE LEARNING TUTOR        ║\n")
    print("╚══════════════════════════════════════════╝")
    print("Learn Spanish words and test your learning.")
    while True:
        if not verified:
            print("\n________________________________")
            print(" Main Menu")
            print("     1. Sign up                  ")
            print("     2. Already signed up? Login ")
            print("_________________________________")
        else:
            print("______________________________")
            print("⇨ Choose any task")
            print("      3. Learn translation ")
            print("      4. Quiz")
            print("_______________________________")
            print("⇨ Other options")
            print("      5. Display learned words")
            print("      6. View progress")
            print("      7. Exit tutor")
            print("______________________________")
            
        ch = int(input("\n⇨ Enter your choice: "))
        
        if ch == 1:
            username = input("\n> Enter a username: ")
            password = input("> Enter a password: ")
            sign_up(username, password)
            print("\n▸ Successfully signed up. Enter your learning journey.")
            verified = True
        
        elif ch == 2:
            username = input("\n>>> Username: ")
            login(username)
            verified = True
            
        elif ch == 3 and verified:
            learned = []
            while True:
                word = input("\nEnglish Word to translate: ")
                translation = learn(word)
                print("↪Spanish Translation:", translation)
                learned.append([word, translation])
                response = input("\nDo you want to learn another word? Enter YES/NO: ").lower()
                if response != 'yes':
                    break
            save_words(username, learned)
            print('\nYour learning has been logged.')
                
        elif ch == 4 and verified:
            quiz(username, counter)
            
        elif ch == 5 and verified:
            display(username)
            
        elif ch == 6 and verified:
            progress(username, counter)
            
        elif ch == 7 and verified:
            print("Thank you for using the Language Learning Tutor! Hope you enjoyed your learning journey!")
            break
        else:
            print("Invalid choice")
main()
