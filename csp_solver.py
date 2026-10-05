locations = [
    "Library",
    "Computer Lab",
    "Cafeteria",
    "Auditorium"
]

suspects = [
    "Shreemayee",
    "Pritheeka",
    "Shabnam",
    "Saloni"
]


def check_constraints(assignment):

    # Clue 1: Shreemayee was in the Computer Lab
    if assignment["Shreemayee"] != "Computer Lab":
        return False

    # Clue 2: Pritheeka was not in the Cafeteria
    if assignment["Pritheeka"] == "Cafeteria":
        return False

    # Clue 3: Shabnam was not in the Library
    if assignment["Shabnam"] == "Library":
        return False

    # Clue 4: Saloni was not in the Auditorium
    if assignment["Saloni"] == "Auditorium":
        return False

    # Each person must have a different location
    if len(set(assignment.values())) != 4:
        return False

    return True


def solve_csp():

    solution = {}

    for shreemayee in locations:
        solution["Shreemayee"] =shreemayee

        for pritheeka in locations:
            solution["Pritheeka"] = pritheeka

            for shabnam in locations:
                solution["Shabnam"] = shabnam

                for saloni in locations:
                    solution["Saloni"] = saloni

                    if check_constraints(solution):
                        return solution.copy()

    return None