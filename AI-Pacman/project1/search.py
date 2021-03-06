# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    # simple commands to understand the search problem
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # pre
    visited_node = []
    path = []
    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    # Circulation
    while not frontier.isEmpty():
        current_node, path = frontier.pop()
        if problem.isGoalState(current_node):
            return path
        else:
            visited_node.append(current_node)
            expand_results = problem.getSuccessors(current_node)  # return (successor,action,and stepCost)
            for successor, action, stepCost in expand_results:
                new_path = path + [action]
                new_node = (successor, new_path)
                if successor not in visited_node:
                    frontier.push(new_node)
    return path

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"

    visited_node = []
    path = []
    frontier = util.Queue()
    frontier.push((problem.getStartState(), []))
    while not frontier.isEmpty():
        current_node, path = frontier.pop()
        if problem.isGoalState(current_node):
            return path
        elif current_node not in visited_node:
            visited_node.append(current_node)
            expand_results = problem.getSuccessors(current_node)
            for successor, action, stepCost in expand_results:
                new_path = path + [action]
                new_node = (successor, new_path)
                if successor not in visited_node:
                    frontier.push(new_node)
    return path

    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    visited_node = []
    path = []
    frontier = util.PriorityQueue()
    start = (problem.getStartState(), [], 0)
    frontier.push(start, start[2])
    while not frontier.isEmpty():
        current_node, path, cost = frontier.pop()
        if problem.isGoalState(current_node):
            return path
        else:
            visited_node.append(current_node)
            expand_results = problem.getSuccessors(current_node)
            for successor, action, stepCost in expand_results:
                new_path = path + [action]
                new_cost = cost + stepCost
                new_node = (successor, new_path, new_cost)
                if successor not in visited_node:
                    frontier.push(new_node, new_cost)
    return path
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"

    visited_node = []
    path = []
    frontier = util.PriorityQueue()
    start = (problem.getStartState(), [], 0)
    frontier.push(start, 0)
    while not frontier.isEmpty():
        current_node, path, cost = frontier.pop()
        if problem.isGoalState(current_node):
            return path
        else:
            visited_node.append(current_node)
            expand_results = problem.getSuccessors(current_node)
            for successor, action, stepCost in expand_results:
                new_path = path + [action]
                new_cost = problem.getCostOfActions(new_path) + heuristic(successor, problem)
                new_node = (successor, new_path, new_cost)
                if successor not in visited_node:
                    frontier.push(new_node, new_cost)
    return path


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
