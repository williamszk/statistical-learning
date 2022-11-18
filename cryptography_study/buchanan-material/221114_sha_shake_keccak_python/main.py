# https://asecuritysite.com/hash/s3

import sys

from hashlib import sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256

message = "abc"
message_bytes = message.encode()

# Test vectors for "abc"
# SHA-3-224	e642824c3f8cf24a d09234ee7d3c766f c9a3a5168d0c94ad 73b46fdf
# SHA-3-256	3a985da74fe225b2 045c172d6bd390bd 855f086e3e9d525b 46bfe24511431532
# SHA-3-384	ec01498288516fc9 26459f58e2c6ad8d f9b473cb0fc08c25 96da7cf0e49be4b2 98d88cea927ac7f5 39f1edf228376d25
# SHA-3-512	b751850b1a57168a 5693cd924b6b096e 08f621827444f70d 884f5d0240d2712e 10e116e9192af3c9 1a7ec57647e39340 57340b4cf408d5a5 6592f8274eec53f0

# Test vectors for ""
# SHA-3-224	6b4e03423667dbb7 3b6e15454f0eb1ab d4597f9a1b078e3f 5b5a6bc7
# SHA-3-256	a7ffc6f8bf1ed766 51c14756a061d662 f580ff4de43b49fa 82d80a4b80f8434a
# SHA-3-384	0c63a75b845e4f7d 01107d852e4c2485 c51a50aaaa94fc61 995e71bbee983a2a c3713831264adb47 fb6bd1e058d5f004
# SHA-3-512	a69f73cca23a9ac5 c8b567dc185a756e 97c982164fe25859 e0d1dcc1475c80a6 15b2123af1f5f94c 11e3e9402c3ac558 f500199d95b6d3e3 01758586281dcd26

if len(sys.argv) > 1:
    message = sys.argv[1]

print(f"The message is: {message}")

print(f"\nFor Keccak 1600 digests\n")
sha_224 = sha3_224()
sha_224.update(message_bytes)
print(f"SHA-3 224 bits: {sha_224.hexdigest()}")
# observed: SHA-3 224 bits: e642824c3f8cf24ad09234ee7d3c766fc9a3a5168d0c94ad73b46fdf
# expected: SHA-3-224	    e642824c3f8cf24ad09234ee7d3c766fc9a3a5168d0c94ad73b46fdf

sha_256 = sha3_256()
sha_256.update(message_bytes)
sha_256.hexdigest()
print(f"SHA-3 256 bits: {sha_256.hexdigest()}")
# observed: SHA-3 256 bits: 3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532
# expected: SHA-3-256	    3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532

sha_384 = sha3_384()
sha_384.update(message_bytes)
print(f"SHA-3 384 bits: {sha_384.hexdigest()}")
# observed: SHA-3 384 bits: ec01498288516fc926459f58e2c6ad8df9b473cb0fc08c2596da7cf0e49be4b298d88cea927ac7f539f1edf228376d25
# expected: SHA-3-384       ec01498288516fc926459f58e2c6ad8df9b473cb0fc08c2596da7cf0e49be4b298d88cea927ac7f539f1edf228376d25

sha_512 = sha3_512()
sha_512.update(message_bytes)
print(f"SHA-3 512 bits: {sha_512.hexdigest()}")
# observed: SHA-3 512 bits: b751850b1a57168a5693cd924b6b096e08f621827444f70d884f5d0240d2712e10e116e9192af3c91a7ec57647e3934057340b4cf408d5a56592f8274eec53f0
# expected: SHA-3-512       b751850b1a57168a5693cd924b6b096e08f621827444f70d884f5d0240d2712e10e116e9192af3c91a7ec57647e3934057340b4cf408d5a56592f8274eec53f0


print("\nFor SHAKE\n")
shake_128_inst = shake_128()
shake_128_inst.update(message_bytes)
shake_128_digest = shake_128_inst.hexdigest(128 // 4)
print(f"Shake 128 bits: {shake_128_digest}")

shake_256_inst = shake_256()
shake_256_inst.update(message_bytes)
shake_256_digest = shake_256_inst.hexdigest(256 // 4)
# shake_256_digest = shake_256_inst.hexdigest(128 // 4)
print(f"Shake 256 bits: {shake_256_digest}")
