#/usr/bin/python3
def is_instance_or_inherited(obj, target_class):
    """Checks if an object is an instance or inherited instance of a class

    Args:
        obj: The object to check.
        target_class: The class to match the type of obj to.
    Returns:
        True if obj is an instance or inherited instance of target_class, False otherwise.
    """
    return isinstance(obj, target_class)
