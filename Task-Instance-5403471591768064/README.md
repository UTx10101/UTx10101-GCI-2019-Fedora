# Ansible Playbook to Automate Installation of TensorFlow on ArchLinux
### What's TensorFlow ?
TensorFlow is the most popular & open source library for Machine Learning which is actively developed by Google.

### Dependencies of this Playbook:-
  1. `ansible`
  2. `pacman` Package Manager
  3. `pip`
  4. `python >=v3.5`
  5. Or you can use `Arch Linux` with dependencies (1,3 and 4).
### Why didn't I just used pip install ?
As this Playbook was made for Arch Linux, pip install tensorflow gives `No Distribution Found Error` as pip packages of tensorflow currently support Ubuntu 16.04+.
To tackle this we first install tensorflow and python-tensorflow with dependencies using `pacman` and then run pip install to get unmet dependencies like `opt_einsum`.

**| This playbook was created by UTx10101. For the GCI-2019 task by Fedora. |**
