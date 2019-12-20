# Ansible-Role: To Fix Heart Bleed Bug
`gci-utx10101.heartbleedfix` is the folder for Ansible-Role<br>
`GCI-Fix-HeartBleed.yml` is a sample playbook to make use of above Ansible-Role

## Steps to Setup:
(Keep The `gci-utx10101.users` as it is without any changes.)<br>
Create a new playbook (By following the demo `GCI-Fix-HeartBleed.yml`) in the same directory as `gci-utx10101.users` or modify `GCI-Fix-HeartBleed.yml`:
1. Some Usual Modifications:
   * Change `hosts: localhost` to `hosts: <hostname>` and remove `connection: local` if you don't want to run Playbook locally.
   * Change `remote_user: utx10101` to `remote_user: <your_current_logged_in_user>`.
2. Execute following command with <your_current_logged_in_user>:
```
$ ansible-playbook -K GCI-Fix-HeartBleed.yml
```
Note:- `-K` Flag here will let you enter `BECOME password` which is your `sudo user password`.
### This Ansible-Role and Playbook was created by UTx10101 to Complete a GCI-2019 task by Fedora : [Here](https://codein.withgoogle.com/dashboard/task-instances/5311751625637888/)
