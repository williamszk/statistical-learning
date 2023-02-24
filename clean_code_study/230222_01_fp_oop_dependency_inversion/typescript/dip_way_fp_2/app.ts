interface User {
	name: string;
	email: string;
}

interface ClientInterface {
	getuser: (email: string) => void;
	createuser: (user: User) => void;
}

const httpclient: ClientInterface = {
	getuser: (email: string) => {
		console.log(`Getting user... ${email}`);
	},
	createuser: (user: User) => {
		console.log(`Creating user... ${user.name}`);
	},
};

function app(clientapi: ClientInterface) {
	clientapi.getuser("bob@clean.com");
	const user: User = {
		name: "Bob",
		email: "bob@clean.com",
	};
	clientapi.createuser(user);
}

app(httpclient);
