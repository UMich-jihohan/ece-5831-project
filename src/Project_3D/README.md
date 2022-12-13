## <div align="center">How to use</div>

<details open>
<summary>Download the dataset</summary>

Download the dataset (.Zip file) used for this project as a single through [UMich Google Drive](https://drive.google.com/file/d/17VLmkYnNJ6AFLT9TUk-1HGiqZgtp4-t2/view?usp=share).
This can be accessed through UMich account.
Once downloaded, move the `3D - Howl` folder into `src/Project_2D/data`, and rename the folder as `Howl`, as not having space in the file/folder name makes the command more concise.

</details>

<details open>
<summary>Split the dataset</summary>

Use Howl.py to split the data.
```bash
cd Project_3D
python Howl.py
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

<summary>Test the trained YOLOv5 model</summary>

```bash
python detect.py -weights runs\train\exp\weights\best.pt --conf 0.7 --source \path\to\video
```

Note that the directory `exp\` is subject to change based on how many runs you've made so far.

</details>