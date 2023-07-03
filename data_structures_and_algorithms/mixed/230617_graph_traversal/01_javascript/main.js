// The Data
const airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM'.split(' ');

const routes = [
	['PHX', 'LAX'],
	['PHX', 'JFK'],
	['JFK', 'OKC'],
	['JFK', 'HEL'],
	['JFK', 'LOS'],
	['MEX', 'LAX'],
	['MEX', 'BKK'],
	['MEX', 'LIM'],
	['MEX', 'EZE'],
	['LIM', 'BKK'],
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

	// TODO: this could potentially repeat the edge if we have e.g.:
	// ['PHX', 'LAX'],
	// ['LAX', 'PHX'],
	// Ideally we should not have the `routes` repeating the connection
}

// create the graph
airports.forEach(addNode);
routes.forEach((route) => addEdge(...route));
// routes.forEach((route) => addEdge(route[0], route[1])); // this is an alternative

console.log(adjacencyList);
// Map(11) {
//   'PHX' => [ 'LAX', 'JFK' ],
//   'BKK' => [ 'MEX', 'LIM' ],
//   'OKC' => [ 'JFK' ],
//   'JFK' => [ 'PHX', 'OKC', 'HEL', 'LOS' ],
//   'LAX' => [ 'PHX', 'MEX' ],
//   'MEX' => [ 'LAX', 'BKK', 'LIM', 'EZE' ],
//   'EZE' => [ 'MEX' ],
//   'HEL' => [ 'JFK' ],
//   'LOS' => [ 'JFK' ],
//   'LAP' => [],
//   'LIM' => [ 'MEX', 'BKK' ]
// }

// find out if there is route between phx and bkk
// we can use breadth first search (BFS) or use depth first search (DFS)

function bfs(start) {
	const visited = new Set();

	// queue = first in first out
	const queue = [start];

	while (queue.length > 0) {
		// .shift will return the first item and remove it from the array
		const airport = queue.shift();

		const destinations = adjacencyList.get(airport);

		for (const destination of destinations) {
			if (destination === 'BKK') {
				console.log('found it!');
			}
			if (!visited.has(destination)) {
				visited.add(destination);
				queue.push(destination);
				console.log(destination);
			}
		}
	}
}

bfs('PHX');

// https://youtu.be/cWNEl4HE2OE?t=515