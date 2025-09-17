def calculate_average(*args):
    """
    Calculates the average of a variable number of numerical arguments
    Args: *args: A variable of numerical argument (integers or floats)
    Returns:
        float : The average of the provided numbers.Return 0 if no arguments are provided.
        """
    if not args:
        return 0
    total_sum = sum(args)
    count = len(args)
    return total_sum /count