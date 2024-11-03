# Digit Recognition Using a 5x5 Grid

This project uses Python, `tkinter`, and `scikit-learn` to create a simple GUI application where users can draw a 5x5 pixel representation of a digit. The application then uses logistic regression to predict the drawn digit.

## Features

- **Draw a Digit**: Toggle pixels in a 5x5 grid to draw a digit from 0 to 9.
- **Guess the Digit**: Press the "Guess the Number" button to see the model's prediction.
- **Logistic Regression Model**: Trained on predefined 5x5 digit patterns for basic recognition.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install numpy scikit-learn
   ```

2. **Run the Program**:
   Save the code in a Python file (e.g., `digit_recognition.py`), and execute it:
   ```bash
   python digit_recognition.py
   ```

## Example Patterns and Results

Below are the 5x5 patterns used to train the model. Each row shows the digit, the grid pattern representing it, and the model's expected prediction.

### 5x5 Patterns for Digits (0-9)

| Digit | Pattern | Model Prediction |
|-------|---------|------------------|
| **0** | ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) | **0** |
| **1** | ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) | **1** |
| **2** | ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) | **2** |
| **3** | Similar to **2** pattern with slight differences. | **3** |
| **4** | Vertical and horizontal patterns to match **4** structure. | **4** |
| **5** | Horizontal top and bottom, vertical middle. | **5** |
| **6** | Closed loop pattern similar to **0** but with middle. | **6** |
| **7** | Horizontal top, descending diagonal. | **7** |
| **8** | Full closed loop like two **0s**. | **8** |
| **9** | **0** pattern with right upper side. | **9** |

## Data fragmentation
## Data Fragmentation

For optimal performance, it's crucial to ensure that data fragmentation is less than 50%. Data fragmentation refers to a situation where the training data does not adequately represent the diversity of input patterns that the model may encounter. When the model is trained on a fragmented dataset, it may learn biases or fail to generalize well, leading to inaccurate predictions.

### Understanding Data Fragmentation

Data fragmentation can occur in various forms:

1. **Underrepresentation of Classes**: If certain digits are drawn much less frequently than others in the training set, the model may struggle to accurately recognize those digits.

2. **Insufficient Variety in Drawings**: If the same patterns of digits are repeated without variation, the model may not learn to recognize different ways the same digit can be represented.

3. **Lack of Noise or Distortions**: In real-world scenarios, digits might be drawn with variations such as different sizes, rotations, or noise. If the training set lacks such diversity, the model may fail to recognize distorted inputs.

### Example of Data Fragmentation

Consider a scenario where we have the following digit representations in our training dataset:

- **Digit 0**: 80 samples
- **Digit 1**: 5 samples
- **Digit 2**: 5 samples
- **Digit 3**: 5 samples
- **Digit 4**: 5 samples
- **Digit 5**: 5 samples
- **Digit 6**: 5 samples
- **Digit 7**: 5 samples
- **Digit 8**: 5 samples
- **Digit 9**: 5 samples

In this case, the model is predominantly trained on the digit `0`, resulting in significant fragmentation. The imbalance shows that:

- **Fragmentation**: The training data for digits `1` through `9` only accounts for 20% of the dataset, which is well below the threshold needed for accurate recognition.

#### Placeholder Example Visualization

To visualize the data fragmentation, consider using a pie chart or bar graph:

```plaintext
+--------------------------------+
|          Data Distribution      |
|                                |
|   0: █████████████████████████  (80 samples)
|   1: ███                      (5 samples)
|   2: ███                      (5 samples)
|   3: ███                      (5 samples)
|   4: ███                      (5 samples)
|   5: ███                      (5 samples)
|   6: ███                      (5 samples)
|   7: ███                      (5 samples)
|   8: ███                      (5 samples)
|   9: ███                      (5 samples)
|                                |
+--------------------------------+
```
### Example Usage

1. **Draw a number** by toggling the pixels on the grid.
2. **Click "Guess the Number"** to let the model predict your digit.
3. **View the result** displayed under the button.

This app is a fun, small-scale digit recognition model, using a simplistic training set for demonstration purposes. Ideal for experimenting with digit recognition without complex models.

### Bonus

Here are some basic 5x5 patterns for the digits 0 through 9 that you can use to help your model recognize each digit. These are simplified and may vary depending on how you want to display each number.

Each pattern is represented by a flattened 5x5 binary grid, where:
- **1** represents a filled (black) cell.
- **0** represents an empty (white) cell.

You can use these patterns to train or test the model by inputting them into your application.

```plaintext
0:
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1

Pattern: [1, 1, 1, 1, 1,
          1, 0, 0, 0, 1,
          1, 0, 0, 0, 1,
          1, 0, 0, 0, 1,
          1, 1, 1, 1, 1]

1:
0 0 1 0 0
0 1 1 0 0
0 0 1 0 0
0 0 1 0 0
0 1 1 1 0

Pattern: [0, 0, 1, 0, 0,
          0, 1, 1, 0, 0,
          0, 0, 1, 0, 0,
          0, 0, 1, 0, 0,
          0, 1, 1, 1, 0]

2:
1 1 1 1 1
0 0 0 0 1
1 1 1 1 1
1 0 0 0 0
1 1 1 1 1

Pattern: [1, 1, 1, 1, 1,
          0, 0, 0, 0, 1,
          1, 1, 1, 1, 1,
          1, 0, 0, 0, 0,
          1, 1, 1, 1, 1]

3:
1 1 1 1 1
0 0 0 0 1
0 1 1 1 1
0 0 0 0 1
1 1 1 1 1

Pattern: [1, 1, 1, 1, 1,
          0, 0, 0, 0, 1,
          0, 1, 1, 1, 1,
          0, 0, 0, 0, 1,
          1, 1, 1, 1, 1]

4:
1 0 0 1 0
1 0 0 1 0
1 1 1 1 1
0 0 0 1 0
0 0 0 1 0

Pattern: [1, 0, 0, 1, 0,
          1, 0, 0, 1, 0,
          1, 1, 1, 1, 1,
          0, 0, 0, 1, 0,
          0, 0, 0, 1, 0]

5:
1 1 1 1 1
1 0 0 0 0
1 1 1 1 1
0 0 0 0 1
1 1 1 1 1

Pattern: [1, 1, 1, 1, 1,
          1, 0, 0, 0, 0,
          1, 1, 1, 1, 1,
          0, 0, 0, 0, 1,
          1, 1, 1, 1, 1]

6:
1 1 1 1 1
1 0 0 0 0
1 1 1 1 1
1 0 0 0 1
1 1 1 1 1

Pattern: [1, 1, 1, 1, 1,
          1, 0, 0, 0, 0,
          1, 1, 1, 1, 1,
          1, 0, 0, 0, 1,
          1, 1, 1, 1, 1]

7:
1 1 1 1 1
0 0 0 0 1
0 0 0 1 0
0 0 1 0 0
0 1 0 0 0

Pattern: [1, 1, 1, 1, 1,
          0, 0, 0, 0, 1,
          0, 0, 0, 1, 0,
          0, 0, 1, 0, 0,
          0, 1, 0, 0, 0]

8:
1 1 1 1 1
1 0 0 0 1
1 1 1 1 1
1 0 0 0 1
1 1 1 1 1

Pattern: [1, 1, 1, 1, 1,
          1, 0, 0, 0, 1,
          1, 1, 1, 1, 1,
          1, 0, 0, 0, 1,
          1, 1, 1, 1, 1]

9:
1 1 1 1 1
1 0 0 0 1
1 1 1 1 1
0 0 0 0 1
1 1 1 1 1

Pattern: [1, 1, 1, 1, 1,
          1, 0, 0, 0, 1,
          1, 1, 1, 1, 1,
          0, 0, 0, 0, 1,
          1, 1, 1, 1, 1]
```

### Usage
To input these patterns in your application, simply toggle each cell in the 5x5 grid according to the pattern for each digit. For example, to display **2**, you would toggle the cells corresponding to `1` in the pattern for `2`.

These patterns are a good starting point, but you may want to create multiple variations or add slight modifications to improve the model’s accuracy when guessing real user-drawn digits.

