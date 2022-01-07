// create an object factory for "house keeper"
// this is like creating a class in Python or maybe a dictionary itself

// this is called a constructor function
function HouseKeper(name, yearsOfExperience, cleaningRepertoire){
    this.name = name;
    this.yearsOfExperience = yearsOfExperience;
    this.cleaningRepertoire = cleaningRepertoire;
    this.clean = function() {
        console.log("Cleaning in progress...")
    }
}

var houseKeeper01 = new HouseKeper("Mary Jane", 10, ["bathroom", "field"])

houseKeeper01
typeof(houseKeeper01)

// node
