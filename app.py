import gradio as gr

def insertion_sort(arr):
    # Convert input string to list of integers
    # This line splits the input string (comma-separated) and converts each value to an integer
    arr = [int(x.strip()) for x in arr.split(',')] 
    steps = []  

   
    for partition in range(1, len(arr)):
        current = arr[partition]  # The current element to be inserted
        prevIndex = partition - 1  # Start comparing from the previous element

        # Capture state before any movement
        steps.append(f"Start partition {partition}: {arr}")  # Store the state before shifting

        # Move elements of arr[0..i-1] that are greater than current to one position ahead
        while prevIndex >= 0 and current < arr[prevIndex]:  # If current element is smaller than previous element
            arr[prevIndex + 1] = arr[prevIndex]  # Shift the element one position to the right
            prevIndex -= 1  # Move one position left in the array
            steps.append(f"Shift → {arr}")  # Capture the state after each shift

        # Insert the current element at the correct position (after the loop)
        arr[prevIndex + 1] = current  # Insert the current element where it belongs
        steps.append(f"Insert {current} → {arr}")  # Capture the state after insertion

    steps.append(f"Sorted: {arr}")  # Final sorted array
    return "\n".join(steps)  # Join the list of steps into a single string and return it


with gr.Blocks() as demo:
    gr.Markdown("## 🔍 Insertion Sort Visualizer")  
    gr.Markdown("Enter a comma‑separated list (e.g., `4,7,5,8,13`) to visualize each sorting step.")  

    input_box = gr.Textbox(label="Input Array")  # Input box where user enters the comma-separated array
    output_box = gr.Textbox(label="Sorting Steps", lines=15)  # Output box to display the sorting steps (with 15 lines)
    run_btn = gr.Button("Run Insertion Sort")  # Button to trigger the sorting

    
    run_btn.click(insertion_sort, inputs=input_box, outputs=output_box)

# Start the Gradio app when the script is executed
if __name__ == "__main__":
    demo.launch()  # Launch the Gradio app