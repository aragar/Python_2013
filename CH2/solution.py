DIRECTIONS_AFTER_ROTATION = {
    'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}


def dragon_fractal():
    directions = []
    current_directions = ['up']

    while True:
        for direction in current_directions:
            yield direction

        directions += current_directions
        current_directions = [DIRECTIONS_AFTER_ROTATION[
            direction] for direction in reversed(directions)]
