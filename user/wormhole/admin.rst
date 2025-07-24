Admin
=====

Bellow you can find documentation for wormhole administrators and bot owners. 

How to set up wormhole on a guild
---------------------------------

This section is aimed to guild owners who want to add bot using this module to their guild. First add the bot to your guild. Then please check if the bot has permission to manage it's future channel. Last please select a wormhole channel with command ``wormhole channel set``. Optionally you can set up guild log channel described in :doc:`../base/admin/logging`.

Application emojis
------------------

You can create special custom emojis to replace guild names in messages. These custom emojis are stored as application emojis and they can be uploaded in `discord developer portal <https://discord.com/developers/applications>`_. The name of each emoji should match the guild's name, converted to lowercase, with spaces converted to ``'_'``, ASCII characters only (if applicable). For the guild ``ČVUT FEL``, the corresponding emoji should be named ``cvut_fel``.

Command overview
----------------

.. admonition:: wormhole ...

    */command, administrator=True*

    A group of configuration commands for the wormhole.

.. admonition:: wormhole channel ...

    */command, administrator=True*

    A group of commands for wormhole channels.

.. admonition:: wormhole channel set <channel>

    */command, administrator=True, default ACLevel: GUILD_OWNER*

    Register a channel as a wormhole. All messages in this channel will be deleted and mirrored to all other wormhole channels. The command will let you choose the ``channel``.

.. admonition:: wormhole channel remove <channel>

    */command, administrator=True, default ACLevel: GUILD_OWNER*

    Unregister a channel from the wormhole. The command will let you choose the ``channel``.

.. admonition:: wormhole slowmode ...

    */command, administrator=True*

    A group of commands for wormhole channels slow mode.

.. admonition:: wormhole slowmode set <time>

    */command, administrator=True, default ACLevel: BOT_OWNER*

    Apply slow mode to all wormhole channels. ``time`` is integer in seconds.

.. admonition:: wormhole slowmode remove

    */command, administrator=True, default ACLevel: BOT_OWNER*

    Disable slow mode in all wormhole channels.

    .. note::
    
        It is equivalent to ``wormhole slowmode set 0``

