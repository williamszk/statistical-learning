
# The objective of this project is to build the fibonacci algorithm
# in different programming languages with different methods
# then we compare the speed in which they perform

# variations of the fibonacci algorithm
# [ ] simple loops
# [ ] simple recursion
# [ ] loops with memoization
# [ ] recursion with memoization

# programming languages
# [ ] Rust
# [ ] Go
# [ ] C++
# [ ] C
# [ ] Python
# [ ] Java
# [ ] TypeScript

# which tools can I use to measure the performance of code?
# https://askubuntu.com/a/53445/1020380
# real: Elapsed real (wall clock) time used by the process, in seconds.
# user: Total number of CPU-seconds that the process used directly (in user mode), in seconds.
# sys: Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in seconds.
# time ls

mkdir cpp
touch cpp/notes.sh
mkdir c
touch c/notes.sh
mkdir go
touch go/notes.sh
mkdir python
touch python/notes.sh
mkdir python
touch python/notes.sh
mkdir java
touch java/notes.sh
mkdir typescript
touch typescript/notes.sh


# ------------------------------------------------------------------------------
# One of the problems of using memoization is that the tool that measures performance will
# capture the time for just 1 run.
# How can we measure the performance for fibonacci with and without memoization?
# We can create a list of values and run them repeteadly to see if the memoization works


# ------------------------------------------------------------------------------
# hyperfine: Hyperfine is a third-party tool designed to benchmark shell commands. 
# It measures the execution time of a command and provides statistical information. 
# Hyperfine runs the command multiple times and gives an average, median, and 
# deviation of the results. It can be installed using package managers like 
# Homebrew (for macOS) or directly from source. Here's an example usage:
hyperfine your_command

apt-get install hyperfine

# ------------------------------------------------------------------------------
# we can try to measure the performance of runs by using internal ways to measure
# the speed of execution of the code
# like using perf_counter inside Python
