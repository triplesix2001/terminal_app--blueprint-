import team_mode
import channel_mode
import group_mode
import sys

def main():
    """Entry point for the application."""
    current_mode = None

    while True:
        command = input(f"Current mode: {current_mode}\n"
                        f"Enter 'team', 'channel', or 'group' to switch modes, or 'exit' to quit: ")

        if command.lower() == "exit":
            break

        # Validate and switch modes
        if command.lower() in ("team", "channel", "group"):
            new_mode = command.lower()
            if new_mode != current_mode:
                if new_mode == "team":
                    current_mode = "team"
                    team_mode.main()  # Invoke team-specific logic
                elif new_mode == "channel":
                    current_mode = "channel"
                    channel_mode.main()  # Handle channel operations
                else:
                    current_mode = "group"
                    group_mode.main()  # Address group functionality
            else:
                print("You are already in this mode.")
        else:
            print("Invalid command. Please enter 'team', 'channel', 'group', or 'exit'.")

if __name__ == "__main__":
    main()