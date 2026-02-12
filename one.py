def get_candidate_paradox(
    candidate, candidate_scores): return candidate_scores.get(candidate)


def get_candidates(inhabitants_list):
    candidates_paradox = {}
    candidate_names = []

    for rep in inhabitants_list:
        parts = rep.rsplit(":", 1)
        if len(parts) == 2:
            candidate = parts[0]
            paradox = int(parts[1])
            candidates_paradox.update({candidate: paradox})
            candidate_names.append(candidate)

    return candidates_paradox, candidate_names


def get_local_maxima(candidates_paradox, candidates_names):
    candidate_count = 0
    prev_candidate_paradox = 0
    selected_candidates = {}
    selected_candidates_names = []

    for candidate, paradox in candidates_paradox.items():
        current = paradox

        if candidate_count == 0:
            next_val = get_candidate_paradox(
                candidates_names[candidate_count + 1], candidates_paradox
            )
            if current > next_val:
                selected_candidates[candidate] = current
                selected_candidates_names.append(candidate)

        elif candidate_count == (len(candidates_paradox) - 1):
            if current > prev_candidate_paradox:
                selected_candidates[candidate] = current
                selected_candidates_names.append(candidate)

        else:
            next_val = get_candidate_paradox(
                candidates_names[candidate_count + 1], candidates_paradox
            )
            if current > prev_candidate_paradox and current > next_val:
                selected_candidates[candidate] = current
                selected_candidates_names.append(candidate)

        prev_candidate_paradox = current
        candidate_count += 1

    return selected_candidates, selected_candidates_names


def get_local_minima(candidates_paradox, candidates_names):
    candidate_count = 0
    prev_candidate_paradox = 0
    selected_candidates = {}
    selected_candidates_names = []

    for candidate, paradox in candidates_paradox.items():
        current = paradox

        if candidate_count == 0:
            next_val = get_candidate_paradox(
                candidates_names[candidate_count + 1], candidates_paradox
            )
            if current < next_val:
                selected_candidates[candidate] = current
                selected_candidates_names.append(candidate)

        elif candidate_count == (len(candidates_paradox) - 1):
            if current < prev_candidate_paradox:
                selected_candidates[candidate] = current
                selected_candidates_names.append(candidate)

        else:
            next_val = get_candidate_paradox(
                candidates_names[candidate_count + 1], candidates_paradox
            )
            if current < prev_candidate_paradox and current < next_val:
                selected_candidates[candidate] = current
                selected_candidates_names.append(candidate)

        prev_candidate_paradox = current
        candidate_count += 1

    return selected_candidates, selected_candidates_names


def elect(population: str) -> str:
    inhabitants_list = population.split()
    candidates_paradox, candidates_names = get_candidates(inhabitants_list)

    if len(candidates_paradox) == 1:
        chosen_monarch = (
            f"Inhabitant {candidates_names[0]} "
            f"(id: {candidates_paradox.get(candidates_names[0])}) "
            "is the new Monarch"
        )
    else:
        while True:
            elected_by_round, candidates = get_local_minima(
                candidates_paradox, candidates_names
            )
            if len(elected_by_round) == 1:
                break

            candidates_names = candidates
            candidates_paradox = elected_by_round

            elected_by_round, candidates = get_local_maxima(
                candidates_paradox, candidates_names
            )
            if len(elected_by_round) == 1:
                break

            candidates_names = candidates
            candidates_paradox = elected_by_round

        chosen_monarch = (
            f"Inhabitant {candidates[0]} "
            f"(id: {elected_by_round.get(candidates[0])}) "
            "is the new Monarch"
        )

    return chosen_monarch
