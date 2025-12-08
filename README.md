AoC [readme](https://adventofcode.com/2025/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4460 so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

|task|interpreter|run 1|run 2|run 3|run 4|run 5|avg[^avg]|
|----|-----------|-----|-----|-----|-----|-----|---------|
| [./01/solve_a.py](./01/solve_a.py) | python3 | 16 ms | 16 ms | 16 ms | 16 ms | 16 ms | **16 ms** |
| [./01/solve_a_golfed.py](./01/solve_a_golfed.py) | python3 | 16 ms | 16 ms | 16 ms | 15 ms | 18 ms | **16 ms** |
| [./01/solve_b.py](./01/solve_b.py) | python3 | 17 ms | 17 ms | 20 ms | 20 ms | 20 ms | **19 ms** |
| [./02/solve_a.py](./02/solve_a.py) | pypy3 | 102 ms | 100 ms | 115 ms | 106 ms | 99 ms | **102 ms** |
| [./02/solve_b.py](./02/solve_b.py) | pypy3 | 441 ms | 441 ms | 445 ms | 452 ms | 450 ms | **445 ms** |
| [./03/solve_a.py](./03/solve_a.py) | python3 | 61 ms | 62 ms | 58 ms | 58 ms | 56 ms | **59 ms** |
| [./03/solve_b.py](./03/solve_b.py) | python3 | 26 ms | 31 ms | 30 ms | 27 ms | 27 ms | **28 ms** |
| [./04/solve_a.py](./04/solve_a.py) | python3 | 44 ms | 46 ms | 56 ms | 47 ms | 44 ms | **45 ms** |
| [./04/solve_b.py](./04/solve_b.py) | pypy3 | 118 ms | 119 ms | 119 ms | 119 ms | 119 ms | **119 ms** |
| [./05/solve_a.py](./05/solve_a.py) | python3 | 27 ms | 26 ms | 26 ms | 24 ms | 31 ms | **26 ms** |
| [./05/solve_b.py](./05/solve_b.py) | python3 | 15 ms | 15 ms | 15 ms | 15 ms | 15 ms | **15 ms** |
| [./06/solve_a.py](./06/solve_a.py) | python3 | 19 ms | 20 ms | 20 ms | 26 ms | 28 ms | **22 ms** |
| [./06/solve_b.py](./06/solve_b.py) | python3 | 21 ms | 21 ms | 21 ms | 21 ms | 21 ms | **21 ms** |
| [./07/solve_a.py](./07/solve_a.py) | python3 | 21 ms | 20 ms | 21 ms | 20 ms | 18 ms | **20 ms** |
| [./07/solve_b.py](./07/solve_b.py) | python3 | 20 ms | 20 ms | 19 ms | 20 ms | 26 ms | **20 ms** |
| [./08/solve_a.py](./08/solve_a.py) | pypy3 | 341 ms | 339 ms | 364 ms | 361 ms | 362 ms | **354 ms** |
| [./08/solve_b.py](./08/solve_b.py) | pypy3 | 324 ms | 339 ms | 342 ms | 344 ms | 336 ms | **339 ms** |
| [./_meta/pypy_startup.py](./_meta/pypy_startup.py) | pypy3 | 43 ms | 46 ms | 57 ms | 47 ms | 47 ms | **46 ms** |
| [./_meta/python_startup.py](./_meta/python_startup.py) | python3 | 20 ms | 23 ms | 25 ms | 22 ms | 22 ms | **22 ms** |

[^avg]: The slowest and the fastest runs are discarded from the average
