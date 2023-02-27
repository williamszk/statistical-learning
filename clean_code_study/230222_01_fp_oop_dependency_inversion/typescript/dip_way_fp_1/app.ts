interface User {
	name: string;
	email: string;
}

const getuser = (email: string) => {
	console.log(`Getting user... ${email}`);
};

const createuser = (user: User) => {
	console.log(`Creating user... ${user.name}`);
};

function app(
	getuser: (email: string) => void,
	createuser: (user: User) => void
) {
	getuser("bob@clean.com");
	const user: User = {
		name: "Bob",
		email: "bob@clean.com",
	};
	createuser(user);
}

app(getuser, createuser);
