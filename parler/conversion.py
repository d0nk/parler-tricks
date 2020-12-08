
class ConversionAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def convert(self, _type, uuid):
        '''
        GET /v3/idConversion/{type}/{uuid}
        params:
            type: one of (user, post, comment, image, video, link)
            uuid: public-facing UUID of the entity
        response:
            hidden sequential ID, as protobuf varint
        rate-limit: none
        auth: yes
        '''
        return self.s.get(
            "{}/v3/idConversion/{}/{}".format(self.root_url, _type, uuid)
        )

    def reverse_convert(self, _type, _id):
        '''
        GET /v3/uuidConversion/{type}/{id}
            (*) this is enumerable
        params:
            type: one of (user, post, comment, image, video, link)
            id: hidden, sequential ID
        response:
            public-facing UUID of the entity
        rate-limit: none
        auth: yes
        '''
        return self.s.get(
            "{}/v3/uuidConversion/{}/{}".format(self.root_url, _type, _id)
        )