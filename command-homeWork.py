RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

while True:
 print(f"""{RED}The available operations are:
 1 - Palindrome:{RESET} {GREEN}Check if the input is palindrome{RESET}
 {RED}2 - Lower:{RESET}{GREEN} Check if all characters in input are lowerscase{RESET}
 {RED}3 - Digit:{RESET} {GREEN}Check if all characters in input are digits{RESET}
 {RED}4 - Long:{RESET} {GREEN}Check if the input length is longer than {RED}15{RESET}{RESET}
 {RED}5 - Empty:{RESET} {GREEN}Check if the input is empty{RESET}
 {RED}6 - Exit:{RESET} {GREEN}Exit successfully from the application{RESET}""")

 operation_number= input(f"\n{RED}Please enter the number of the operation you choose: ")

 if operation_number not in ["1", "2", "3", "4", "5", "6"]:
    print(f"{YELLOW}Invalid choice. Please enter a valid number.{RESET}\n")
    continue
 
 user_input= input(f"{RED}Enter an input: ")


 if any(c.isalpha() for c in user_input) and any(c.isdigit() for c in user_input):
    print(f"{YELLOW}Error: Mixed input (letters + digits) is not allowed.{RESET}\n")
    continue

 if operation_number=="6":
    print(f"{GREEN}Exit successfully{RESET}")
    break
 elif operation_number=="1":
    print(f"{RED}The answer is:{RESET} {BLUE}{user_input==user_input[::-1]}{RESET}\n")
 elif operation_number=="2":
    print(f"{RED}The answer is:{RESET}{BLUE} {user_input.islower()}{RESET}\n")
 elif operation_number=="3":
    print(f"{RED}The answer is:{RESET} {BLUE}{user_input.isdigit()}{RESET}\n")
 elif operation_number=="4":
    print(f"{RED}The answer is:{RESET} {BLUE}{len(user_input)>15}{RESET}\n")
 elif operation_number=="5":
    print(f"{RED}The answer is:{RESET} {BLUE}{user_input== '' }{RESET}\n")
