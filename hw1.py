def calculate_probability(event: int, trials: int) -> float:
    """
    Calculate the probability of an event occurring.

    Args:
        event (int): the number of times the event occurs.
        trials (int): the total number of trials.

    Returns:
        float: the probability of the event (value between 0 and 1).
    """
    if trials <= 0:
        raise ValueError("The total number of trials must be greater than 0.")
    if event < 0 or event > trials:
        raise ValueError("The number of event occurrences must be between 0 and the total number of trials.")

    probability = event / trials
    return probability


event_count = 15  # Number of event occurrences
total_count = 50  # Total number of trials
result = calculate_probability(event_count, total_count)
print(f"The probability of the event is: {result:.2f}")

