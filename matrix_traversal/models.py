from django.db import models


class MatrixField(models.Field):
    """
    Custom Django model field for storing matrix data.

    This field stores matrix data as a string in a specific format.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the MatrixField.
        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        kwargs['editable'] = False  # Matrix field is not editable through the admin interface
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        """
        Convert the value from the database to a Python object.
        Args:
            value: The value retrieved from the database.
            expression: Unused in this method.
            connection: Unused in this method.
        Returns:
            The Python representation of the value.
        """
        if value is None:
            return value
        return value

    def to_python(self, value):
        """
        Convert the value stored in the database to a Python object.
        Args:
            value: The value retrieved from the database.
        Returns:
            The Python representation of the value.
        Raises:
            ValueError: If the matrix format is invalid.
        """
        if isinstance(value, str):
            if not value.startswith("+-----+") or not value.endswith("+-----+"):
                raise ValueError("Invalid matrix format")
            return value
        return super().to_python(value)

    def get_prep_value(self, value):
        """
        Prepare the value for saving into the database.
        Args:
            value: The value to be saved.
        Returns:
            The prepared value.
        """
        return value

    def get_internal_type(self):
        return 'TextField'


class Matrix(models.Model):
    matrix = MatrixField()
