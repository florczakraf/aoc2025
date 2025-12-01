AoC [readme](https://adventofcode.com/2025/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4460 so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

|task|interpreter|run 1|run 2|run 3|run 4|run 5|avg[^avg]|
|----|-----------|-----|-----|-----|-----|-----|---------|
| [./01/solve_a.py](./01/solve_a.py) | python3 | 16 ms | 16 ms | 16 ms | 16 ms | 16 ms | **16 ms** |
| [./01/solve_a_golfed.py](./01/solve_a_golfed.py) | python3 | 16 ms | 16 ms | 18 ms | 19 ms | 18 ms | **17 ms** |
| [./01/solve_b.py](./01/solve_b.py) | python3 | 17 ms | 17 ms | 20 ms | 20 ms | 20 ms | **19 ms** |
| [./_meta/pypy_startup.py](./_meta/pypy_startup.py) | pypy3 | 43 ms | 46 ms | 57 ms | 47 ms | 47 ms | **46 ms** |
| [./_meta/python_startup.py](./_meta/python_startup.py) | python3 | 20 ms | 23 ms | 25 ms | 22 ms | 22 ms | **22 ms** |

[^avg]: The slowest and the fastest runs are discarded from the average
