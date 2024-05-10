import base64

class Base64:

    @staticmethod
    def encode(data):
        data_bytes = data.encode('utf-8')
        encoded_data = base64.urlsafe_b64encode(data_bytes)
        return encoded_data.decode('utf-8')

    @staticmethod
    def decode(data):
        data_bytes = base64.urlsafe_b64decode(data)
        decoded_data = data_bytes.decode('utf-8')
        return decoded_data
