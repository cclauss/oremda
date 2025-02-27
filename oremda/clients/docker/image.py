from oremda.clients.base import ImageBase


class DockerImage(ImageBase):
    def __init__(self, client, name):
        self.client = client
        self.image = client.images.get(name)

    @property
    def raw_labels(self):
        return self.image.labels
