from Utils import EvenStream


# Task 11
def calculate_cost(duration_in_seconds):
    minute_rate = 1.45
    cost = duration_in_seconds * (minute_rate / 60)
    return cost


# Task 12
def print_from_stream(n, stream=EvenStream()):
    if stream is None:
        stream = EvenStream()
    output = []
    for _ in range(n):
        output.append(stream.get_next())
    return output
