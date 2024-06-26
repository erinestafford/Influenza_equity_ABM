#!/bin/bash

source /app/lmod/lmod/init/profile
ml Python/3.9.5-GCCcore-10.3.0
sbatch --array=1 -n 1 -c 1  --time 20-0:0:0 --job-name=$i --wrap="python five_mil_ex.py" --output=results/res_slurm/%A_%a.txt
