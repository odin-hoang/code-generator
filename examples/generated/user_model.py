class UserModel:
    """
    A model class representing a user in the system.
    """

    @property
    def full_name(self):
            """
        Get the user's full name.
        """
        return f"{self._first_name} {self._last_name}"

    def __init__(self, first_name, last_name, email):
            """
        Initialize a new user instance.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def update_email(self, new_email):
            """
        Update the user's email address.
        """
        self._email = new_email
        return True