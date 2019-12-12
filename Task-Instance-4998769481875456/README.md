# Ansible-Role: To add a New User
## Workflow of Ansible-Playbook:
In the tasks section we have `"Create a New User"` it uses Ansible's `user` module to carry out the <br>
process of adding new user.
<br><br>
The `"Create a New User"` task requires `{name,password,groups}` to create a new user.
<br><br>
These details are povided by following code:
```
      with_items:
               - { name: gci-2019, password: "1234", groups: "" }
```
## To Add Users:
For this you need to modify the above mentioned section of code `with_items:`.<br>
You need to follow this pattern to add new entries:
```
      with_items:
               - { name: user1, password: "pass1", groups: "group names or leave empty" }
               - { name: user2, password: "pass2", groups: "group names or leave empty" }
               - { name: user3, password: "pass3", groups: "group names or leave empty" }
                 .
                 .
               - { name: userN, password: "passN", groups: "group names or leave empty" }
```
### Note:- Here, N is number of different users.
## Steps to Run the Playbook:
1. Some Usual Modifications:
   * Change `hosts: localhost` to `hosts: <hostname>` and remove `connection: local` if you don't want to run Playbook locally.
   * Change `remote_user: utx10101` to `remote_user: <your_current_logged_in_user>`.
2. Execute following command with <your_current_logged_in_user>:
```
$ ansible-playbook -K GCI-Create-User-Ansible.yml
```
Note:- `-K` Flag here will let you enter `BECOME password` which is your `sudo user password`.
### This Playbook was created by UTx10101 to Complete a GCI-2019 task by Fedora : [Here](https://codein.withgoogle.com/dashboard/task-instances/4998769481875456/)
