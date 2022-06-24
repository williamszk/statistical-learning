const { scryptSync, randomBytes } = require("crypto");

function signup(email, password) {
  const salt = randomBytes(16).toString("hex");
  const hashedPassword = scryptSync(password, salt, 64).toString("hex");

  const user = { email, password: `${salt}:${hashedPassword}` };
  // we store the salt with the hashed password
  // notice that we pass email, instead of giving the name of the key also
  // javascript already knows that this is the name of the key
}

function login(email, password) {}
