AoC [readme](https://adventofcode.com/2024/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4460 so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

|task|interpreter|run 1|run 2|run 3|run 4|run 5|avg|
|----|-----------|-----|-----|-----|-----|-----|---|
| [./_meta/pypy_startup.py](./_meta/pypy_startup.py) | pypy3 | 94 ms | 46 ms | 46 ms | 46 ms | 55 ms | **57 ms** |
| [./_meta/python_startup.py](./_meta/python_startup.py) | python3 | 21 ms | 28 ms | 26 ms | 25 ms | 23 ms | **24 ms** |
