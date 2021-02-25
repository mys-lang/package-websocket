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
       client.connect("ws://localhost:8765")

       name = input("What's your name? ")
       client.write_string(name)
       print(f"> {name}")

       greeting = client.read_string()
       print(f"< {greeting}")

       client.disconnect()

Functions and types
===================

Client side
-----------

.. mysfile:: src/client.mys

Server side
-----------

.. mysfile:: src/server.mys

.. _Mys programming language: https://mys.readthedocs.io/en/latest/
