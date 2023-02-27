var httpclient = {
    getuser: function (email) {
        console.log("Getting user... ".concat(email));
    },
    createuser: function (user) {
        console.log("Creating user... ".concat(user.name));
    }
};
function app(clientapi) {
    clientapi.getuser("bob@clean.com");
    var user = {
        name: "Bob",
        email: "bob@clean.com"
    };
    clientapi.createuser(user);
}
app(httpclient);
