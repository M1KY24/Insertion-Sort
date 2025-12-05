---
title: Insertion Sort
emoji: 👀
colorFrom: red
colorTo: indigo
sdk: gradio
sdk_version: 6.0.2
app_file: app.py
pinned: false
license: mit
---
```

Decomposition:
Handle input first by separating the user's comma separated string and turning it into an integer. Second, perform the core insertion sort method, where the left part of the list is viewed as sorted and the right part as unsorted. Third, capture each essential step of the algorithm into a steps list for display on how the sorting is done.  Lastly, attach this logic to a straightforward Gradio GUI that has an input textbox, a sort button, and an output textbox that shows all of the steps that were recorded.

Pattern Recognition:
The algorithm repeatedly applies the same pattern to each element after the first. For each new element, it compares it to the elements in the sorted region, adjusts any larger elements one position to the right, and then inserts the current one into the correct location. Every partition follows the same series of actions: start a new partition, execute zero or more shifts, and then perform one insert. In theory, the list is always split between a sorted prefix and an unsorted suffix.

Abstraction:
I will only display the algorithm's essential actions to make the visualization simpler. At key moments, the user will view the complete array with labels like "Start partition," "Shift", "Insert," and "Sorted" to show how the algorithm is progressing. The user won't see internal features like the partition and prevIndex variables, loop syntax, or type conversions. Instead of concentrating on the algorithm's inner workings, I want to show how the list changes. In order to keep the interface simple and centered on the sorting process, I will also assume that the user enters correct integers and will not incorporate any error handling logic.

Algorithm Design (Input → Processing → Output + GUI)
Input: The user hits the "Run Insertion Sort" button after entering a series of integers separated by commas in the Gradio textbox (Input Array).  
The external datatype is str (integers separated by commas).  
After parsing, the internal datatype is list[int].

Processing: The string is parsed into a list of numbers by the insertion_sort function, which then performs the insertion sort and logs each step as a message that can be read by humans in a steps list. All of the messages are combined into a single multi-line string once the loop is complete.

Output: The user can scroll through the algorithm's execution from unsorted to fully sorted by sending the multi line string containing all the stages back to the Gradio output textbox (Sorting stages).

Flowchart:
![Flow Chart](image.png)

Testing:
[![Insertion Sort Visualization](https://img.youtube.com/vi/_UwsIHs9mg0/0.jpg)](https://youtu.be/_UwsIHs9mg0)

Hugging Face link: https://huggingface.co/spaces/M1KY/Insertion_Sort




```

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
Testing of the project https://www.youtube.com/watch?v=_UwsIHs9mg0

