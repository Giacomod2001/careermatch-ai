import glob
import os

test_files = glob.glob("test_*.py") + ["verify_mining.py"]

for file in test_files:
    if not os.path.exists(file):
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if we already have the shared_core path
    if "'shared_core'" in content or '"shared_core"' in content:
        continue
        
    # Replace sys.path.insert
    import re
    new_content = re.sub(
        r'sys\.path\.insert\(0, os\.path\.dirname\(os\.path\.abspath\(__file__\)\)\)',
        r'sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "shared_core"))\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))',
        content
    )
    
    # For files that might not have the sys.path.insert (like verify_mining.py)
    if "sys.path.insert" not in content and "import ml_utils" in content:
        new_content = "import sys\nimport os\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shared_core'))\n" + new_content
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Updated test paths!")
