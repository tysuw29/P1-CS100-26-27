# Mod Bot - Lesson 5A
# Run the file after every step.

# STEP 1 > define run_command(message) and catch IndexError


# STEP 2 > read the days with int() and catch ValueError


# STEP 3 > move the Banned line into else, and log in finally


# CHECK: three calls, no crash, every call ends with a Logged line.

# DONE EARLY: try run_command("") and add a !mute command.
def run_command(message):
    try:
        parts = message.split()
        who = parts[1]
        days = int(parts[2])
    except IndexError:
        print("Missing command parts")
    except ValueError:
        print("Days not a number")
    else:
        print("Banned", who, days)
    finally:
        print("Logged", message)
        
run_command("!ban Sam 7")
run_command("!ban")
run_command("!ban sam seven")