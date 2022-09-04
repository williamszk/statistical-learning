// this is how we import modules
mod players;

fn main() {
    println!("Hello, world!");

    // we use :: to use a function from another module
    players::play_movie("Pirate of the Caribbean");

    players::play_audio("Twenty one pilots");

    clean::perform_clean();

    // here we are accessing the submodule's function
    clean::files::clean_files();
}

// we could define a module inside a same file
pub mod clean {
    pub fn perform_clean() {
        println!("Cleaning hdd");
    }
    // we could nest modules inside of each other

    pub mod files {

        pub fn clean_files() {
            println!("Removing unused files");
        }
    }
}
