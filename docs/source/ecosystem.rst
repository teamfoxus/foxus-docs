The Foxus Ecosystem
=====

Foxus Camera
--------

The Foxus camera is a nifty bit of hardware -- two high-quality stereoscopic cameras that go on the front of your VR device to allow full-color passthrough video. 

.. image:: http://www.foxus.com/foxus-quest.jpg
    :alt: The Foxus camera, in bright blue, mounted on the front of a Meta Quest 2 headset.
    :align: center


Right now, these play nice with the Godot engine, using a special plugin called gd_eiffelcam to process the video feeds. You can connect them to a Meta Quest headset using a microUSB to USB-C cable. You can also connect them directly to a computer, where the feeds can be used in other programs with a bit of hackery!

Foxus Playback Engine
--------

The Foxus playback engine is usually what we mean when we say *Foxus*. It's an app that runs in your headset to give you access to mixed reality experiences. We're working on adding networking features so that your Foxus can sync up with others in the same room, and you can share some communal MR experiences. Rather than a fully virtual reality experience, or an augmented reality experience where digital assets are overlaid on reality, we use the term mixed reality because the Foxus is for processing and altering the optical flow fed through these cameras. 

Foxus Mixhouse
--------

This is the Foxus creator engine. In the Mixhouse, you'll be able to create MR experiences on your home computer and preview them inside of a headset. The Mixhouse runs on the Godot engine, but it's made for people who don't necessarily have experience with Godot. If you're a power user, we're hoping to also provide a Mixhouse plugin to enhance your regular Godot environment.

Foxus Storefront
--------

Made something great in the Mixhouse? Upload it to the Foxus storefront and anyone can use it inside the Foxus playback engine. Charge money or make it free. You decide if your creations are Mixable (can be edited by the purchaser) or set in stone. 

Foxus Toy?
--------

Maybe you don't have a Quest ... there's alternatives coming soon!

.. note::

   Here be dragons! The dragons here are especially large. The Foxus Toy is under super secret development.