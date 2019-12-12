# Ansible-Role: To add a New User
`gci-utx10101.users` is the folder for Ansible-Role<br>
`GCI-Create-User-Ansible.yml` is a sample playbook to make use of above Ansible-Role
## To Add Users:
For this you need to modify the vars section in `GCI-Create-User-Ansible.yml`.<br>
You need to follow this pattern to add new entries:
[See Entry Pattern Here](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-4998769481875456/gci-utx10101.users/defaults/main.yml)<br>
An example is already present in `GCI-Create-User-Ansible.yml`.

## Steps to Setup:
(Keep The `gci-utx10101.users` as it is without any changes.)<br>
Create a new playbook or modify existing one in the same directory as `gci-utx10101.users`:
1. Some Usual Modifications:
   * Change `hosts: localhost` to `hosts: <hostname>` and remove `connection: local` if you don't want to run Playbook locally.
   * Change `remote_user: utx10101` to `remote_user: <your_current_logged_in_user>`.
2. Execute following command with <your_current_logged_in_user>:
```
$ ansible-playbook -K GCI-Create-User-Ansible.yml
```
Note:- `-K` Flag here will let you enter `BECOME password` which is your `sudo user password`.
### This Ansible-Role and Playbook was created by UTx10101 to Complete a GCI-2019 task by Fedora : [Here](https://codein.withgoogle.com/dashboard/task-instances/4998769481875456/)
