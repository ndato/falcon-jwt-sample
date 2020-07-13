def cred_checker(cred):
    """
        Check Adapter Credentials if valid.

            Parameters:
                cred (dict): Supplied Account Credentials to check.
                Expected format of the dictionary is as follows:
                {
                    "username": <Username Credentials>,
                    "password": <Password Credentials>
                }

            Returns:
                cred (dict or None): Passes the Credentials if
                    valid. Returns None if not.
    """

    # Return None if credentials is None
    if cred is None:
        return None

    # The credentials is under the "user" key if it is decoded from
    # a JWT token. This handles that issue.
    if "user" in cred.keys():
        cred = cred["user"]

    # Return None if there is no username provided in credentials
    if "username" not in cred.keys():
        return None

    # Check Adapter Credentials are correct
    if cred['username'] == 'Username' and cred.get('password', '') == '':
        return cred

    return None
