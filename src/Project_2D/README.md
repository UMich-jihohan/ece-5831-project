## <div align="center">How to use</div>

<!-- ```bash
git clone https://github.com/UMich-jihohan/ece-5831-project.git  # clone
cd ece-5831-project/src
pip install -r requirements.txt  # install
``` -->
<details open>
<summary>Download and prepare the dataset</summary>

Download the dataset (.Zip file) used for this project as a single through [UMich Google Drive](https://drive.google.com/file/d/17VLmkYnNJ6AFLT9TUk-1HGiqZgtp4-t2/view?usp=share).
This can be accessed through UMich account.
Once downloaded, move the `2D - Pororo` folder into `src/Project_3D/data`, and rename the folder as `Pororo`, as not having space in the file/folder name makes the command more concise.

</details>

<details open>
<summary>Split the dataset</summary>

Use Pororo.py to split the data.
```bash
cd Project_3D
python Pororo.py
```

</details>

<details close>

<summary>Prepare the configuration file</summary>

The configuration file is prepared as `dataset.yaml`, but make sure to edit this when you are changing the dataset or file directory.

</details>

<details open>

<summary>Train using YOLOv5</summary>

```bash
python train.py --img 640 --batch 16 --epochs 100 --data dataset.yaml --weights yolov5s.pt
```

</details>
