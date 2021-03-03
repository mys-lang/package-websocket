About
=====

Websockets in the `Mys programming language`_.

Project: https://github.com/mys-lang/package-websocket

Examples
========

Client side
-----------

.. code-block:: python

   from websocket.client import Client

   def main():
       client = Client()
       client.connect("localhost", 20000)
       self.websocket.send_text("Hello!")
       print(self.websocket.receive_text())
       connect.disconnect()

Server side
-----------

.. code-block:: python

   from websocket.server import Server

   def main():
       server = Server()
       server.listen(20000)

       while True:
           client = server.accept()
           message = client.receive_text()
           print(f"Got: {message}")
           client.send_text(f"Message: '{message}'")

Functions and types
===================

Client side
-----------

.. mysfile:: src/client.mys

Server side
-----------

.. mysfile:: src/server.mys

.. _Mys programming language: https://mys.readthedocs.io/en/latest/
