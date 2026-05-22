import os
import sys
import shlex
import random
import time
import code

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cmd_help():
    print("Available commands:")
    print("- help : show this menu")
    print("- clear : clear the screen")
    print("- exit : quit AquaShell")
    print("- echo <text> : repeat back your text")
    print("- cd <path> : change directory")
    print("- pwd : show current directory")
    print("- dir : list files in current directory")
    print("- react <emoji/text> : print a reaction")
    print("- matrix : show a matrix rain effect")
    print("- dice : roll a six-sided dice")
    print("- joke : tell a random joke")
    print("- python : open a mini Python REPL")

def cmd_echo(args):
    if not args:
        print("Usage: echo <text>")
        return
    print(" ".join(args))

def cmd_cd(args):
    if not args:
        print("Usage: cd <path>")
        return
    try:
        os.chdir(args[0])
        print(f"Changed directory to {os.getcwd()}")
    except Exception as e:
        print(f"Error: {e}")

def cmd_pwd():
    print(os.getcwd())

def cmd_dir():
    try:
        for item in os.listdir(os.getcwd()):
            print(item)
    except Exception as e:
        print(f"Error: {e}")

def cmd_react(args):
    if not args:
        print("Usage: react <emoji/text>")
        return
    print(f"Reaction: {args[0]}")

def cmd_matrix():
    chars = "01"
    print("Matrix rain... press Ctrl+C to stop")
    try:
        while True:
            line = "".join(random.choice(chars) for _ in range(60))
            print(line)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Matrix stopped")

def cmd_dice():
    roll = random.randint(1, 6)
    print(f"You rolled a {roll} 🎲")

def cmd_joke():
    jokes = [
        "Why don’t programmers like nature? Too many bugs.",
        "I told my computer I needed a break… it said 'No problem, I’ll go to sleep.'",
        "Why do Java developers wear glasses? Because they don’t see sharp."
    ]
    print(random.choice(jokes))

def cmd_python():
    print("Entering mini Python REPL. Type exit() to quit.")
    code.interact(local=dict(globals(), **locals()))

def main():
    clear_screen()
    print("=== AquaShell v0.1 Useful + Fun Edition ===")
    print("Type 'help' for commands, 'exit' to quit.\n")

    while True:
        try:
            raw = input("AquaShell$ ")
            parts = shlex.split(raw)
            if not parts:
                continue
            cmd, *args = parts

            if cmd == "help":
                cmd_help()
            elif cmd == "clear":
                clear_screen()
            elif cmd == "exit":
                print("Exiting AquaShell...")
                sys.exit(0)
            elif cmd == "echo":
                cmd_echo(args)
            elif cmd == "cd":
                cmd_cd(args)
            elif cmd == "pwd":
                cmd_pwd()
            elif cmd == "dir":
                cmd_dir()
            elif cmd == "react":
                cmd_react(args)
            elif cmd == "matrix":
                cmd_matrix()
            elif cmd == "dice":
                cmd_dice()
            elif cmd == "joke":
                cmd_joke()
            elif cmd == "python":
                cmd_python()
            else:
                print(f"Unknown command: {cmd}")

        except KeyboardInterrupt:
            print("\nInterrupted. Exiting AquaShell...")
            sys.exit(0)

if __name__ == "__main__":
    main()
