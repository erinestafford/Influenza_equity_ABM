#!/bin/bash

source /app/lmod/lmod/init/profile
ml Python/3.9.5-GCCcore-10.3.0
sbatch --array=1-100 -n 1 -c 1  --time 14-0:00 --job-name=$i --wrap="python cs_swp_sim.py" --output=results/res_slurm/%A_%a.txt
