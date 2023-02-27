var getuser = function (email) {
    console.log("Getting user... ".concat(email));
};
var createuser = function (user) {
    console.log("Creating user... ".concat(user.name));
};
function app(getuser, createuser) {
    getuser("bob@clean.com");
    var user = {
        name: "Bob",
        email: "bob@clean.com"
    };
    createuser(user);
}
app(getuser, createuser);
