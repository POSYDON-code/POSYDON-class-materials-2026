#!/bin/bash
#SBATCH --job-name=1e+00_popsyn
#SBATCH --output=./1e+00_logs/popsyn_%A_%a.out
#SBATCH --time=14:00:00
#SBATCH --cpus-per-task=4
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=8GB
#SBATCH --account=jeffrey.andrews
#SBATCH --partition=hpg-default
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=kasdaglie@ufl.edu
export PATH_TO_POSYDON=/home/kasdaglie/blue/kasdaglie/POSYDON
export PATH_TO_POSYDON_DATA=/home/kasdaglie/blue/kasdaglie/
srun python ./pop_run.py