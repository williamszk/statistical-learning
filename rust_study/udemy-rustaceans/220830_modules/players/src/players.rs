// this file is called a module
// in rust packages are called crates



// we need to use the pub keyword to make this function available to others to use
pub fn play_movie(name: &str) {
    println!("Playing movie {}", name);
}


pub fn play_audio(name: &str){
    println!("Playing audio {}", name);
}

