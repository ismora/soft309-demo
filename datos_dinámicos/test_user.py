from faker import Faker

fake = Faker()

def test_user_creation():
    username = "maria_89"                   # Ej: "maria_89"
    email = "maria@example.com"             # Ej: "maria@example.com"
    age = 25                                #Ej: 25

    # Simulación de creación de usuario
    user_data = {"username": username, "email": email, "age": age}
    print("Datos:", username, email, age)
    
    assert len(user_data["username"]) > 3
    assert "@" in user_data["email"]

    """
    Ejecución: pytest .\test_user.py -v -s
    """