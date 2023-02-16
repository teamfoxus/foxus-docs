Importing 3D Models
===================================

.. note::

   Here be dragons! 
   
   Positioning of 3D models in a mixed reality space is not an exact science.

   Just placing an object in Godot will not anchor it to a "real" position in space.

   Moving your head, or moving within the space, may move 3D objects in unexpected ways. 

   This problem could likely be solved with the use of pose estimation tools like `ArUco markers <https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html>`_.


If you've made a 3D model in an external program, or downloaded one you can use, you can probably import it into the Foxus view. Check the `Godot documentation <https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_scenes.html>`_ to find a list of accepted formats. For now, since we're keeping things as simple as possible, we'll be using a .obj file with included materials. You can download this file, its .mtl (materials file), and the texture it uses as an image, just in case. 

`Foxus Logo 3D Model.obj </_static/FOXUS_LOGO/Foxus Logo 3d model .obj>`

`Foxus Logo 3D Model.mtl </_static/FOXUS_LOGO/Foxus Logo 3d model .mtl>`

`foxus-gradient-01.jpg </_static/FOXUS_LOGO/foxus-gradient-01.jpg>`

You can drag these directly into the Foxus project folder, or tuck them inside of a sub-folder to keep things more organized. Either way, they will be visible inside of the FileSystem tab inside of Godot:

.. image:: _static/3d1.png
   :align: center

*You can't see the .mtl file in this view, but it's there in the same folder.*