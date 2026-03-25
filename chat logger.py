from datetime import datetime

while True:
    print("\n--- Chat System ---")
    print("1. Send Message")
    print("2. View Chat")
    print("3. clear chat")
    print("4.Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        msg = input("Enter message: ").strip()

        if msg == "":
            print("Message cannot be empty")
            continue

        msg_time = datetime.now().strftime("[%H:%M:%S]")

        with open("chat.txt", "a") as file:
            file.write(f"{msg_time} harsha: {msg}\n")

        print("Message sent...")

    elif choice == "2":
        try:
            print("\n--- Chat History ---")
            with open("chat.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No chat history found")

    elif choice == "3":
        confirm = input("Are you sure? (yes/no): ").lower()
        if confirm == "yes":
            with open("chat.txt", "w") as file:
                pass
                print("Chat history cleared!")
        else:
            print("Cancelled")
    elif choice=="4":
        print("Bye")
        break

    else:
        print("Invalid choice")
