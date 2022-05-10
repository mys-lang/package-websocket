|discord|_
|test|_
|stars|_

About
=====

Websockets in the `Mys programming language`_.

Project: https://github.com/mys-lang/package-websocket

Examples
========

Client side
-----------

.. code-block:: mys

   from websocket.client import Client

   func main():
       client = Client()
       client.connect("localhost", 20000)
       client.send_text("Hello!")
       print(client.receive_text())
       client.disconnect()

Server side
-----------

.. warning:: Server side websockets are not yet implemented!

.. code-block:: mys

   from websocket.server import Server

   func main():
       server = Server()
       server.listen(20000)

       while True:
           client = server.accept()
           message = client.receive_text()
           print(f"Got: {message}")
           client.send_text(f"Message: '{message}'")

API
===

Client side
-----------

.. mysfile:: src/client.mys

Server side
-----------

.. warning:: Server side websockets are not yet implemented!

.. mysfile:: src/server.mys

.. |discord| image:: https://img.shields.io/discord/777073391320170507?label=Discord&logo=discord&logoColor=white
.. _discord: https://discord.gg/GFDN7JvWKS

.. |test| image:: https://github.com/mys-lang/package-websocket/actions/workflows/pythonpackage.yml/badge.svg
.. _test: https://github.com/mys-lang/package-websocket/actions/workflows/pythonpackage.yml

.. |stars| image:: https://img.shields.io/github/stars/mys-lang/package-websocket?style=social
.. _stars: https://github.com/mys-lang/package-websocket

.. _Mys programming language: https://mys-lang.org
