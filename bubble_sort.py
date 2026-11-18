# Bubble Sort Algorithm Implementation and Demonstration

def bubble_sort(arr):
    """
    Bubble sort implementation with step-by-step state logging.
    """
    a = list(arr)
    n = len(a)
    steps = []
    steps.append(("Initial", list(a)))
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
                steps.append((f"Swap ({a[j+1]} <-> {a[j]})", list(a)))
        if not swapped:
            break
    steps.append(("Sorted", list(a)))
    return a, steps

if __name__ == "__main__":
    initial_data = [4, 1, 3, 9, 2, 6, 5, 8]
    print(f"Original Array: {initial_data}")
    sorted_data, steps = bubble_sort(initial_data)
    print(f"Sorted Array  : {sorted_data}")
    print("\nStep-by-step transitions:")
    for idx, (action, state) in enumerate(steps):
        print(f"Step {idx:02d} [{action}]: {state}")
