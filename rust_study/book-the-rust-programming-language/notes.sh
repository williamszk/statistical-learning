# some notes based on the book: The Rust Programming Language
# Klabnik

# Writting this on Windows

cargo new project-01
cd project-01

rustc src/main.rs
.\main.exe

cargo --version
# cargo 1.63.0 (fd9c4297c 2022-07-01)

cargo build 

# cargo run will compile and then run the code
cargo run

# this command will check if the program compiles but does not produce an executable
cargo check 
# cargo check is faster than cargo build,


# this will build with optimizations
cargo build --release
# this takes longer to compile, but runs faster
# the executable is in target/release
# instead of target/debug



# =================
cargo new guessing_game
cd guessing_game
cargo run









