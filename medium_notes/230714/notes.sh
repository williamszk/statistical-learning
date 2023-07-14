

docker build -t my-base-image .

docker build -t base-python-image -f Dockerfile.base .

docker build -t my-test-image -f ./tests/Dockerfile .
docker run -t --rm my-test-image

tree | grep -v ".venv"
tree

.
├── 230714
│   ├── Dockerfile
│   └── notes.sh
└── notes.md

1 directory, 3 files