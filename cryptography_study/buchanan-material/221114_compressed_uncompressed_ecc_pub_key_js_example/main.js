const EthCrypto = require("eth-crypto");
const crypto = require("crypto");
const { log } = require("console");

const privateKey = crypto.randomBytes(32).toString("hex");
const publicKey = EthCrypto.publicKeyByPrivateKey(privateKey);
const address = EthCrypto.publicKey.toAddress(publicKey);

const publicKeyCompressed = EthCrypto.publicKey.compress(publicKey);

log(`address: ${address}`);
log(`publicKey: ${publicKey}`);
log(`publicKeyCompressed: ${publicKeyCompressed}`);
