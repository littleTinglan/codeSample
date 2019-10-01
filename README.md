# Lillian's Code Sample

Code samples and details for projects I have worked on.

## Projects

### [Colorblind Screen Filter App](https://github.com/littleTinglan/screen-filter-app) - Currently under development
  * A WPF (Windows Presentation Foundation) app ideally would help to develop colorblind friendly art assets. It will apply a filter to 
  the selected area of the screen which modifies that part of the screen displaying as colorblind mode.
  * Inspired by talking to a VFX artist friend. According to him, the workflow for developing/iterating colorblind friendly art assets is painful.
  It requires importing the assets into the game engine, launching the game, taking a screenshot, opening the screenshot to Photoshop, then
  apply a filter and repeat the above cycle. I am developing an app hopefully will help with this tedious process.

### [Maya Face Auto Rig Tool](https://github.com/littleTinglan/codeSample/blob/master/facerig.py) 
  * A Maya tool written in Python helps automate facial rigging process with blendshapes
  * [Demo Video](https://github.com/littleTinglan/codeSample/blob/master/demorel.mp4)

### [Custome Graphics Engine](https://github.com/littleTinglan/d11-graphics-engine)
  * Custome DirectX 11 graphics engine. The starter code was given by a professor. I was responsible for implementing the following features:
    * Import models and textures
    * Camera and materials
    * Normal maps and [lighting](https://github.com/littleTinglan/d11-graphics-engine/blob/master/d11/DX11Starter/Light.h) (directional light, point light,
    customizable spotlight, specular light)
    * [Skybox](https://github.com/littleTinglan/d11-graphics-engine/blob/master/d11/DX11Starter/SkyPS.hlsl)
    * Post processing bloom
    * [Post processing depth of field](https://github.com/littleTinglan/d11-graphics-engine/blob/master/d11/DX11Starter/dofPS.hlsl)
    
## Work Experiences

  ### Tool & Pipeline Technical Artist Intern - League of Legends
  #### Riot Games
  * In-game Cheat
    * A set of cheatsheets in Lua that help internal developers conveniently recreate in-game situations
      * Manipulating player stats: movement speed, critical strike chance, attack speed
      * Triggering different run cycle animations
      * Displaying debug information for bones and bone axis
      * Triggering desired gameplay situations: spawn monsters, polymorph, special item effects
  * Features for Custom Game Engine Tools
    * A tool in Python for the custom game engine in C++. When creating a new skin for a champion, allow the user to choose an existing asset
    as the base for the new skin. It will help to set up some files for the user such as the character rig file, the animation graph, and others. My task was to 
    allow the user to either create a new layer or to a specified layer when creating this new skin.
    * Writing validations calling Perforce commands. If the files already existed on local or depot for this champion, provide a warning.
    
  * Features for Maya Tools using PyQt
    * Responsible for implementing UI features and validation for a rigging tool.
  
  
