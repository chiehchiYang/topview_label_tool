# topview_label_tool
A tool to label object position in Carla world coordinate.


## install 
```bash
conda create -n label python=3.7
conda activate label

# install package
conda  install pyqt
pip install opencv-python-headless

pip install scipy
```

---

- example_lbc_collect_data : 
Using "Learning by cheating" camera setting to collect the topdown view image.

- Label_crosswalk_tool :
Using PyQt to find the object Position in carla coordinate. 

## Usage ( How to run the label_tool_program )

```
cd Label_crosswalk_tool 

# run
python main.py
```

## Label pipeline

1. Use **left click** to select point
2. After collect **4** points
3. Use right click to check the area
4. If the area is ok, then save points




