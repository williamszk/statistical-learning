const HttpClient = {
	getuser: (email: string) => {
		console.log(`Getting user... ${email}`);
	},
	createuser: (user: User) => {
		console.log(`Creating user... ${user.name}`);
	},
};

function app() {
	HttpClient.getuser("bob@clean.com");
	const user: User = {
		name: "Bob",
		email: "bob@clean.com",
	};
	HttpClient.createuser(user);
}

interface User {
	name: string;
	email: string;
}

app();
