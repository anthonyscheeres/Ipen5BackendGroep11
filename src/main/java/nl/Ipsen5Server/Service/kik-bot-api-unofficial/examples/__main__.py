"""
A Kik bot that just logs every event that it gets (new message, message read, etc.),
and echos back whatever chat messages it receives.
"""
import os
from .kik_unofficial.datatypes.xmpp import chatting as chatting
from .kik_unofficial.client import KikClient
from .kik_unofficial.callbacks import KikClientCallback
from .kik_unofficial.datatypes.xmpp.errors import SignUpError, LoginError
from .kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse, PeersInfoResponse
from .kik_unofficial.datatypes.xmpp.sign_up import RegisterResponse, UsernameUniquenessResponse
from .kik_unofficial.datatypes.xmpp.login import LoginResponse, ConnectionFailedResponse

username = 'CKMOfficial'
password = 'HeleGoeieWachtwoord'
cur_path = os.path.dirname(os.path.abspath(__file__))

def main():
    bot = EchoBot()

def getUsers():
    print("current path: ", cur_path)
    f = cur_path.split("\\")
    print("f is ", f)
    f.remove(f.__getitem__(len(f)-1))
    f.remove(f.__getitem__(len(f)-1))
    url = ""
    for i in f:
        if url == "":
            url1 = i
        else:
            url1 = url + "\\" + i
        url = url1
    path = url + "\\users.txt"

    return open(path, "r").read().replace("[", "").replace("]", "").split(",")

def getMessage():
    print("current path: ", cur_path)
    f = cur_path.split("\\")
    f.remove(f.__getitem__(len(f)-1))
    f.remove(f.__getitem__(len(f)-1))
    url = ""
    for i in f:
        if url == "":
            url1 = i
        else:
            url1 = url + "\\" + i
        url = url1
    path = url + "\\message.txt"
    return open(path, "r").read()

class EchoBot(KikClientCallback):
    def __init__(self):
        self.client = KikClient(self, username, password)

    def on_authenticated(self):
        print("Now I'm ready to send a message")
        for i in getUsers():
            self.client.send_chat_message(self.client.get_jid(i.replace(" ", "")), getMessage())
        self.client.disconnect()


    def on_login_ended(self, response: LoginResponse):
        print("Full name: {} {}".format(response.first_name, response.last_name))

    def on_chat_message_received(self, chat_message: chatting.IncomingChatMessage):
        print("[+] '{}' says: {}".format(chat_message.from_jid, chat_message.body))
        print("[+] Replaying.")
        self.client.send_chat_message(chat_message.from_jid, "You said \"" + chat_message.body + "\"!")

    def on_message_delivered(self, response: chatting.IncomingMessageDeliveredEvent):
        print("[+] Chat message with ID {} is delivered.".format(response.message_id))

    def on_message_read(self, response: chatting.IncomingMessageReadEvent):
        print("[+] Human has read the message with ID {}.".format(response.message_id))

    def on_group_message_received(self, chat_message: chatting.IncomingGroupChatMessage):
        print("[+] '{}' from group ID {} says: {}".format(chat_message.from_jid, chat_message.group_jid,
                                                          chat_message.body))

    def on_is_typing_event_received(self, response: chatting.IncomingIsTypingEvent):
        print("[+] {} is now {}typing.".format(response.from_jid, "not " if not response.is_typing else ""))

    def on_group_is_typing_event_received(self, response: chatting.IncomingGroupIsTypingEvent):
        print("[+] {} is now {}typing in group {}".format(response.from_jid, "not " if not response.is_typing else "",
                                                          response.group_jid))

    def on_roster_received(self, response: FetchRosterResponse):
        print("[+] Chat partners:\n" + '\n'.join([str(member) for member in response.peers]))

    def on_friend_attribution(self, response: chatting.IncomingFriendAttribution):
        print("[+] Friend attribution request from " + response.referrer_jid)

    def on_image_received(self, image_message: chatting.IncomingImageMessage):
        print("[+] Image message was received from {}".format(image_message.from_jid))
    
    def on_peer_info_received(self, response: PeersInfoResponse):
        print("[+] Peer info: " + str(response.users))

    def on_group_status_received(self, response: chatting.IncomingGroupStatus):
        print("[+] Status message in {}: {}".format(response.group_jid, response.status))

    def on_group_receipts_received(self, response: chatting.IncomingGroupReceiptsEvent):
        print("[+] Received receipts in group {}: {}".format(response.group_jid, ",".join(response.receipt_ids)))

    def on_status_message_received(self, response: chatting.IncomingStatusResponse):
        print("[+] Status message from {}: {}".format(response.from_jid, response.status))

    def on_username_uniqueness_received(self, response: UsernameUniquenessResponse):
        print("Is {} a unique username? {}".format(response.username, response.unique))

    def on_sign_up_ended(self, response: RegisterResponse):
        print("[+] Registered as " + response.kik_node)

    # Error handling

    def on_connection_failed(self, response: ConnectionFailedResponse):
        print("[-] Connection failed: " + response.message)

    def on_login_error(self, login_error: LoginError):
        if login_error.is_captcha():
            login_error.solve_captcha_wizard(self.client)

    def on_register_error(self, response: SignUpError):
        print("[-] Register error: {}".format(response.message))


if __name__ == '__main__':
    main()
