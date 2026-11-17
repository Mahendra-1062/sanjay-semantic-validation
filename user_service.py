class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


def get_user(user_id):
    return User(user_id, "John", "john@example.com")


def get_user_email(user_id):
    user = get_user(user_id)
    if not user:
        return None
    return user.email


def get_user_details(user_id):
    user = get_user(user_id)
    if not user:
        return None

    return {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email
    }