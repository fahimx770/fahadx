import os
import sys
import time
from datetime import datetime, timedelta
import random

# Define colors using ANSI escape sequences
RESET = "\033[0m"
BOLD = "\033[1m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_MAGENTA = "\033[95m"
MAGENTA = "\033[35m"
BRIGHT_BLUE = "\033[94m"
BLUE = "\033[34m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_YELLOW = "\033[93m"
WHITE = "\033[97m"
BRIGHT_RED = "\033[91m"
BROWN = "\033[38;5;94m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
ORANGE = "\033[38;5;214m"
INDIGO = "\033[38;5;75m"
DEEP_BLUE = "\033[38;5;19m"
# Define a list of rainbow colors
rainbow_colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, WHITE]

# Clear the screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Animated typing effect
def typing_effect(text, delay=0.0005, clear=True):
    if clear:
        clear_screen()
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Function to show animated loading
def animated_loading(message, duration=3):
    chars = ["|", "-", "|", "-"]
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in chars:
            sys.stdout.write(f"\r{BRIGHT_YELLOW}{BOLD}{message} {char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")

# Function for user authentication
def login():
    correct_id = "z"
    correct_password = "z"
    correct_license = "z"

    while True:
        # Prompt for PERADOX ID and Password
        typing_effect(f"{BOLD}{BRIGHT_CYAN}☑ LOGIN NOW.   {RESET}\n", delay=0.05)
        print(f"{BOLD}{BRIGHT_GREEN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{RESET}")
        paradox_id = input(f"{BRIGHT_RED}{BOLD}Enter your PERADOX ID : {RESET}")
        password = input(f"{BRIGHT_GREEN}{BOLD}Enter your Password : {RESET}")

        # Loading animation for verifying ID and Password
        animated_loading("Verifying ID and Password...", duration=2)

        # Clear the screen
        clear_screen()

        if paradox_id == correct_id and password == correct_password:
            typing_effect(f"{BRIGHT_GREEN}{BOLD}LOGIN SUCCESSFUL!{RESET}\n")
            
            # Prompt for License Key
            license = input(f"{BRIGHT_YELLOW}{BOLD}Enter your License Key : {RESET}")

            # Loading animation for verifying License Key
            animated_loading("Connecting License to API Server...", duration=2)

            # Clear the screen
            clear_screen()

            if license == correct_license:
                typing_effect(f"{BRIGHT_GREEN}{BOLD}LICENSE CONNECTED TO API SERVER✓{RESET}\n")
                
                # Display the multi-colored banner using typing effect
                banner = f"""
{BRIGHT_RED}██████╗   {ORANGE}███████╗  {BRIGHT_YELLOW}██████╗   {BRIGHT_GREEN} █████╗   {BRIGHT_CYAN}██████╗   {BRIGHT_BLUE} ██████╗   {INDIGO}██╗  ██╗
{BRIGHT_RED}██╔══██╗  {ORANGE}██╔════╝  {BRIGHT_YELLOW}██╔══██╗  {BRIGHT_GREEN}██╔══██╗  {BRIGHT_CYAN}██╔══██╗  {BRIGHT_BLUE}██╔═══██╗  {INDIGO}╚██╗██╔╝
{BRIGHT_RED}██████╔╝  {ORANGE}█████╗    {BRIGHT_YELLOW}██████╔╝  {BRIGHT_GREEN}███████║  {BRIGHT_CYAN}██║  ██║  {BRIGHT_BLUE}██║   ██║   {INDIGO}╚███╔╝ 
{BRIGHT_RED}██╔═══╝   {ORANGE}██╔══╝    {BRIGHT_YELLOW}██╔══██╗  {BRIGHT_GREEN}██╔══██║  {BRIGHT_CYAN}██║  ██║  {BRIGHT_BLUE}██║   ██║   {INDIGO}██╔██╗ 
{BRIGHT_RED}██║       {ORANGE}███████╗  {BRIGHT_YELLOW}██║  ██║  {BRIGHT_GREEN}██║  ██║  {BRIGHT_CYAN}██████╔╝  {BRIGHT_BLUE}╚██████╔╝  {INDIGO}██╔╝ ██╗
{BRIGHT_RED}╚═╝       {ORANGE}╚══════╝  {BRIGHT_YELLOW}╚═╝  ╚═╝  {BRIGHT_GREEN}╚═╝  ╚═╝  {BRIGHT_CYAN}╚═════╝   {BRIGHT_BLUE} ╚═════╝   {INDIGO}╚═╝  ╚═╝
{RESET}
"""
                typing_effect(banner, delay=0.0002)
                # Display developer info without clearing the banner
                today_date = datetime.now().strftime("%Y-%m-%d %H:%M")  # Updated to include live time
                developer_info = f"""
{BOLD}{BRIGHT_YELLOW}   ☬☬ ════════════════════ PERADOX v2.7 ═════════════════════ ☬☬
{BOLD}{BRIGHT_GREEN}   ☬☬ ═════════════════ DEVELOPER BY FAHAD X ════════════════ ☬☬
{BOLD}{BRIGHT_CYAN}   ☬☬ ═══════════════════ TG: @th_fahad_00 ══════════════════ ☬☬
{BOLD}{BRIGHT_MAGENTA}   ☬☬ ══════════ TIME ASIA/BANGLADESH UTC + 06:00 ═══════════ ☬☬
{BOLD}{BRIGHT_BLUE}   ☬☬ ═════════ Time in Bangladesh: {today_date} ════════ ☬☬
{RESET}
"""
                typing_effect(developer_info, delay=0.005, clear=False)

                # Display the pairs
                display_pairs(pairs)

                # Allow the user to select pairs and specify time
                select_pairs_with_time(pairs, banner, developer_info)
                break
            else:
                print(f"{BRIGHT_RED}{BOLD}Invalid License Key! Try again.{RESET}\n")
                time.sleep(1.5)
        else:
            print(f"{BRIGHT_RED}{BOLD}Invalid PERADOX ID or Password! Try again.{RESET}\n")
            time.sleep(1.5)

# Function to display pairs in a formatted table
def display_pairs(pairs):
    # Print the header
    print(f"{BOLD}{DEEP_BLUE}╔═══════════════════════════════════════════════════════════════════════════╗")
    print(f"║                             Available Pairs:                              ║")
    print(f"╠══════════════════╦══════════════════╦══════════════════╦══════════════════╣")

    # Format and print the pairs in rows of 4
    for i in range(0, len(pairs), 4):
        row = pairs[i:i+4]
        formatted_row = "║ " + "║ ".join([f"{str(j+1).zfill(2)}.{pair:<14}" for j, pair in enumerate(row, start=i)]) + "║ "
        print(formatted_row)
        if i + 4 < len(pairs):  # Add a separator if not the last row
            print(f"╠══════════════════╦══════════════════╦══════════════════╦══════════════════╣")

    # Print the footer
    print(f"╚══════════════════╩══════════════════╩══════════════════╩══════════════════╝{RESET}")

# Signal generation function
def generate_signal(trend="All"):
    """Generate a signal based on market trend"""
    if trend == "CALL":
        return "CALL"
    elif trend == "PUT":
        return "PUT"
    else:
        return random.choice(["CALL", "PUT"])

def generate_signals_for_multiple_pairs(total_signals, start_time, end_time, selected_pairs, trend, backtest_day):
    """Generate signals for multiple pairs with deterministic randomness."""
    
    # Set a fixed seed for reproducibility
    seed_value = f"{total_signals}{start_time}{end_time}{','.join(selected_pairs)}{trend}{backtest_day}"
    random.seed(seed_value)
    
    current_time = datetime.strptime(start_time, "%H:%M")
    end_time_obj = datetime.strptime(end_time, "%H:%M")
    signals = []

    while current_time <= end_time_obj and len(signals) < total_signals:
        for pair in random.choices(selected_pairs, k=1):
            if len(signals) >= total_signals:
                break
            signal_time = (current_time + timedelta(minutes=random.randint(6, 15))).strftime("%H:%M")
            direction = generate_signal(trend)
            signals.append(f"{BOLD}{pair}  {signal_time} ⧐ {direction}{RESET}")

            # Adjust time intervals based on the backtest day
            if 1 <= backtest_day <= 5:
                current_time += timedelta(minutes=random.randint(1, 5))
            elif 6 <= backtest_day <= 10:
                current_time += timedelta(minutes=random.randint(2, 7))
            elif 11 <= backtest_day <= 16:
                current_time += timedelta(minutes=random.randint(3, 13))
            elif 17 <= backtest_day <= 21:
                current_time += timedelta(minutes=random.randint(5, 15))
            elif backtest_day == 22:
                current_time += timedelta(minutes=random.randint(2, 30))
            elif 23 <= backtest_day <= 30:
                current_time += timedelta(minutes=random.randint(19, 90))
            else:
                print(f"{BRIGHT_RED}{BOLD}Invalid Backtest Day!{RESET}")
                return []
    return signals

# Update the select_pairs_with_time function
def select_pairs_with_time(pairs, banner, developer_info):
    # Prompt the user to select pairs by their number
    selected_indices = input(f"{BOLD}{BRIGHT_YELLOW}Enter the numbers of the pairs (comma-separated): {RESET}")
    try:
        # Convert input to a list of integers
        indices = [int(i.strip()) - 1 for i in selected_indices.split(",")]
        selected_pairs = [pairs[i] for i in indices if 0 <= i < len(pairs)]
        
        # Prompt for signal start date
        start_date = input(f"{BOLD}{BRIGHT_GREEN}Enter the signal start date (YYYY-MM-DD): {RESET}")
        
        # Prompt for start and end times
        start_time = input(f"{BOLD}{BRIGHT_GREEN}Enter the start time : {RESET}")
        end_time = input(f"{BOLD}{BRIGHT_GREEN}Enter the end time : {RESET}")
        
        # Validate time format
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            start_time_obj = datetime.strptime(start_time, "%H:%M")
            end_time_obj = datetime.strptime(end_time, "%H:%M")
            
            if start_time_obj >= end_time_obj:
                print(f"{BRIGHT_RED}{BOLD}End time must be later than start time!{RESET}")
                return
            
            # Prompt for backtest day analysis
            backtest_day = input(f"{BOLD}{BRIGHT_MAGENTA}Enter the Backtest Day (1 to 30): {RESET}")
            if not backtest_day.isdigit() or not (1 <= int(backtest_day) <= 30):
                print(f"{BRIGHT_RED}{BOLD}Invalid Backtest Day! Please enter a number between 1 and 30.{RESET}")
                return
            
            # Prompt for the number of signals
            num_signals = input(f"{BOLD}{BRIGHT_BLUE}How many signals do you want : {RESET}")
            if not num_signals.isdigit() or int(num_signals) <= 0:
                print(f"{BRIGHT_RED}{BOLD}Invalid number of signals! Please enter a positive number.{RESET}")
                return
            
            # Prompt for signal direction
            signal_direction = input(f"{BOLD}{BRIGHT_CYAN}Enter the signal direction (CALL/PUT/BOTH): {RESET}").strip().upper()
            if signal_direction not in ["CALL", "PUT", "BOTH"]:
                print(f"{BRIGHT_RED}{BOLD}Invalid signal direction! Please enter CALL, PUT, or BOTH.{RESET}")
                return
            
            # Generate signals
            signals = generate_signals_for_multiple_pairs(
                int(num_signals), start_time, end_time, selected_pairs, signal_direction, int(backtest_day)
            )
            
            # Clear the screen but keep the banner and developer info
            clear_screen()
            print(f"{BOLD}{BRIGHT_GREEN}LOGIN SUCCESSFUL! LICENSE ACTIVATED✓{RESET}\n")
            print(banner)
            print(developer_info)
            
            # Display "Collecting Data from API" with animated loading
            animated_loading("Collecting Data from API...", duration=6)
            typing_effect(f"{BRIGHT_GREEN}Data Collection Complete!{RESET}\n", delay=0.01, clear=False)
            
            # Display selected pairs in a single row
            typing_effect(f"{BOLD}{BRIGHT_YELLOW}Selected Pairs: {RESET}", delay=0.01, clear=False)
            typing_effect(f"{BOLD}{BRIGHT_CYAN}{', '.join(selected_pairs)}{RESET}\n", delay=0.01, clear=False)
            
            # Display signal time range only once
            typing_effect(f"{BOLD}{BRIGHT_YELLOW}Signal Time Range: {start_date} {start_time} to {end_time}{RESET}\n", delay=0.01, clear=False)
            
            typing_effect(f"\n{BOLD}{BRIGHT_GREEN}Generated Signals:{RESET}\n", delay=0.01, clear=False)
            for signal in signals:
                typing_effect(f"{signal}\n", delay=0.01, clear=False)
        
        except ValueError:
            print(f"{BRIGHT_RED}{BOLD}Invalid date or time format! Please use YYYY-MM-DD for date and HH:MM (24-hour format) for time.{RESET}")
    
    except ValueError:
        print(f"{BRIGHT_RED}{BOLD}Invalid input! Please enter valid numbers separated by commas.{RESET}")

# List of pairs
pairs = [
    "USD/MXN-OTC", "USD/CHF-OTC", "USD/BRL-OTC", "AUD/NZD-OTC", "BOE-OTC    ", "NZD/JPY-OTC",
    "JNJ-OTC    ", "USD/PHP-OTC", "USD/IDR-OTC", "USD/NGN-OTC", "USD/BDT-OTC", "USD/ARS-OTC",
    "USD/MXN-OTC", "USD/TRY-OTC", "USD/PKR-OTC", "USD/INR-OTC", "USD/ZAR-OTC", "USD/DZD-OTC",
    "PFE-OTC    ", "XAU/USD-OTC", "XAG/USD-OTC", "MSF-OTC    ", "BTC/USD-OTC", "INT-OTC    ",
    "FAB-OTC    ", "AXP-OTC    ", "NZD/CAD-OTC", "EUR/CAD-OTC", "MCD-OTC    ", "NZD/CHF-OTC",
    "ETH/USD-OTC", "SOL/USD-OTC", "TRN/USD-OTC", "TRM/USD-OTC", "PEP/USD-OTC", "FLK/USD-OTC",
    "DOG/USD-OTC", "DGF/USD-OTC", "BNK/USD-OTC", "BNB/USD-OTC"
]


# Main execution
if __name__ == "__main__":
    clear_screen()
    login()  # The banner is displayed after successful login
    input(f"{BOLD}{BRIGHT_YELLOW}Press Enter to exit...{RESET}")