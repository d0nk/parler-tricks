
class ContactsUploaderAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    '''
    {
        "contactsList": [{
            "firstName": "",
            "email": "",
            "lastName": "",
            "phone": ""
        }]
    }
    '''
    def start_uploading(self, *args, **kwargs):
        return self.s.post("{}/v2/contacts".format(self.root_url), *args, **kwargs)