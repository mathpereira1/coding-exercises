def getPasswordStrength(passwords, common_words):
    passwordsStrenghts = []

    for password in passwords:
        checked = 0
        if len(password) < 6:
            passwordsStrenghts.append("weak")
            checked = 1
            continue
        if checked == 0;
            for common_word in common_words:
                if common_word in password and checked == 0:
                    passwordsStrenghts.append("weak")
                    checked = 1
                    continue
            
            if not password.isdigit():
                if not any(char.isupper() for char in password) and checked = 0:
                    passwordsStrenghts.append("weak")
                    checked = 1
                    continue
                
                if not any(char.islower() for char in password) and checked == 0:
                    passwordsStrenghts.append("weak")
                    checked = 1
                    continue
            else:
                passwordsStrenghts.append("weak")
                checked=1
        
        if checked == 0:
            passwordsStrenghts.append("strong")
    return passwordsStrenghts