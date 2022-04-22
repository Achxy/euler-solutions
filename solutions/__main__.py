# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

import importlib
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

_PARENT = Path(__file__).resolve().parent
_ROOT = _PARENT.parent

if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


def _discover():
    return sorted(
        int(p.stem.split("_")[1])
        for p in _PARENT.glob("problem_*.py")
    )


def _solve_one(n):
    module = importlib.import_module(f".problem_{n}", package="solutions")
    start = time.perf_counter()
    result = module.solve()
    elapsed = (time.perf_counter() - start) * 1000
    return n, result, elapsed


def run(numbers=None):
    if numbers is None:
        numbers = _discover()

    pending = {}
    results = {}
    cpu_total = 0
    wall_start = time.perf_counter()

    with ThreadPoolExecutor() as pool:
        for n in numbers:
            pending[n] = pool.submit(_solve_one, n)

        print_idx = 0
        for future in as_completed(pending.values()):
            n, result, elapsed = future.result()
            results[n] = (result, elapsed)
            cpu_total += elapsed

            while print_idx < len(numbers) and numbers[print_idx] in results:
                pn = numbers[print_idx]
                r, e = results.pop(pn)
                print(f"Problem {pn:>3}: {str(r):<30s} ({e:.2f}ms)")
                print_idx += 1

    wall = (time.perf_counter() - wall_start) * 1000
    if len(numbers) > 1:
        print(f"\nSolved {len(numbers)} problems in {wall:.2f}ms (cpu: {cpu_total:.2f}ms)")


if __name__ == "__main__":
    args = sys.argv[1:]
    run([int(a) for a in args] if args else None)
