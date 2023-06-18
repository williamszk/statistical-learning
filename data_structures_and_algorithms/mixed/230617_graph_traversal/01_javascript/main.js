// The Data
const airports = 'phx bkk okc jfk lax mex eze hel los lap lim'.split(' ');

const routes = [
	['phx', 'lax'],
	['phx', 'jfk'],
	['jfk', 'okc'],
	['jfk', 'hel'],
	['jfk', 'los'],
	['mex', 'lax'],
	['mex', 'bkk'],
	['mex', 'lim'],
	['mex', 'eze'],
	['lim', 'bkk'],
];
// those routes are few compared to the number of nodes, so the matrix is sparse
// if the matrix is sparse then it will take a lot of
// unused space
// an adjacency list takes less space

// the graph
const adjacencyList = new Map();
// the key of the map is a string and the value is an array

// add node
function addNode(airport) {
	adjacencyList.set(airport, []);
}

// add edge (undirected)
function addEdge(origin, destination) {
	adjacencyList.get(origin).push(destination);
	adjacencyList.get(destination).push(origin);
	// FIXME: this could potentially repeat the edge if we have e.g.:
	// ['phx', 'lax'],
	// ['lax', 'phx'],
}

// create the graph
airports.forEach(addNode);
routes.forEach((route) => addEdge(...route));

console.log(adjacencyList);
// Map(11) {
//   'phx' => [ 'lax', 'jfk' ],
//   'bkk' => [ 'mex', 'lim' ],
//   'okc' => [ 'jfk' ],
//   'jfk' => [ 'phx', 'okc', 'hel', 'los' ],
//   'lax' => [ 'phx', 'mex' ],
//   'mex' => [ 'lax', 'bkk', 'lim', 'eze' ],
//   'eze' => [ 'mex' ],
//   'hel' => [ 'jfk' ],
//   'los' => [ 'jfk' ],
//   'lap' => [],
//   'lim' => [ 'mex', 'bkk' ]
// }

// find out if there is route between phx and bkk
// we can use breadth first search (BFS) or use depth first search (DFS)

// https://youtu.be/cWNEl4HE2OE?t=350