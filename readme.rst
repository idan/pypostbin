pypostbin
=========

PyPostbin is a simple `postbin.org`_ clone, written because I tweeted about
postbin and the resulting traffic took postbin over their Google AppEngine
quota. It is designed to be run on `ep.io`_ with a minimum of fuss.

.. _`postbin.org`: http://postbin.org
.. _`ep.io`: http://ep.io

How do I use this?
==================

1. Clone this repository
2. Create a virtualenv for your project. You *are* using virtualenv, right?
3. Install some basic requirements using ``pip install -r requirements.txt``. You *are* using pip, right?
4. You'll need to specify a value for ``SECRET_KEY`` in ``settings/base.py``. By default, Django concocts a random 50-character alphanumeric string for this value.
5. Create an app instance on ep.io, and upload this app there.
6. There is no step 6.

How does this work?
===================

Let's say your app instance is called "postbin", so you're hosting the app on
``mypostbin.ep.io``. You direct a browser at http://mypostbin.ep.io and you get
redirected to a blank postbin at http://mypostbin.ep.io/1/. It tells you that
there are no posts yet, and that you should make a couple in order to find
satisfaction in life. Heed these sage words.

So you fire up a terminal, and recite the following incantation::

  curl -d "foo=bar&baz=bling" -v http://mypostbin.ep.io/1/

And voila, your POSTed data is visible when you refresh the browser.

Is this totally ghetto?
=======================

Yes. Yes it is. This hack was written entirely between the hours of midnight
and 3 A.M.