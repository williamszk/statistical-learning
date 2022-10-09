const express = require("express");
const redis = require("redis");
const process = require("process");

const app = express();
const client = redis.createClient({
	host: "redis-server",
	// we can include just the name of the container
	// usually we would include an URL like:
	// https://my-redis-server
	port: 6379
});

client.set("visits", 0);

app.get("/", (req, res) => {
	// this is called exit status code
	// 0 means that we exit because every is ok, and is intentional
	// other values -1, 1, 2, 3 etc means that something went wrong
	process.exit(0);
	client.get("visits", (err, visits) => {
		res.send("Number of visits is " + visits);
		client.set("visits", parseInt(visits) + 1);
	});
});

app.listen(8081, () => {
	console.log("Listenig on port 8081");
});
