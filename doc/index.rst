About
=====

Websockets in the `Mys programming language`_.

Project: https://github.com/mys-lang/package-websocket

Examples
========

.. code-block:: python

   from websocket.client import Client

   def main():
       client = Client()
       client.connect("ws://localhost:20000")
       self.websocket.send_text("Hello!")
       print(self.websocket.receive_text())
       connect.disconnect()

Functions and types
===================

Client side
-----------

.. mysfile:: src/client.mys

Server side
-----------

.. _Mys programming language: https://mys.readthedocs.io/en/latest/
