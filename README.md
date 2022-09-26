Edit the class labels of YOLO annotation files. 

### Requirements
1. Python 3

### Usage
```bash
python3 main.py --path <path to the folder containing annotations> --search <label to change> --replace <label to be changed with>
```

E.g.
```bash
python3 main.py -p /Users/user/Downloads/dataset -s 0 -r 10
```
