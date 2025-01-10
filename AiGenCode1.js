// Function to visualize the shortest paths in an unweighted graph using A* search algorithm
function visualizeShortestPaths(graph, startNode) {
  const openSet = [startNode];
  const cameFrom = {};
  const gScore = { [startNode]: 0 };
  const fScore = { [startNode]: heuristic(startNode) };

  while (openSet.length > 0) {
    let currentNode = openSet[0];

    for (const neighbor of graph[currentNode]) {
      if (!gScore[neighbor] || gScore[neighbor] + heuristic(neighbor) < fScore[neighbor]) {
        cameFrom[neighbor] = currentNode;
        gScore[neighbor] = gScore[currentNode] + 1;
        fScore[neighbor] = gScore[neighbor] + heuristic(neighbor);
        if (!openSet.includes(neighbor)) openSet.push(neighbor);
      }
    }

    openSet.sort((a, b) => fScore[a] - fScore[b]);
    if (openSet.length === 0 || !openSet[0]) break;
    openSet.shift();
  }

  const path = [];
  let current = startNode;

  while (current !== undefined) {
    path.unshift(current);
    current = cameFrom[current];
  }

  return { shortestPath: path, gScores: gScore };
}

// Heuristic function for A* search algorithm
function heuristic(node) {
  // For this example, we'll use a simple Manhattan distance heuristic
  switch (node) {
    case 'A':
      return 0;
    case 'B':
      return Math.abs(1 - node);
    case 'C':
      return Math.abs(2 - node);
    default:
      throw new Error(`Unknown node: ${node}`);
  }
}

// Example usage
const graph = {
  A: ['B', 'C'],
  B: ['A', 'D'],
  C: ['A', 'F'],
  D: ['B'],
  E: ['F'],
  F: ['C', 'E']
};

console.log(visualizeShortestPaths(graph, 'A'));
