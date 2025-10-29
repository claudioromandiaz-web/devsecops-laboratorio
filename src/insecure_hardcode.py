# insecure_hardcode.py  -- forzar SAST: credenciales hardcoded
password = "P@ssw0rd12345"   # SonarCloud suele detectar credenciales hard-coded
def login(user, pwd):
    if user == "admin" and pwd == password:
        return True
    return False

if __name__ == "__main__":
    print(login("admin", "P@ssw0rd12345"))
