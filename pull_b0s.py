import argparse
import nibabel as nib
import numpy as np
from dipy.io import read_bvals_bvecs
import subprocess
import os

# argparse arguments
parser = argparse.ArgumentParser(description='Eddymotion Implementation')

parser.add_argument("--input_dir", help="Flag for defining input directory")
parser.add_argument("--output_dir", help="Flag for defining output directory")
args = parser.parse_args()

input_dir = args.input_dir
output_dir = args.output_dir

# file paths
bval_path = f'{input_dir}/dwi.bval'
bvec_path = f'{input_dir}/dwi.bvec'
nii_path = f'{input_dir}/dwi.nii.gz'

# import bval/bvecs/nifti files
bval,bvec = read_bvals_bvecs(bval_path, bvec_path)

img = nib.load(nii_path)
nii = img.get_fdata()

# identify + extract b0s and save synb0 output for each b0
b_count = 0 
for i in range(len(bval)):
    if bval[i] == 0 or bval[i] == 1:
        b_count = b_count + 1
        print(f'\n [[b0 #{b_count} identified]]')

        nii_b0 = nii[:,:,:,i:i+1]
        b0 = nib.Nifti1Image(nii_b0, affine=img.affine, header=img.header)
        nib.save(b0, f'{output_dir}/b0_{b_count}.nii.gz')
print(" ")