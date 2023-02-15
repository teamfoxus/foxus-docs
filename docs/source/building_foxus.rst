Building Foxus
=====

.. note::

   Here be dragons! Not all environments are currently supported, and those which have support may not have detailed build instructions yet.
   
   Notably, Windows builds for Foxus are not yet supported. There's still some kinks to be worked out with the OpenCV libraries and other dependencies. 

   Although it's still a big unknown, you can always try building Foxus under the Windows Subsystem for Linux or other virtual machine solutions!

   Got Foxus built out on something not mentioned here? We'd love to hear from you!



Linux (General)
------------

You'll first need to download the X11 build dependencies for Godot, as described in `their documentation <https://docs.godotengine.org/en/stable/development/compiling/compiling_for_x11.html>`_. They provide a set of one-line commands specific to your Linux distribution to get started.

You'll also want to install Android Studio. Go to https://developer.android.com/studio/index.html and find the Linux download. Go through the standard install process. When you're on the screen reading “Welcome to Android Studio”, click “More Actions” and then “SDK Manager”.

On this screen, you're given the install location of the Android SDK, which you'll need to know in a moment. You can also install the required NDK here. Go to the *SDK Tools* tab, then check *Show Package Details* in the bottom right. Now you'll be able to select NDK version 23.2.8568313 and install it by hitting Apply.

Set the *ANDROID_NDK_ROOT* and *ANDROID_SDK_ROOT* variables, using the install location of your Android SDK from above. For example, if your Android SDK was installed in */home/Android/Sdk*, your commands might look like this:

.. code-block:: console

   export ANDROID_SDK_ROOT=/home/Android/Sdk
   export ANDROID_NDK_ROOT=/home/Android/Sdk/ndk/23.2.8568313

If you don't have any installed already, I also recommend getting *unzip*, *clang* and both the JRE and JDK for your preferred version of Java. (Java 11 works well.)

You can now use the console to clone and build Foxus. Each of these steps will take a while.

.. code-block:: console

   git clone --recursive https://github.com/cryptovoxels/foxus.git
   cd foxus
   ./build_godot.sh
   ./build.sh

Finally, to run the editor:

.. code-block:: console

   ./run_editor.sh

Go to Editor > Editor Settings in the top bar. Here you'll have to set the Android SDK path (it's the same one we found earlier) and the debug keystore (which will be in the foxus folder). After that, you're good to go and you can build this project out to your Oculus headset.

Linux (Steam Deck)
------------

There's a few things to consider before we get started…

The Steam Deck OS ships as “read-only” which prevents us from installing the necessary packages to build Godot and Foxus. This means that we'll be changing it to read-write mode immediately, which is recommended more for advanced Linux users since we can make changes to the OS. Don't install packages willy-nilly after this or you may break something!

The Oculus app currently doesn't support Linux. This means that we don't have access to the Air Link features, and so, to build to your headset, you'll be using a wired connection. Meta recommends a very expensive Oculus Link cable, but it seems to me any USB-C cable may work. Cable management may become an interesting challenge for you. Whenever possible, try using Bluetooth connected keyboards/mice to free up some ports. I'm using a generic USB-C dock with USB 2.0 ports, with an adapter to plug the USB-C cable into one.

After you've used a wired connection, you can use ADB to switch to a wireless one temporarily. This lets you quickly iterate through builds with the Foxus cameras plugged in, which is a real plus.

As our first step we'll be setting up a password to use sudo commands. Switch to Desktop Mode if you haven't already, and open up the Konsole app.

.. code-block:: console

   passwd

Don't forget the password you set in this step! You'll need it again frequently.

Next up we'll disable read-only mode on the OS, and make sure pacman (which we'll be using to fetch packages) is up to date.

.. code-block:: console

   sudo steamos-readonly disable
   sudo pacman-key --init
   sudo pacman-key --populate
   sudo pacman-key --refresh-keys 

(That last one might take a while, and I can't tell if it's required or I'm superstitious … but it doesn't hurt.)

The Godot build page has a “one-line” command to get the required dependencies working on Arch Linux setups. However, this will break the Steam Deck's audio libraries if you use them as-is, and there's some stuff missing that we'll have to do ourselves.

.. code-block:: console

   sudo pacman -S scons gcc yasm linux-headers clang llvm pkgconf libxcursor libxinerama libxi libxrandr mesa glu libglvnd alsa-lib libisl libmpc linux-api-headers glibc libx11 xorgproto libxrender pavucontrol libxext systemd libpulse libxfixes

Yes, a lot of this is a reinstall of existing packages. Just trust me — not all of the stuff you'd expect to work out of the box will unless you reinstall them!

Let's grab the JDK and JRE for Java 11 while we're here.

.. code-block:: console

   sudo pacman -S jdk11-openjdk jre11-openjdk

OK, take a break from konsole commands. It's time to go install the Android SDK & NDK. I recommend using Android Studio for this. https://developer.android.com/studio will have the latest version, so you can navigate there on your Steam Deck and extract it. Go into the “bin” folder and run the studio.sh file (or run it in the konsole if you like.) Go through the standard install process. When you're on the screen reading “Welcome to Android Studio”, click “More Actions” and then “SDK Manager”.

On this screen, you're given the install location of the Android SDK:

.. code-block:: console

   /home/deck/Android/Sdk

…which will help you later. You can also install the required NDK here. Go to the “SDK Tools” tab, then check “Show Package Details” in the bottom right. Now you'll be able to select NDK version 23.2.8568313 and install it by hitting Apply.

We can now set these locations as environment variables for the build process to use.

.. code-block:: console

   export ANDROID_SDK_ROOT=/home/deck/Android/Sdk
   export ANDROID_NDK_ROOT=/home/deck/Android/Sdk/ndk/23.2.8568313

Now let's try actually building our special version of Godot. Each of these steps will take a while.

.. code-block:: console

   git clone --recursive https://github.com/cryptovoxels/foxus.git
   cd foxus
   ./build_godot.sh
   ./build.sh
  
Finally, to run the editor:

.. code-block:: console

   ./run_editor.sh

You're in! Go to Editor > Editor Settings in the top bar. Here you'll have to set the Android SDK path (it's the same one we found earlier) and the debug keystore (which will be in the foxus folder). After that, you're good to go and you can build this project out to your Oculus headset.

MacOS (Intel chip only)
------------

M1 and M2 chips are currently **not** supported for building Foxus. 

.. note::

   Here be dragons! The macOS builds of Foxus are mostly untested. 

   If you're running a macOS environment and want to share your experiences building out Foxus, get in touch!


You'll first need to download the macOS build dependencies for Godot, as described in `their documentation <https://docs.godotengine.org/en/stable/development/compiling/compiling_for_osx.html>`_. If you use `Homebrew <https://brew.sh/>`_ or `MacPorts <https://www.macports.org/>`_, installing SCons and yasm is a bit easier:


.. code-block:: Homebrew

   brew install scons yasm

.. code-block:: MacPorts

   sudo port install scons yasm

You'll also want to install Android Studio. Go to https://developer.android.com/studio/index.html and find the macOS download. Go through the standard install process. When you're on the screen reading “Welcome to Android Studio”, click “More Actions” and then “SDK Manager”.

On this screen, you're given the install location of the Android SDK, which you'll need to know in a moment. You can also install the required NDK here. Go to the *SDK Tools* tab, then check *Show Package Details* in the bottom right. Now you'll be able to select NDK version 23.2.8568313 and install it by hitting Apply.

Set the *ANDROID_NDK_ROOT* and *ANDROID_SDK_ROOT* variables, using the install location of your Android SDK from above. For example, if your Android SDK was installed in */home/Android/Sdk*, your commands might look like this:

.. code-block:: console

   export ANDROID_SDK_ROOT=/home/Android/Sdk
   export ANDROID_NDK_ROOT=/home/Android/Sdk/ndk/23.2.8568313

If you don't have any installed already, I also recommend getting *unzip*, *clang* and both the JRE and JDK for your preferred version of Java. (Java 11 works well.)

You can now use the console to clone and build Foxus. Each of these steps will take a while.

.. code-block:: console

   git clone --recursive https://github.com/cryptovoxels/foxus.git
   cd foxus
   ./build_godot.sh
   ./build.sh

Finally, to run the editor:

.. code-block:: console

   ./run_editor.sh

Go to Editor > Editor Settings in the top bar. Here you'll have to set the Android SDK path (it's the same one we found earlier) and the debug keystore (which will be in the foxus folder). After that, you're good to go and you can build this project out to your Oculus headset.

If you're trying to run Foxus on macOS directly, due to how the USB cameras are handled in macOS, the Foxus app has to run as root (Administrator). Use the provided run.sh with sudo to run it:

.. code-block:: console

   sudo ./run.sh
