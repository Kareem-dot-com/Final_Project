# Marking Day – Bubble Sort Teacher Trainer
This project is an interactive Bubble Sort trainer designed around a classroom “marking day” theme.
The program generates a random list of students with randomized grades and guides the user, acting as the teacher, through the sorting process.
At each comparison step, the teacher chooses whether to swap the students or leave them as they are, and the system evaluates the accuracy of these decisions according to Bubble Sort rules.
At the end of the session, the program reports the final sorted list, the number of swaps performed, and the user’s overall accuracy.

---

Why I chose bubble sort: For this project, I needed to choose one algorithm from the list provided in the assignment guidelines, which included both searching algorithms (Linear Search, Binary Search) and sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort). I decided to implement Bubble Sort because its structure makes it especially well suited for an interactive demonstration. Bubble Sort progresses through a list using repeated adjacent comparisons, which translates naturally into a step-by-step interface where a user can view each comparison and decide whether to swap or not. This supports the requirement to “visualize and interactively demonstrate one algorithm” in a clear and intuitive way.

--- 
Video of tests: 

A variety of tests were performed to confirm correct functionality.

Test 1: Small class (2 students).
Expected: One comparison only.
Result: App handles single comparison correctly.

Test 2: Medium class (5–10 students).
Random grades each run.
Teacher decisions correctly tracked.
Final accuracy displayed accurately.

Test 3: Lowest-to-highest order.
Bubble Sort recommended swaps matched expected ascending logic.
Final sorted order validated correctly.

Test 4: Highest-to-lowest order.
Bubble Sort rule reversed as expected.
Accuracy scoring properly adjusted.

Test 5: Early stop (Finish now).
Accuracy calculated based only on completed decisions.
App correctly reports if final list is sorted or not.

Test 6: Wrong decisions on purpose.
Accuracy dropped accordingly.
Final list validation correctly marked as “NOT sorted.”

These tests demonstrate correctness, handling of edge cases, and proper Bubble Sort behavior.

---

Link of app: https://kareemalk-marking-day-bubble-sort-teacher-trainer.hf.space

--- 

Decomposition

To build this project, I divided the overall problem into a sequence of smaller tasks that match the structure of Bubble Sort. The app first generates a random list of students with assigned grades. It then identifies which two students need to be compared, presents that comparison to the user, and waits for a decision. After the user chooses to swap or not swap, the list updates and the program moves to the next pair. Once the end of a pass is reached, the program automatically transitions to the next pass until sorting is complete or the user chooses to finish early. Breaking the work into these simple steps made the entire sorting process easier to control, test, and explain.

Pattern Recognition

Bubble Sort relies on repeated, predictable actions, and the app highlights this pattern. Every comparison follows the same structure: two adjacent students, a check to see whether a swap is needed, and an update to the list. Each pass repeats this pattern across the full list, pushing the highest or lowest grade toward its correct position. By structuring the app around these recurring patterns, the user can experience the consistent rhythm of Bubble Sort and begin to recognize how small local decisions gradually sort the entire list.

Abstraction

To keep the interaction simple and uncluttered, I hid all algorithmic details that are unnecessary for the user to understand. Instead of showing index numbers, nested loops, or internal state variables, the app only shows the essential information: the current list, the two students being compared, and whether Bubble Sort would recommend a swap. This abstraction allows the user to focus on the sorting logic rather than the mechanics behind it, and it frames Bubble Sort in a way that feels natural for someone acting as a teacher reviewing student grades.

Algorithm Design

The design of the algorithm follows the traditional Bubble Sort structure. The program tracks both the current pass and the current position within that pass, determines whether a swap is recommended based on the chosen sorting order, and moves step-by-step through the list. Each decision is recorded so that accuracy can be calculated at the end of the simulation. By combining these components with Gradio’s state management system, the program is able to present Bubble Sort one comparison at a time while keeping all internal variables synchronized behind the scenes. This design results in an interactive sorting experience that remains faithful to the algorithm’s logic.

--- 

Steps to run:

When the user starts a simulation, the program generates a class list containing randomly assigned grades.
The interface then presents one comparison at a time.
Each comparison includes the two students being evaluated and a message indicating what Bubble Sort would do in that situation.

The user then chooses whether to swap or not.
Each decision updates the list visually and progresses the algorithm to the next comparison.
Users can continue through all passes or end the session early by clicking “Finish now.”
At the end, the tool shows the final sorted list, indicates whether it is truly sorted, and provides a summary of the number of swaps performed along with the user’s decision accuracy.

This interaction turns Bubble Sort into a hands-on process instead of something hidden inside code.

---
Author & Acknowledgment: 

This project was created by Your Name for the CISC-121 final project at Queen’s University. All core design decisions, implementation work, testing, and documentation were done by me. I used AI tools during development to help clarify certain programming concepts, improve parts of the code structure, and better understand some of the underlying logic behind state management and Bubble Sort behavior. These tools supported my learning but did not replace my own work or decision-making throughout the project.

I would also like to acknowledge the course instructor for providing the assignment guidelines and the structure that shaped this project. The external tools used—Python, Gradio, and Hugging Face Spaces—supported the development and deployment of the interactive application.
