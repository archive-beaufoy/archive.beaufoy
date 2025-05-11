## Beaufoy Archive
Beaufoy London Diamondway  Buddhist Center photo / video archive project

- [Todo](#todo)
- [Dependencies](#dependencies)
- [Status](#status)
- [Transcribe](#transcribe)


### Todo
* Create archive.beaufoy gmail mail address
* Link tailscale to archive gmail
* Link apple id to archive gmail
* Backup system drive as image
* Backup system drive as TimeMachine
* Update to MacOS Ventura
* Create Naxtcloud / Memories on old MacMini

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
