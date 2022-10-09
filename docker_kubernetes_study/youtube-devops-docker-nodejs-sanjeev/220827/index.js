const express = require("express");

const app = express();

app.get("/", (req, res) => {
	res.send("<h2>Hi there!</h2>");
});

// if the environment variable PORT was not being set, then we call 3000
const port = process.env.PORT || 3000;

app.listen(port, () => {
	console.log(`Listening on port ${port}`);
});
