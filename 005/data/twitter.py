import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

consumer_key = '7afhFQjDvlhPYlRn93GnA8jeV'
consumer_secret = 'xgsaWTZ7Px7e32T0mnWFUaSUDQ8pjYTmG3Qab8GVU6Tro7f2MO'
access_token = '268456887-4kiBfTRLbLqWJSriyXAGAQeAf4QwDerjdtEYKfMb'
access_secret = 'D8z3zy6ZuW0DduOHcAPJiHcsFRWZqZCKdjniN5CDEodGE'

class TweetsListener(StreamListener):

    def __init__(self, client_socket):
        self.client_socket = client_socket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(data.encode('utf-8'))
            return True
        except BaseException as e:
            print('Error on_data: %s' % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def send_data(c_socket, track):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=track)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--track', nargs='+', default=['trump'], help='topics to track')
    parser.add_argument('--host', default='127.0.0.1', help='local machine name')
    parser.add_argument('--port', type=int, default=4455, help='listen to the port')

    args = parser.parse_args()

    s = socket.socket()              # Create a socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((args.host, args.port))   # Bind to the port

    print('Listening on: %s:%s' % (args.host, args.port))

    s.listen(5)                 # Now wait for client connection.
    client_socket, host_port = s.accept()        # Establish connection with client.

    print('Received request from: %s:%s' % host_port)

    send_data(client_socket, track=args.track)
