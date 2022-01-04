// create an object factory for "house keeper"
// this is like creating a class in Python or maybe a dictionary itself

function HouseKeper(name, yearsOfExperience, cleaningRepertoire){
    this.name = name;
    this.yearsOfExperience = yearsOfExperience;
    this.cleaningRepertoire = cleaningRepertoire;
}

var houseKeeper01 = new HouseKeper("Mary Jane", 10, ["bathroom", "field"])

houseKeeper01
typeof(houseKeeper01)

// node
