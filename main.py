from util import functions

"""Create a password modifier. Replace the following with the corresponding keys.
i > !
a > @
m > M
B > 8
o > .

Then append "q*s" to the end.

Example: if the input is mypassword, the output is Myp@ssw.rdq*s

hint: Python strings are immutable, but support string concatenation. Store and build the stronger
password in the given password variable.
"""


class User:
    def __init__(self, password):
        self.password = password


if __name__ == '__main__':
    user = User(
        functions.get_password()
    )

    print("\nYour new password is: {}".format(user.password))

