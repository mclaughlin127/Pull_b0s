import argparse
import nibabel as nib
import numpy as np
from dipy.io import read_bvals_bvecs
import os

# argparse arguments
parser = argparse.ArgumentParser(description='For Pulling those b0s')

#parser.add_argument("--input_dir", help="Flag for defining input directory")
parser.add_argument("--output_dir", help="Flag for defining output directory")
parser.add_argument("--nii_path", help="Flag for defining NIFTI file path")
parser.add_argument("--bval_path", help="Flag for defining BVAL file path")
parser.add_argument("--bvec_path", help="Flag for defining BVEC file path")
args = parser.parse_args()

#input_dir = args.input_dir
output_dir = args.output_dir
nii_path = args.nii_path
bval_path = args.bval_path
bvec_path = args.bvec_path

# file paths
#bval_path = f'{input_dir}/*.bval'
#bvec_path = f'{input_dir}/*.bvec'
#nii_path = f'{input_dir}/*.nii.gz'

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
