# The $\Psi$-reka Problem

Let there be a desired distribution, i.e. 24.06% - 58.89% - 17.05%.

Suppose you are now given a set of datapoints, with its own distribution.

For example:

|            | _01_       | _02_       | _03_       |
| ---------- | ---------- | ---------- | ---------- |
|            | 123        | 32         | 21         |
|            | 23         | 515        | 88         |
|            | 252        | 321        | 450        |
| **$\sum$** | **398**    | **868**    | **559**    |
| $\\\%$     | **21.80%** | **47.56%** | **30.63%** |

Create a program where we can append or prepend the decimal string of each datapoint, i.e.

$$
"123"\rightarrow "x123"\text{ or }"123x"\text{ or }"12"\text{ or }"23"\text{, where }x\in[0,9]\subset\mathbb{Z}
$$

such that in the end, the distribution of the datapoint is closest to our "desired distribution".
