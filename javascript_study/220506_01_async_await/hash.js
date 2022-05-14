// https://www.youtube.com/watch?v=NuyzuNBFWxQ&ab_channel=Fireship

// crypto is a builtin module to nodejs
const { createHash } = require("crypto");

function hash(input) {
    // returns a hash string as output
    return createHash("sha256").update(input).digest("hex"); // another options would be base64
    // sha256, secure hashing algorithm 256
    // sha256 returns a 456 bit key, this is a hash value
    // also called a digest.
    // md5 is very weak compared to sha256
    // md5 is deprecated by NIST
    // NIST: National Institute of Standards and Technology
    // Argon2 is a stronger option for hashing
}

const password = "hi mon!";

const hash1 = hash(password);

console.log(hash1);

const password2 = "hi mom";

const hash2 = hash(password2);

const match = hash1 === hash2;

console.log(match ? "✅ good password" : "❌ password does not match");
