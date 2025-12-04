import random
import gradio as gr

# ---------- Helper functions ----------

def generate_random_students(n_students: int):
    """
    Generate a random class with names 'Student 1', 'Student 2', ...
    and random grades between 0 and 100.
    """
    students = []
    for i in range(n_students):
        name = f"Student {i + 1}"
        grade = random.randint(0, 100)
        students.append([name, grade])
    return students


def format_students(students):
    """
    Turn a list like [["Student 1", 78], ["Student 2", 92]]
    into: [Student 1 (78), Student 2 (92)]
    """
    parts = [f"{name} ({grade:g})" for name, grade in students]
    return "[" + ", ".join(parts) + "]"


def is_sorted(students, ascending):
    """
    Check if the list is sorted by grade in the chosen order.
    """
    grades = [g for _, g in students]
    if ascending:
        return all(grades[i] <= grades[i + 1] for i in range(len(grades) - 1))
    else:
        return all(grades[i] >= grades[i + 1] for i in range(len(grades) - 1))


def bubble_rule_should_swap(left_grade, right_grade, ascending):
    """
    Bubble Sort rule: when do we swap?
    """
    if ascending:
        return left_grade > right_grade
    else:
        return left_grade < right_grade


# ---------- Simulation functions ----------

def start_simulation(n_students, order_choice):
    """
    Create a random class and set up the first comparison.
    """
    try:
        n_students = int(n_students)
    except ValueError:
        n_students = 5  # default

    if n_students < 2:
        n_students = 2

    students = generate_random_students(n_students)
    n = len(students)
    ascending = (order_choice == "Lowest to highest")

    # Initial pass and position
    i = 0  # pass index
    j = 0  # position index

    list_text = format_students(students)

    left_name, left_grade = students[j]
    right_name, right_grade = students[j + 1]
    should_swap = bubble_rule_should_swap(left_grade, right_grade, ascending)

    comparison_text = (
        f"Pass {i + 1} – Compare {left_name} ({left_grade:g}) "
        f"and {right_name} ({right_grade:g})\n"
        f"Bubble Sort rule for this comparison: "
        f"{'Swap' if should_swap else 'Do NOT swap'}"
    )

    status = (
        "New random class generated.\n"
        "Use the buttons below to decide each step."
    )

    # At start: no swaps yet, no accuracy info yet
    swap_count = 0
    correct_decisions = 0
    total_decisions = 0
    finished = False

    return (
        list_text,
        comparison_text,
        status,
        students,
        i,
        j,
        swap_count,
        finished,
        order_choice,
        correct_decisions,
        total_decisions,
    )


def step_simulation(
    action,
    students,
    pass_index,
    position_index,
    swap_count,
    finished,
    order_choice,
    correct_decisions,
    total_decisions,
):
    """
    One step after the teacher presses Swap / Don't swap.
    """
    if students is None:
        return (
            "Click 'Start Simulation' to generate a class.",
            "",
            "No active simulation.",
            students,
            pass_index,
            position_index,
            swap_count,
            finished,
            order_choice,
            correct_decisions,
            total_decisions,
        )

    if finished:
        list_text = format_students(students)
        status = "Simulation already finished. Start again with a new class."
        return (
            list_text,
            "",
            status,
            students,
            pass_index,
            position_index,
            swap_count,
            finished,
            order_choice,
            correct_decisions,
            total_decisions,
        )

    n = len(students)
    ascending = (order_choice == "Lowest to highest")

    i = pass_index
    j = position_index

    # Current pair before action
    left_name, left_grade = students[j]
    right_name, right_grade = students[j + 1]
    rule_says_swap = bubble_rule_should_swap(left_grade, right_grade, ascending)

    teacher_chose_swap = (action == "swap")

    # Update accuracy counters
    total_decisions += 1
    if teacher_chose_swap == rule_says_swap:
        correct_decisions += 1

    # Apply teacher choice
    if teacher_chose_swap:
        students[j], students[j + 1] = students[j + 1], students[j]
        swap_count += 1
        teacher_action_text = "Teacher chose to SWAP these two students."
    else:
        teacher_action_text = "Teacher chose NOT to swap these two students."

    # Move to next position
    j += 1

    status = teacher_action_text

    # End of this pass?
    if j >= n - 1 - i:
        i += 1
        j = 0
        status += f"\nEnd of pass {i}. Moving to the next pass."

    # All passes done?
    if i >= n - 1:
        finished = True
        list_text = format_students(students)
        correct_order = is_sorted(students, ascending)

        # Accuracy
        if total_decisions > 0:
            accuracy = (correct_decisions / total_decisions) * 100
        else:
            accuracy = 0.0

        comparison_text = ""
        status += "\n\nSimulation finished. Final list locked."

        if correct_order:
            status += "\nThe final list IS correctly sorted according to the chosen order."
        else:
            status += "\nThe final list is NOT correctly sorted according to the chosen order."

        status += f"\nTotal swaps you performed: {swap_count}"
        status += f"\nYour decision accuracy: {accuracy:.1f}% "
        status += f"({correct_decisions} out of {total_decisions} decisions matched the Bubble Sort rule.)"

        return (
            list_text,
            comparison_text,
            status,
            students,
            i,
            j,
            swap_count,
            finished,
            order_choice,
            correct_decisions,
            total_decisions,
        )

    # Not finished: compute next comparison
    left_name, left_grade = students[j]
    right_name, right_grade = students[j + 1]
    should_swap = bubble_rule_should_swap(left_grade, right_grade, ascending)

    list_text = format_students(students)
    comparison_text = (
        f"Pass {i + 1} – Compare {left_name} ({left_grade:g}) "
        f"and {right_name} ({right_grade:g})\n"
        f"Bubble Sort rule for this comparison: "
        f"{'Swap' if should_swap else 'Do NOT swap'}"
    )

    return (
        list_text,
        comparison_text,
        status,
        students,
        i,
        j,
        swap_count,
        finished,
        order_choice,
        correct_decisions,
        total_decisions,
    )


def finish_now(
    students,
    pass_index,
    position_index,
    swap_count,
    finished,
    order_choice,
    correct_decisions,
    total_decisions,
):
    """
    Teacher clicks 'Finish now' before all passes complete.
    """
    if students is None:
        return (
            "Click 'Start Simulation' to generate a class.",
            "",
            "No active simulation.",
            students,
            pass_index,
            position_index,
            swap_count,
            finished,
            order_choice,
            correct_decisions,
            total_decisions,
        )

    ascending = (order_choice == "Lowest to highest")
    list_text = format_students(students)
    correct_order = is_sorted(students, ascending)

    status = "Teacher finished the list early.\n"

    if correct_order:
        status += "The final list IS correctly sorted according to the chosen order."
    else:
        status += "The final list is NOT correctly sorted according to the chosen order."

    if total_decisions > 0:
        accuracy = (correct_decisions / total_decisions) * 100
    else:
        accuracy = 0.0

    status += f"\nTotal swaps you performed: {swap_count}"
    status += f"\nYour decision accuracy: {accuracy:.1f}% "
    status += f"({correct_decisions} out of {total_decisions} decisions matched the Bubble Sort rule.)"

    finished = True

    return (
        list_text,
        "",
        status,
        students,
        pass_index,
        position_index,
        swap_count,
        finished,
        order_choice,
        correct_decisions,
        total_decisions,
    )


# ---------- Gradio UI ----------

with gr.Blocks(
    title="Marking Day – Bubble Sort Trainer",
    theme=gr.themes.Soft()
) as demo:
    gr.Markdown(
        """
        # Marking Day – Bubble Sort Trainer

        Train your Bubble Sort intuition as a teacher:
        - Pick class size and sort order
        - Let the app generate random grades
        - Decide **Swap** or **Don't swap** for each comparison
        - Check how accurate you were at the end
        """
    )

    with gr.Row():
        # Left: controls
        with gr.Column(scale=1):
            n_students_input = gr.Slider(
                minimum=2,
                maximum=20,
                value=5,
                step=1,
                label="Class size",
            )

            order_choice = gr.Radio(
                choices=["Highest to lowest", "Lowest to highest"],
                value="Highest to lowest",
                label="Sort order",
            )

            start_button = gr.Button("Start new class", variant="primary")

            gr.Markdown(
                """
                **How to play**
                1. Choose class size and order
                2. Click “Start new class”
                3. For each comparison, choose **Swap** or **Don't swap**
                4. Stop early with **Finish now** or let Bubble Sort finish
                """
            )

            with gr.Row():
                swap_button = gr.Button("Swap")
                dont_swap_button = gr.Button("Don't swap")
                finish_button = gr.Button("Finish now")

        # Right: live view
        with gr.Column(scale=2):
            list_display = gr.Markdown(
                label="Class list",
                value="Class list will appear here."
            )
            comparison_display = gr.Markdown(
                label="Current comparison",
                value="Start a class to see the first comparison."
            )
            status_display = gr.Markdown(
                label="Result and feedback",
                value="Progress and final accuracy will appear here."
            )

    # State variables (unchanged)
    students_state = gr.State()
    pass_state = gr.State(0)
    position_state = gr.State(0)
    swap_count_state = gr.State(0)
    finished_state = gr.State(False)
    order_state = gr.State("Highest to lowest")
    correct_decisions_state = gr.State(0)
    total_decisions_state = gr.State(0)

    # Start simulation
    start_button.click(
        fn=start_simulation,
        inputs=[n_students_input, order_choice],
        outputs=[
            list_display,
            comparison_display,
            status_display,
            students_state,
            pass_state,
            position_state,
            swap_count_state,
            finished_state,
            order_state,
            correct_decisions_state,
            total_decisions_state,
        ],
    )

    # Step with Swap
    swap_button.click(
        fn=lambda students, p, pos, swaps, fin, ord_choice, correct_dec, total_dec: step_simulation(
            "swap",
            students,
            p,
            pos,
            swaps,
            fin,
            ord_choice,
            correct_dec,
            total_dec,
        ),
        inputs=[
            students_state,
            pass_state,
            position_state,
            swap_count_state,
            finished_state,
            order_state,
            correct_decisions_state,
            total_decisions_state,
        ],
        outputs=[
            list_display,
            comparison_display,
            status_display,
            students_state,
            pass_state,
            position_state,
            swap_count_state,
            finished_state,
            order_state,
            correct_decisions_state,
            total_decisions_state,
        ],
    )

    # Step with Don't swap
    dont_swap_button.click(
        fn=lambda students, p, pos, swaps, fin, ord_choice, correct_dec, total_dec: step_simulation(
            "no_swap",
            students,
            p,
            pos,
            swaps,
            fin,
            ord_choice,
            correct_dec,
            total_dec,
        ),
        inputs=[
            students_state,
            pass_state,
            position_state,
            swap_count_state,
            finished_state,
            order_state,
            correct_decisions_state,
            total_decisions_state,
        ],
        outputs=[
            list_display,
            comparison_display,
            status_display,
            students_state,
            pass_state,
            position_state,
            swap_count_state,
            finished_state,
            order_state,
            correct_decisions_state,
            total_decisions_state,
        ],
    )

    # Finish early
    finish_button.click(
        fn=finish_now,
        inputs=[
            students_state,
            pass_state,
            position_state,
            swap_count_state,
            finished_state,
            order_state,
            correct_decisions_state,
            total_decisions_state,
        ],
        outputs=[
            list_display,
            comparison_display,
            status_display,
            students_state,
            pass_state,
            position_state,
            swap_count_state,
            finished_state,
            order_state,
            correct_decisions_state,
            total_decisions_state,
        ],
    )

if name == "main":
    demo.launch()