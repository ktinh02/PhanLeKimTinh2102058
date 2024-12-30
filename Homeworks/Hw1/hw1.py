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

    return event/trials

try:
    event_count = int(input("Enter number of event: "))
    total_trials = int(input("Enter total number of trials: "))

    probability = calculate_probability(event_count, total_trials)
    print(f"The probability of the event is: {probability:.2f}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")