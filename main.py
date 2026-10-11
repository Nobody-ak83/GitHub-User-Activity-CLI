from config import getGitUserActivity

def main():
    user_input=input("Hello! Enter nickname of user you want to know about: \n").strip()
    
    if not user_input:
        user_input=input("We need the nickname: \n").strip()

    getGitUserActivity(user_input)
    




if __name__ == "__main__":
    main() 
    