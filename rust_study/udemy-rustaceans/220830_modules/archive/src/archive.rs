pub mod arch {
    pub fn archive_file(name: &str) {
        println!("Archive file: {}", name);
    }

    pub fn archive_file_with_a_long_name(name: &str){
        println!("Archiving a file with a function with a long name: {}", name);
    }
}
