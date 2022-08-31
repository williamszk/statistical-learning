// There are two types of crates
// the binary crate: which is a crate that has an entry point, main function
// the library crate which doesn't have the main entry point
// use crate::archive::arch::arch_files;
//  use crate::file::module::function

// we can also use an alias
use crate::archive::arch::arch_files as arc;



mod archive;


fn main() {
    // arch_files("somefile.log");
    arc("somefile.log");

}











