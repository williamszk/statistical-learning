enum CellHealth {
	Alive = 1,
	Dead,
}

type CellState = {
	cellHealth: CellHealth;
	numNeighbors: number;
};

function getCellHealth(): CellHealth {
	// need to implement
	return CellHealth.Alive;
}

function getNumNeighbors(): number {
	let numNeighbors = 4;
	// need to implement
	if (numNeighbors > 8) {
		// There is some problem!
		// the output should not be above 8
		throw new Error('numNeighbors should not be greater than 8');
	} else if (numNeighbors < 0) {
		throw new Error('numNeighbors should not be less than 8');
	}

	return numNeighbors;
}

let numNeighbors = getNumNeighbors;

let currentCell: CellState = {
	cellHealth: getCellHealth(),
	numNeighbors: getNumNeighbors(),
};

getCellHealth();
let nextCell = undefined;

switch (currentCell.cellHealth) {
	case CellHealth.Dead:
		if (currentCell.numNeighbors == 3) {
			currentCell.cellHealth = CellHealth.Alive;
		}
	case CellHealth.Alive:
		break;
	default:
		break;
}
// https://youtu.be/ygdPRlSo3Qg?t=446
