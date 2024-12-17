++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
README file for Homework 4, Math 471, Fall 2024, J. Chaudhary
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
- This is the README for Homework 4.
- The elements of the hw4 directory are this README and two
  subdirectories: code and report.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
- The subdirectory code contains all of the necessary code for
  this assignment. It includes the following Python scripts:
  
  - check_matvec.py: Verifies the correctness of matrix-vector multiplication.
  - generate_plots.py: Produces various plots for error analysis and parallel performance.
  - hw4_skeleton.py: Contains the main implementation for the finite difference method, using either serial or parallel execution.
  - poisson.py: Generates the sparse CSR matrix containing the finite difference stencil.
  - threads_plots.py: Additional script for plotting threaded performance results.
  - hw4.sh: Shell script for running the necessary scripts on the CARC platform.
  
- To edit any of these files, you can use a text editor such as nano, vim, or emacs.
- To run the primary code for analysis and generate the error plots, execute the following commands in the terminal:
  
  python3 hw4_skeleton.py
  python3 generate_plots.py
  
- These scripts will print relevant output to the terminal and save resulting plots as .png files in the report directory.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
- The subdirectory report contains all of the necessary files for generating the PDF report that includes the assignment results.

- report.tex: The LaTeX source file for the homework report.
- error1.png, error2.png, error3.png: Log-log plots of error vs. grid size for different thread counts.
- local_timings_plot.png, strong_scaling_plot.png, parallel_efficiency_plot.png:
- Plots showing efficiency and timing data for both local machine and CARC performance analysis.
- timings.txt and timingsCarc.txt: Text files with raw timing data from local and CARC runs.
- report.pdf: The compiled PDF of the final report.
- To compile and open the LaTeX report, navigate to the report directory and run the following commands:
- pdflatex report.tex
- open report.pdf
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
