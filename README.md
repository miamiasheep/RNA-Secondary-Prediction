# CS571_final_project
This repository is for CS571 final project in Purdue University.


## Nussinov's Algorithm
In the directory of nussinov, it is a project of Nussinov's Algorithm.
If you want to access this project, go to the directory of `nussinov`

```
cd nussinov
```

## Installation
You can install all the dependencies by

```
pip install -r requirements.txt
```

## Execution

If you want to run nussinov's Algorithm you can go to the nussinov directory and simply run:

```python
python main.py --seq [target sequence] --output [file location of output image] --min_loop_length [min loop length] --score_metrics_file [the file of score metrics]
```

For example, If you execute,

```python
python main.py --seq CGAGUCGGAGUC --output demo/demo1.png --min_loop_length 0
```

Note: If you don't specify the scoring metrics, we will use {(A, C): 1, (C, G): 1} as a default.

You will get the following output:

![Alt text](nussinov/demo/demo1.png)

### Score Metrics Format
The Score metrics use the following format:

[First Nucleotide] [Second Nucleotide] [Weight]

You can see an example in `nussinov/score_metrics/score_1.txt`. In this example, we let (A, C) with the weight 1, (C, G) with the weight 1, and (A, G) with the weight 100.

```
A U 1
C G 1
A G 100
```

And we can use `score_metrics_file` option to change the score_metrics.

For example, we can use:

```
python main.py --seq ACUG --ouput demo/demo2.png --min_loop_length 0 --score_metrics_file score_metrics/score_1.txt
```

And you will get the following output:
![Alt text](nussinov/demo/demo2.png)

### Read Extreme Large Sequence file

If you want to read a super long sequence, it might be more convenient to store the input in a file. In that case, you can use `seq_file` option.

For example, you can run store your input in seq/seq1.txt and then execute:

```python
python main.py --seq_file seq/seq1.txt --min_loop_length 1 --output demo/demo3.png
```

And the output will be:
![Alt text](nussinov/demo/demo3.png)




