|test|_

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
       client.send_text("Hello!")
       print(client.receive_text())
       client.disconnect()

Server side
-----------

.. warning:: Server side websockets are not yet implemented!

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

.. warning:: Server side websockets are not yet implemented!

.. mysfile:: src/server.mys

.. |test| image:: https://github.com/mys-lang/package-websocket/actions/workflows/pythonpackage.yml/badge.svg
.. _test: https://github.com/mys-lang/package-websocket/actions/workflows/pythonpackage.yml

.. _Mys programming language: https://mys-lang.org
