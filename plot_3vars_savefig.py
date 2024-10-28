"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot, and saves it to a file named "myplot.png"

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "MFLOPSplot.png"

fname = "sum_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

mflops_code1 = [problem_sizes[i]/(code1_time[i] * 1e6) for i in range(len(problem_sizes))]
mflops_code2 = [problem_sizes[i]/(code2_time[i] * 1e6) for i in range(len(problem_sizes))]
mflops_code3 = [problem_sizes[i]/(code3_time[i] * 1e6) for i in range(len(problem_sizes))]

plt.figure()

plt.title("MFLOPS Comparison of 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(mflops_code1, "r-o", label='Direct Sum')
plt.plot(mflops_code2, "b-x", label= 'Vector Sum')
plt.plot(mflops_code3, "g-^", label='Indirect Sum')

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOPS")


plt.legend( loc="best")

plt.grid(axis='both')

# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)


plt.show()

# EOF
