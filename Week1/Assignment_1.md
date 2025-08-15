## Figure out any problem which you can't solve on a classical computer

**1. The Halting Problem (Undecidable)**

This is the classic example, discovered by Alan Turing in 1936.

**Problem**: Can a computer program determine whether another program will eventually stop (halt) or run forever?

**Answer**: No, it’s impossible to create a program that correctly solves this for all other programs.

✅ Works for some cases.

❌ But a universal solution doesn't exist.

**2. The Entscheidungsproblem (Decision Problem)**
This was part of David Hilbert’s goal to formalize all mathematics. Turing and Gödel proved it’s impossible.

**Problem**: Can a machine decide whether any given mathematical statement is provable?

**Answer**: No. Some truths can't be proven using any formal system.

**3. Gödel’s Incompleteness Theorems**

These don’t describe computing problems per se, but they limit what any logic-based system (including software) can prove or solve.

**Main idea**: In any powerful enough system, there will always be true statements that cannot be proven within that system.

**4. Problems Too Complex (Intractable)**

Even if a problem is theoretically solvable, it might be computationally infeasible (i.e., would take more time than the age of the universe).
-    Example: Traveling Salesman Problem for 10,000 cities (NP-Hard)
-    No known efficient algorithms exist for some of these problems
-    Quantum computing might help with some, but not all


## Find out what sort of physical technologies are currently being worked on to build and generate cubits

**Superconducting Qubits**

-    How It Works: Uses superconducting circuits cooled near absolute zero to create quantized energy states.
-    Pros: Mature technology, good scalability, supported by major companies.
-    Cons: Requires extreme cooling, still prone to errors.
-    Current Leaders: IBM, Google, Rigetti.

**Trapped Ion Qubits**
-    How It Works: Uses ions trapped in electromagnetic fields; qubits stored in ions’ internal states, manipulated by lasers.
-    Pros: Very stable qubits, long coherence times.
-    Cons: Slow gate speeds, scaling is harder.
-    Current Leaders: IonQ, Quantinuum.

**Spin Qubits (Quantum Dots)**
-    How It Works: Uses the spin of electrons in semiconductor nanostructures.
-    Pros: Smaller and potentially integrable with existing chip technology.
-    Cons: Fabrication and control challenges.
-    Current Leaders: Intel, Delft University.

**Photonic Qubits**
-    How It Works: Encodes qubits in photons’ polarization or path.
-    Pros: Works at room temperature, easy to transmit over distance.
-    Cons: Photon losses, requires efficient single-photon sources.
-    Current Leaders: Xanadu, PsiQuantum.

**Topological Qubits**
-    How It Works: Uses exotic quasiparticles (anyons) that store information in their braiding (topology).
-    Pros: Theoretically very resistant to errors.
-    Cons: Still experimental — no large-scale systems yet.
-    Current Leaders: Microsoft (StationQ).
