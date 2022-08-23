import os
import shutil
import random
import numpy as np
import argparse

#init argparse and take some arguments
parser=argparse.ArgumentParser(description="A random sampling script. Move n random files from the lowest subdirectories of a source location to the destination directory. Folders for each label are also created in the dest directory.")

parser.add_argument("src", help="source directory")
parser.add_argument("dest", help="destination directory")
parser.add_argument("n", type=int, help="samples per folder")
parser.add_argument("-s", "--seed", type=int, help="random seed")
parser.add_argument("-e", "--exclude", action="append", help="exclude a list of folders from being sampled")
parser.add_argument("-d", "--debug", action='store_true', help="toggle for debugging")
parser.add_argument("--no_folders", action='store_false' , help="toggle for folder creation in destination")


args=parser.parse_args()

#store to variables
source_dir=args.src
dest_dir=args.dest
n=args.n
seed=args.seed
exclude_list=args.exclude
create_folders=args.no_folders
debug=args.debug

#for debugging only
if debug:
    print(f"source:{source_dir}")
    print(f"dest:{dest_dir}")
    print(f"samples:{n}")
    print(f"seed:{seed}")
    print(f"exclude list:{exclude_list}")
    print(f"create folders:{create_folders}")

#set random seed
if seed:
    print(f"Setting random seed to {seed}...")
    random.seed(seed)
    np.random.seed(seed)

k=0
for i, (dirs, subdirs, files) in enumerate(os.walk(source_dir)):            
    if dirs is not source_dir:
            category = dirs.split("\\")[-1] #get last element in list 
            print(f"Category: {category}")  
            
            #exclude from sampling if in exclude_list
            if exclude_list is not None:
                if category in exclude_list:
                    continue
            
            #create folders
            if create_folders:
                new_folder=os.path.join(dest_dir,category)
                #ensure folder doesn't exist
                if not os.path.isdir(new_folder):
                    print(f"Creating folder {category}")
                    os.mkdir(new_folder)
            
            #pick n random samples
            print(f"Random sampling {n} files")
            rand_files=random.sample(files,n)
            
            for l in range(n):
                file_path=os.path.join(dirs, rand_files[l])
                #use created folder
                if create_folders:
                    shutil.copy(file_path, new_folder)
                else:
                    shutil.copy(file_path, dest_dir)
                
                k+=1
                print(f"Copied: {file_path}; labels: {i}; files sampled: {k}")
                
            
                
            
            

    
    
    






