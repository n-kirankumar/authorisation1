from log import logger

# Example users data (for demonstration purposes, actual authentication should use secure methods)
users = [
    {'username': 'admin', 'password': 'admin123', 'role': 'admin'},
    {'username': 'user1', 'password': 'user123', 'role': 'normal'},
    {'username': 'user2', 'password': 'user456', 'role': 'normal'}
]

current_user = None  # Global variable to store the current authenticated user

def authenticate(username, password):
    """
    Authenticate a user based on username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    global current_user
    for user in users:
        if user['username'] == username and user['password'] == password:
            current_user = user
            logger.info(f"User '{username}' logged in")
            return True
    logger.error("Authentication failed")
    return False

def is_admin():
    """
    Check if the current authenticated user is an admin.

    Returns:
        bool: True if the current user is admin, False otherwise.
    """
    global current_user
    return current_user and current_user['role'] == 'admin'

def is_authenticated():
    """
    Check if any user is currently authenticated.

    Returns:
        bool: True if there is an authenticated user, False otherwise.
    """
    global current_user
    return current_user is not None
