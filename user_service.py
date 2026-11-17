
def get_user(user_id):
    """
    Retrieve basic user information.
    """
    users = {
        1: {
            "user_id": 1,
            "name": "John",
            "email": "john@example.com"
        },
        2: {
            "user_id": 2,
            "name": "David",
            "email": "david@example.com"
        }
    }

    return users.get(user_id)


def get_user_status(user_id):
    """
    Return the current status of a user.
    """
    user = get_user(user_id)

    if user is None:
        return None

    return {
        "user_id": user_id,
        "status": "active"
    }


def format_user(user):
    """
    Format user information.
    """
    if user is None:
        return "User not found"

    return f"{user['name']} ({user['email']})"


def validate_user(user_id):
    """
    Check whether a user exists.
    """
    return get_user(user_id) is not None
