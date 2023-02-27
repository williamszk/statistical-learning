var HttpClient = {
    getuser: function (email) {
        console.log("Getting user... ".concat(email));
    },
    createuser: function (user) {
        console.log("Creating user... ".concat(user.name));
    }
};
function app() {
    HttpClient.getuser("bob@clean.com");
    var user = {
        name: "Bob",
        email: "bob@clean.com"
    };
    HttpClient.createuser(user);
}
app();
