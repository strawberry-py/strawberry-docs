Regular user
============

A wormhole is a virtual bridge between channels and guilds. When a message is sent to one wormhole-enabled channel, it’s automatically forwarded to all others in the same group. It supports 

* regular text messages,
* stickers,
* files,
* forwards and
* replies.

When a message sent to the wormhole channel exceeds the maximum allowed length, it should be divided into multiple smaller messages. The splitting process attempts to break the message at space characters to avoid cutting words in half. Each resulting message is then sent sequentially.
