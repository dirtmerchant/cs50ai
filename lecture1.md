# Lecture 1

## Agent

- An entity that percieves its environment and acts upon that environment

## State

- A configuration of the agent in its environment

### Initial State

- Where the agent starts
- How do we get from the initial position to the goal?

## Actions

`actions(s) returns the set of actions that can be executed in state set`

- 15 puzzle usually has 4 actions (left, right, up, down)

## Transition Model 

- A description of what state results from any applicable action in any state

`results(s,a) returns the state resulting from performa action a in state se

## State Space 

- The set of all reachable from the initial state by any sequence of actions

## Path Cost

- Numerical ccost associate with a given path

## Node 

- A data structure that keeps track of 
    - a state
    - a parent (node that generated this node)
    - an action (action applied to parent to get node)
    - a path cost (from initial state to node)

## Frontier

- Represents all things we could explore that we have not yet explored

## Approach

- Start with a frontier that contains the initial state
- Repeat
    - If the frontier is empty, then there is no solution
    - Remove a node from the frontier
    - If the node contains the goal state, return the solution
    - Expand node, add resulting nodes to the frontier
    

## Find a path from A to E

    a -> b -> c -> e
           -> d -> f


## Revised Approach 

- Start with a frontier that contains the initial state
- Start with an empty explored set
- Repeat
    - If the frontier is empty, then there is no solution
    - Remove a node from the frontier
    - If the node contains the goal state, return the solution
    - Add the node to the explored set
    - Expand node, add add resulting nodes to the frontier if they aren't already in the frontier or the explored set

    a <-> b -> c -> e
            -> d -> f



## Depth-first search

- Search algorith that always expands the deepest nod in the frontier

    - Will always solve a search, but may not choose the most efficient path

## Stack

- Last in, first out data type

## Breadth-first search

- Search algorith that always expands the shallowest node in the frontier

    - Will always solve a search, but will need to explore more states to find the most efficient path
    
## Queue 

- First in first out data type