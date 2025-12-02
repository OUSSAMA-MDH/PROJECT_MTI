USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "teacher1": {"password": "teach123", "role": "teacher"}
}

def login(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        print(f"Connexion réussie en tant que {user['role']}")
        return user["role"]
    print("Nom d'utilisateur ou mot de passe incorrect")
    return None
