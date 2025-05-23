import os
from pathlib import Path
import logging

logging.basicConfig(level=logging. INFO, format='[%(asctime)s]:%(message)s:')

project_name = "cnnClassifier"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/configuration/__init.py",
    f"src/{project_name}/configuration/azure_blob.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "requirements.txt", 
    "setup.py", 
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0 ):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creatting empty file: {filename}")
    else:
        logging.info(f"{filename} is already exists")