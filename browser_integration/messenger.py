import json
import logging
import struct
import sys


class Messenger(object):
    def getMessage(self,):
        buffer = sys.stdin
        if hasattr(buffer, "buffer"):
            buffer = buffer.buffer

        logging.debug("Buffer initialized")
        rawLength = buffer.read(4)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack("@I", rawLength)[0]
        message = buffer.read(messageLength)
        logging.debug("Message readed")
        return json.loads(message)

    def sendMessage(self, message):
        encodedContent = json.dumps(message).encode("utf-8")
        encodedLength = struct.pack("@I", len(encodedContent))

        buffer = sys.stdout
        if hasattr(buffer, "buffer"):
            buffer = buffer.buffer
        buffer.write(encodedLength)
        buffer.write(encodedContent)
        buffer.flush()
        logging.debug("Message sended: " + json.dumps(message))
