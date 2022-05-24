
// https://www.udemy.com/course/rustaceans/learn/lecture/19478246?start=15#overview

mod player;

fn main() {

    player::play_movies("snatch.mp4");

    player::play_audio("linkin_park.mp4");

    clean::perform_clean();

    clean::files::clean_files();

}


mod clean {
    pub fn perform_clean() {
        println!("Cleaning hdd");
    }

    // without the pub the submodule would only available inside the module
    pub mod files {
        pub fn clean_files() {
            println!("Removing unused files");
        }
    }
}