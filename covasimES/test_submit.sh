#!/bin/bash

source /app/lmod/lmod/init/profile
ml Python/3.9.5-GCCcore-10.3.0
sbatch --array=1-100 -n 1 -c 12  --time 1 --job-name=$i --wrap="python sim_for_cluster.py" --output=results/res_slurm/%A_%a.txt
