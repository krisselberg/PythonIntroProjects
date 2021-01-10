# Pomodoro method for interval work automated through notification app in MacOS
import time
import os

# Notification system (for MacOS) dependent on which Pomodoro technique you choose in the command line
def pomo(duration, period):
    start = time.time()
    while True:
        os.system(f'''
                  osascript -e 'display notification "{"Your Pomodoro session has started."}" with title "{"Start Working!"}"'
                  ''')
        os.system('say "be less impressed and be more involved"')
        time.sleep(period*60)
        if period == 25:
            os.system(f'''
                      osascript -e 'display notification "{"Relax, get some coffee, and declutter your brain."}" with title "{"Take a 5 minute break."}"'
                      ''')
            os.system('say "take a five minute break and relax"')
            time.sleep(300)
            os.system(f'''
                      osascript -e 'display notification "{"You have the work ethic and courage to tackle this task."}" with title "{"Get back to work!"}"'
                      ''')
            os.system('say "get back to work"')
        elif period == 45:
            os.system(f'''
                      osascript -e 'display notification "{"Relax, get some coffee, and declutter your brain."}" with title "{"Take a 15 minute break."}"'
                      ''')
            os.system('say "take a fifteen minute break and relax"')
            time.sleep(900)
            os.system(f'''
                      osascript -e 'display notification "{"You have the work ethic and courage to tackle this task."}" with title "{"Get back to work!"}"'
                      ''')
            os.system('say "get back to work"')
        elif period == 50:
            os.system(f'''
                      osascript -e 'display notification "{"Relax, get some coffee, and declutter your brain."}" with title "{"Take a 10 minute break."}"'
                      ''')
            os.system('say "take a ten minute break and relax"')
            time.sleep(600)
            os.system(f'''
                      osascript -e 'display notification "{"You have the work ethic and courage to tackle this task."}" with title "{"Get back to work!"}"'
                      ''')
            os.system('say "get back to work"')
        if time.time() > start + period : break

# Taking input from the user to run Pomodoro program
def command():
    duration = int(input("How many hours will you be working for?"))
    period = int(input("Will you be working in 25, 45, or 50 minute periods?"))
    print(period)
    if period != 25 and period != 45 and period != 50 :
        print("That is not a valid option. Please try again.")
        command()
        pomo(duration, period)
    pomo(duration, period)

command()
