"""Exact audits of the flow-defect identity and movement-episode reduction.

Only the Python standard library is used. The original four traffic steps
are implemented directly; no old solver or projection code is imported.
The polynomial check proves the tested local identities for every epsilon,
not merely for selected floating-point parameters.
"""

from itertools import product
from pathlib import Path
import json


def move(g, v, coin):
    accelerated = min(v + 1, 2)
    collision_free = min(accelerated, g)
    return max(collision_free - (1 - coin), 0)


def step(g, v, coins):
    n = len(g)
    w = tuple(move(g[i], v[i], coins[i]) for i in range(n))
    gg = tuple(g[i] + w[(i + 1) % n] - w[i] for i in range(n))
    assert min(gg) >= 0 and sum(gg) == sum(g)
    return gg, w


def compositions(h, n):
    if n == 1:
        yield (h,)
    else:
        for j in range(h + 1):
            for z in compositions(h - j, n - 1):
                yield (j,) + z


def audit_local_polynomials(count):
    # The weights are the coefficients of epsilon^0, epsilon^1, epsilon^2.
    weights = {(0, 0): (1, -2, 1), (0, 1): (0, 1, -1),
               (1, 0): (0, 1, -1), (1, 1): (0, 0, 1)}
    for g, h, v, leader_v in product(range(17), range(17), range(3), range(3)):
        c = int(v > 0 and g >= 2)
        z = int(leader_v > 0 and h >= 2)
        leader_o = int(h >= 1)
        potential = c * (g - 1)
        drift = [0, 0, 0]
        for x, y in product((0, 1), repeat=2):
            w, incoming = move(g, v, x), move(h, leader_v, y)
            after_g = g + incoming - w
            after_potential = int(w > 0 and after_g >= 2) * (after_g - 1)
            assert w == c + x * int(g >= 1)
            for k in range(3):
                drift[k] += (after_potential - potential) * weights[x, y][k]
            count['direct_local_masks'] += 1

        t, u, s = int(c and g == 2), int(v == 0 and g >= 2), int(g == 1)
        r0 = t * (1 - z) + c * leader_o + u * z
        r1 = t * (z - leader_o) + s * z + u * leader_o
        expected = [-c * (1 - z), max(g - 2, 0) - potential + r0, r1]
        assert drift == expected, (g, h, v, leader_v, drift, expected)
        count['all_epsilon_drift_polynomials'] += 1
        # The remainder and its pointwise upper bound are affine in epsilon.
        # Nonnegative endpoint values certify the whole interval [0,1].
        for e in (0, 1):
            remainder = r0 + e * r1
            bound = c + c * (1 - z) + (1 - c) * z + e
            assert 0 <= remainder <= bound
            count['remainder_endpoint_certificates'] += 1

    for g, v in product(range(201), range(3)):
        a, o, q = int(v > 0), int(g >= 1), int(g >= 2)
        c, d = a * q, g - q
        assert max(g - 2, 0) == g - o - q
        assert a * d == c * (g - 1) + int(a and g == 1)
        assert (1 - c) * g == g - c * (g - 1) - c
        count['reward_mass_identities'] += 1


def one_episode(g, v, first, second):
    assert v[0] == 0 and g[0] >= 1 and first[0] == 1
    initial_gap = g[0]
    reward = incoming = length = 0
    horizon = sum(g) + 4
    for k in range(horizon):
        coins = first if k == 0 else second if k == 1 else (0,) * len(g)
        gg, w = step(g, v, coins)
        if w[0] == 0:
            assert length >= 1 and v[0] > 0 and g[0] <= 1
            assert reward == initial_gap + incoming - g[0]
            assert reward >= initial_gap - int(initial_gap >= 2)
            return reward
        reward += w[0]
        incoming += w[1]
        length += 1
        g, v = gg, w
    raise AssertionError('All-braking suffix did not end the episode')


def audit_episodes(count):
    for n in range(2, 5):
        masks = list(product((0, 1), repeat=n))
        for h in range(1, min(2 * n, 5)):
            for g in compositions(h, n):
                if g[0] == 0:
                    continue
                for other_v in product((0, 1), repeat=n - 1):
                    v = (0,) + other_v
                    for rest_first in product((0, 1), repeat=n - 1):
                        first = (1,) + rest_first
                        for second in masks:
                            reward = one_episode(g, v, first, second)
                            count['episode_conservation_and_gain'] += 1
                            if (not (v[1] > 0 and g[1] >= 2)
                                    and first[1] == second[0] == second[1] == 0):
                                assert reward == g[0] - int(g[0] >= 2)
                                count['isolated_episode_reductions'] += 1


def audit_time_charging(count):
    # Purely combinatorial audit of the time-mass-transport step. These
    # words are not asserted to be stationary NaSch trajectories.
    for n in range(2, 10):
        for word in product((0, 1, 2), repeat=n):
            if 0 not in word:
                continue
            total = 0
            for i in range(n):
                if word[i] > 0 and word[(i - 1) % n] == 0:
                    reward, j = 0, i
                    while word[j % n] > 0:
                        reward += word[j % n]
                        j += 1
                    total += reward
            assert total == sum(word)
            count['cyclic_time_reward_words'] += 1


def audit_pair_extinction(count):
    # Freeze only the first initially unqualified leader. Explore EVERY
    # reachable path that has not yet lost the qualified pair, allowing
    # arbitrary coins at all other sites. No surviving path may remain
    # after a number of steps equal to the initial run's vacancy mass.
    for n in range(3, 6):
        for h in range(4, min(2 * n, 7)):
            for g in compositions(h, n):
                for v in product((0, 1), repeat=n):
                    c = tuple(int(v[i] and g[i] >= 2) for i in range(n))
                    if not (c[0] and c[1]):
                        continue
                    mass, j = 0, 1
                    while c[j % n]:
                        mass += g[j % n]
                        j += 1
                    anchor = j % n
                    masks = [z for z in product((0, 1), repeat=n) if z[anchor] == 0]
                    states = {(g, v)}
                    for time in range(mass):
                        next_states = set()
                        for gg, vv in states:
                            for coins in masks:
                                gnew, vnew = step(gg, vv, coins)
                                assert vnew[anchor] == 0
                                count['frozen_boundary_transitions'] += 1
                                if all(vnew[i] > 0 and gnew[i] >= 2 for i in (0, 1)):
                                    # Velocities 1 and 2 have the same next acceleration.
                                    next_states.add((gnew, tuple(int(x > 0) for x in vnew)))
                        states = next_states
                    assert not states
                    count['frozen_boundary_pair_extinctions'] += 1


def main():
    count = dict.fromkeys(('direct_local_masks', 'all_epsilon_drift_polynomials',
                          'remainder_endpoint_certificates', 'reward_mass_identities',
                          'episode_conservation_and_gain', 'isolated_episode_reductions',
                          'cyclic_time_reward_words', 'frozen_boundary_transitions',
                          'frozen_boundary_pair_extinctions'), 0)
    audit_local_polynomials(count)
    audit_episodes(count)
    audit_time_charging(count)
    audit_pair_extinction(count)
    out = {'status': 'all_passed_exactly', 'counts': count,
           'scope': 'Exact local drift, episode and reward-accounting identities. '
                    'No stationary solver, no proof of defect vanishing, and no general flow closure.'}
    path = Path(__file__).parent / 'results' / 'verified.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
