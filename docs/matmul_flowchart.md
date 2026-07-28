# Matrix Multiplication Flowchart — `matmul(A, B)`

Algorithm: multiply `A` (m×n) by `B` (n×p) → result `C` (m×p).

```mermaid
flowchart TD
    START(["START: matmul(A, B)"]) --> DIMS["Get dimensions:\nm = len(A), n = len(A[0])\np = len(B[0])"]
    DIMS --> INIT["Initialise result matrix C\nwith zeros (m × p)"]
    INIT --> LOOP_I["OUTER LOOP\nfor i in range(m)"]
    LOOP_I --> LOOP_J["MIDDLE LOOP\nfor j in range(p)"]
    LOOP_J --> INIT_S["Set running sum s = 0"]
    INIT_S --> LOOP_K["INNER LOOP\nfor k in range(n)"]
    LOOP_K --> MULADD["s += A[i][k] * B[k][j]"]
    MULADD --> CHECK_K{"k == n - 1 ?"}
    CHECK_K -- No --> LOOP_K
    CHECK_K -- Yes --> STORE["Store C[i][j] = s"]
    STORE --> CHECK_J{"j == p - 1 ?"}
    CHECK_J -- No --> LOOP_J
    CHECK_J -- Yes --> CHECK_I{"i == m - 1 ?"}
    CHECK_I -- No --> LOOP_I
    CHECK_I -- Yes --> RETURN(["RETURN C"])
```

## Legend

| Symbol | Meaning |
|---|---|
| `[ ... ]` | Process step |
| `{ ... }` | Decision / condition |
| `([ ... ])` | Start / End (stadium shape) |
| `-->` | Flow direction |

## Complexity

- **Time**: O(m × n × p) — triple nested loops
- **Space**: O(m × p) — for the result matrix `C`

## How to render this chart

### In Google Colab:

```python
!pip install colab-print
import colab_print
colab_print.print_mermaid("""
flowchart TD
    START(["START: matmul(A, B)"]) --> DIMS["Get dimensions: ..."]
    ...
""")
```

### In VS Code:

Install the **Markdown Preview Mermaid Support** extension, then open this
file and press `Ctrl+Shift+V`.

### Online:

Copy the Mermaid block (between the triple backticks) into
[mermaid.live](https://mermaid.live/).
