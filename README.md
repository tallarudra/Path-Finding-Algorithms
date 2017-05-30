# Path-Finding-Algorithms<br>
Given set of nodes and the distance between them, it finds the path between the start node and goal node using BFS, DFS, A* and UCS Algorithms.

<h2>Usage</h2>
Run the pathFinder.py file without providing any arguments. The program will ask 2 inputs from the User:<br>
    <ol><li>Name of the file present in the same directory as pathFinder.py or a relative link to the input file.<li>The algorithm to be used to compute the path. (BFS, DFS, A*, UCS - Case Sensitive).</ol><br>
    Input Format:<br>
    &lt;START STATE&gt;<br>&lt;GOAL STATE&gt;<br>&lt;NUMBER OF PATHS&gt;<br>&lt;... PATHS ...&gt;<br>&lt;NUMBER OF HEURISTIC PATHS&gt;<br>&lt;... HEURISTIC PATHS ...&gt;<br><br>
    The input consists of the start state, goal state, number of 'n' paths, followed by 'n' paths on a seperate line where each path is of the format &lt;fromState toState Cost&gt;. Next, it has the number of heuristic paths followed by the heuristic paths in the same format.<br>
    <br>
    <h3>Output</h3><br>
    The output path is generated in an output.txt file. The output files contains multiple lines where each line is of the format:<br>
    &lt;STATE&gt; &lt;ACCUMULATED TRAVEL TIME FROM START TO HERE&gt;</br>
 
