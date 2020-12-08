class ParlerVideoAPI:
    def __init__(self, session, root_url="http://api.parler.com"):
        self.root_url = root_url
        self.s = session

    def get_current_video_status(self, *args, **kwargs):
        return self.s.get("{}/v2/upload/video/status".format(self.root_url), *args, **kwargs)

    def get_video_processing_status(self, video, *args, **kwargs):
        return self.s.get("{}/v2/upload/video/status/{}".format(self.root_url, video), *args, **kwargs)

    def cancel_video_process(self, video, *args, **kwargs):
        return self.s.delete("{}/v2/upload/video/cancel/{}".format(self.root_url, video), *args, **kwargs)

    def notify_server_of_the_finished_uploaded_video(self, video, *args, **kwargs):
        return self.s.post("{}/v2/upload/video/uploaded/{}".format(self.root_url, video), *args, **kwargs)

    def request_video_upload_url(self, *args, **kwargs):
        return self.s.post("{}/v2/upload/video/new".format(self.root_url), *args, **kwargs)
