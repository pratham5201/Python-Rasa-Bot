import os
# #Step 0: Retrive the data from html file
# os.system("python my_html_parser.py")
# # Step 1: Prepare Data
# os.system("python prepare_data.py")

# # Step 2: Prepare Responses
# os.system("python prepare_responses.py")

# # Step 3: Prepare Stories
# os.system("python prepare_stories.py")


#Step 4: Train NLU Model
# os.system("python train_nlu.py")


# # Step 5: Train Dialogue Model
# os.system("python train_dialogue.py")


# ngrok start --config=ngrok.yml --all



import subprocess
import os

def train_rasa():
    # Run Rasa training command
    subprocess.run(["rasa", "train"])

def run_rasa_shell():
    # Run Rasa shell command
    subprocess.run(["rasa", "shell"])

if __name__ == "__main__":
    # Train Rasa
    train_rasa()

    # Run Rasa shell
    run_rasa_shell()