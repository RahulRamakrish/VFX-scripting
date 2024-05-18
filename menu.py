toolbar = nuke.toolbar("Nodes")

ceaMenu = toolbar.addMenu("CEA", icon="cea24x24.png")

ceaMenu.addCommand("Gizmos/CEA_Gizmos/New_Distortion", "nuke.createNode(\"New_Distortion\")", icon="distort.png")