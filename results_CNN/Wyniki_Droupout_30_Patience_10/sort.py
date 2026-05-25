import shutil
from pathlib import Path

def sort_files_by_suffix(directory_path):
    base_dir = Path(directory_path)
    accuracy_folder = base_dir / "Accuracy"
    loss_folder = base_dir / "Loss"
    accuracy_folder.mkdir(exist_ok=True)
    loss_folder.mkdir(exist_ok=True)

    for file_path in base_dir.iterdir():
        if file_path.is_file():
            
            # .stem gets the filename without the extension (e.g., "my_model_loss")
            file_name = file_path.stem.lower()
            
            # Check the end of the filename and move accordingly
            if file_name.endswith("accuracy") or file_name.endswith("accuracy"):
                destination = accuracy_folder / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"Moved: {file_path.name} -> {accuracy_folder.name}/")
                
            elif file_name.endswith("loss"):
                destination = loss_folder / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"Moved: {file_path.name} -> {loss_folder.name}/")

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

sort_files_by_suffix(dir_path)