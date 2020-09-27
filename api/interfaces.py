import zope.interface


class IApi(zope.interface.Interface):
    url = zope.interface.Attribute("""API url""")

    def get_info(self, *args, **kwargs) -> str:
        """Get info from API"""
