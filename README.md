# <div align="center">AI in Animation: Custom Trainable YOLO Based Real-Time Character Recognition in Animations</div>

<div align="center">

Solo Final Project relevant to pattern recognition and neural networks - reimplementation of YOLO v5 in Animation, which is an attempt never made before.

The code is powered by YOLOv5 from ultralytics.

  <p>
    <a align="center" href="https://ultralytics.com/yolov5" target="_blank">
      <img width="850" src="https://raw.githubusercontent.com/ultralytics/assets/master/yolov5/v70/splash.png"></a>
  </p>
</div>

## <div align="center">Table of Contents</div>
- [What's included](#tree)
- [Documentation](#docs)
- [Git workflow](#workflow)
- [License](#license)

## <div align="center"><a name="tree"></a> What's included</div>

```text
ece-5831-project/
├── docs/
│   └── DEVELOPER.md  
├── src/
│   ├── classfy/
│   ├── models/
│   ├── segment/
│   ├── utils/
│   └── train.py        // python script for training the model
└── README.md
```

## <div align="center"><a name="docs"></a>Documentation</div>

See the [docs folder](https://https://github.com/UMich-jihohan/ece-5831-project/docs) for full documentation.

<!-- <details open>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

</details> -->

## <div align="center"><a name="workflow"></a> Git Workflow</div>
The core idea behind the Feature Branch Workflow is that all feature development should take place in a dedicated branch instead of the master branch. This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the main codebase. It also means the master branch will never contain broken code, which is a huge advantage for continuous integration environments.

#### release
This branch contains the machine problems from the semester, as well as any other code examples staff members want to send to the students.

### Main Branches
* master
* release

#### master
This branch is the branch where all the development takes place. When the source code in the develop branch reaches a stable point and is ready to be released, all of the changes should be merged back into master somehow and then tagged with a release number. How this is done in detail will be discussed further on.

#### release
This is the main branch where the source code of HEAD always reflects a production-ready state. I consider this branch to be the main branch where the source code of HEAD always reflects a state with the latest delivered development changes for the next release. Some would call this the “integration branch”.

### Feature Branches
* feature
* hotfix

#### feature
Feature branches (or sometimes called topic branches) are used to develop new features for the upcoming or a distant future release. When starting development of a feature, the target release in which this feature will be incorporated may well be unknown at that point. The essence of a feature branch is that it exists as long as the feature is in development, but will eventually be merged back into develop (to definitely add the new feature to the upcoming release) or discarded (in case of a disappointing experiment).

Feature branches typically exist in developer repos only, not in origin.

#### hotfix
Hotfix branches are very much like release branches in that they are also meant to prepare for a new production release, albeit unplanned. They arise from the necessity to act immediately upon an undesired state of a live production version. When a critical bug in a production version must be resolved immediately, a hotfix branch may be branched off from the corresponding tag on the master branch that marks the production version.

The essence is that work of team members (on the develop branch) can continue, while another person is preparing a quick production fix.

----------

## <div align="center"><a name="license"></a>License</div>
Even though the project is not planned to be used for commercial product, as it uses YOLOv5, this project is also under the GPL-3.0 License. See [LICENSE](https://github.com/UMich-jihohan/ece-5831-project/blob/master/LICENSE) file for details.
