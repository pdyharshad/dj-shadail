from django.db import models


class MessageType(models.Model):
    msg_type = models.CharField(max_length=200)
    src = models.CharField('Source file path from static folder',
            max_length=200)
    alt = models.CharField('Alternative text for image',
            max_length=200)
    caption_h3 = models.CharField('Caption header in caursel img',
            max_length=200)
    caption_p = models.CharField('Caption Para in Caurosel img',
            max_length=200)

    def __str__(self):
        return self.msg_type


class Message(models.Model):
    message = models.CharField(max_length=200)
    message_type = models.ForeignKey(MessageType, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
