def f(x):
    """The function we want to minimize."""
    return (x - 5) ** 2 + 10
 
 
def hill_climbing(start_x, step_size=1.0, min_step=1e-5, shrink_factor=0.5):
    """
    Performs hill climbing to find the x that minimizes f(x).
    Returns (best_x, best_f, history) where history is a list of
    (iteration, x, f(x)) tuples for every point actually moved to.
    """
    current_x = start_x
    current_f = f(current_x)
    history = [(0, current_x, current_f)]
 
    iteration = 0
    step = step_size
 
    print(f"{'Iter':<6}{'x':<12}{'f(x)':<12}")
    print("-" * 30)
    print(f"{iteration:<6}{current_x:<12.5f}{current_f:<12.5f}")
 
    while step > min_step:
        # Generate the two neighbours
        right_x = current_x + step
        left_x = current_x - step
        right_f = f(right_x)
        left_f = f(left_x)
 
        # Move to whichever neighbour is better (lower f), if any
        if right_f < current_f and right_f <= left_f:
            current_x, current_f = right_x, right_f
        elif left_f < current_f:
            current_x, current_f = left_x, left_f
        else:
            # No neighbour improves f(x) at this step size -> shrink the step
            step *= shrink_factor
            continue
 
        iteration += 1
        history.append((iteration, current_x, current_f))
        print(f"{iteration:<6}{current_x:<12.5f}{current_f:<12.5f}")
 
    return current_x, current_f, history
 
 
def main():
    print("Hill Climbing Search")
    print("=" * 30)
    start_x = 0.0   # initial value of x
    print(f"Initial x : {start_x}\n")
 
    best_x, best_f, history = hill_climbing(start_x)
 
    print("\nApproximate x that minimizes f(x):", round(best_x, 4))
    print("Minimum value of f(x):", round(best_f, 4))
 
 
if __name__ == "__main__":
    main()
 