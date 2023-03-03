class ServiceAdapter:
    @property
    def fb_post_auth(self):
        from fb_post.adapters.fb_post_auth_adapter import FbPostAuthAdapter
        return FbPostAuthAdapter()


def get_service_adapter():
    return ServiceAdapter()
