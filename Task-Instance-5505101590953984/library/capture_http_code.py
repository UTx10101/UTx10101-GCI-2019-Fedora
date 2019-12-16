#!/usr/bin/python

DOCUMENTATION = '''
---
module: capture_http_code.py

version_added: "1.0"

description:
    - "This is a module to capture the HTTP status code returned by the server present on the input URL."

options:
    url:
        description:
            - This is the url whose HTTP status code will be captured
        required: true
                
author:
    - Utkrisht Singh Chauhan (@UTx10101)
'''

EXAMPLES = '''
# to capture the status code of https://codein.withgoogle.com/
- name: Capture HTTP status code of `https://codein.withgoogle.com/`
  capture_http_code:
    url: https://codein.withgoogle.com/
'''

from ansible.module_utils.basic import AnsibleModule
import requests as rq

def main():
    module_args = dict(url=dict(type='str', required=True))
    result = dict(
        changed=False,
        failed=False,
        meta=dict(return_code='')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        module.exit_json(**result)
    try:
        r=rq.Session()
        res = r.get(url=module.params['url'], headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})
        result['meta']['return_code'] = res.status_code
        result['changed'] = True
    except:
        result['failed'] = True
    module.exit_json(**result)

if __name__ == '__main__':
    main()
