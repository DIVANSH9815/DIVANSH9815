import time
import datetime
import pygame

def set_alarm(alarm_set):
    print(f"Alarm set for {alarm_set}")
    
    sound_file = "C:\python.py\__pycache__\justin-bieber-type-beat-pop-rnb-freedom-by-tremoxbeatz-216870 (1).mp3"  # Ensure the file exists in the same directory
    is_running = True  # Correct loop condition
    
    while is_running:  
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Removed spaces
        print(current_time, end="\r")  # Print in the same line
        
        if current_time == alarm_set:  # Correct format comparison
            print("\nTime Up!")  
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False  # Stop the loop

        time.sleep(1)  # Prevent CPU overuse

if __name__ == "__main__": 
    alarm_set = input("Enter Your Alarm Time (HH:MM:SS): ")  # Corrected prompt format
    set_alarm(alarm_set)

