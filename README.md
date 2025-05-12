## Beaufoy Archive
Beaufoy London Diamondway  Buddhist Center photo / video archive project

- [Todo](#todo)
- [Dependencies](#dependencies)
- [Status](#status)
- [Transcribe](#transcribe)
- [Pytorch](#pytorch)
- [Changelog](#changelog)

### Todo
* Link tailscale on main box to archive gmail
* Link apple id on main box to archive gmail
* Link tailscale on Kitsu VM to archive gmail
* Backup system drive as image
* Backup system drive as TimeMachine
* Copy achive_vol004 local to external drive
* Send copy of achive_vol004 to Hubert (Gdansk Anniversary?)
* Update to MacOS Ventura (?)
* Create Naxtcloud / Memories on old MacMini
* Create and check fields interpolation based on flownet5
* Create, train and check DV / VHS to 2k upscaler including artefacts removal

### Dependencies
* Gmail
* Tailscale

### Status

### Transcribe

Transcribe is based on transcribe-anything v2.4.0 and custom direcrtory walkthrough script. It is using "medium" model by default and cpu backend due to lack of mps support on Intel-baseed Macs.

* Activate transcribe python environment 

```bash
eval "$(~/miniconda3/bin/conda shell.bash hook)"
conda activate transcribe
```

### Pytorch

Install latest pytorch officially avaliable for Intel Macs (2.2.2) with mps backend.

```bash
eval "$(~/miniconda3/bin/conda shell.bash hook)"
conda create -n torch-mps -c conda-forge python=3.10
conda activate torch-mps
conda install numpy=1.21 mkl=2021.4.0
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 -c pytorch
```

MPS backend seem to work faster with simple CNN

```bash
(torch-mps) archive@Archive mps-test % python mps_test.py                              
Device: cpu | Time per forward pass: 19.2168 seconds
Device: mps | Time per forward pass: 3.4896 seconds
```

### Changelog

* [2025/05/08] Transcribe anvironment created, transcribe process started on local copy of archive_vol004.
* [2025/05/11] Pytorch with MPS backend installed and tested.
* [2025/05/12] archive.beaufoy@gmail.com mail address created.


