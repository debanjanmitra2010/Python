# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper_fn(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print("Validity failed. Message not sent")
    return wrapper_fn


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
