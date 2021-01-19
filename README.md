# Summary
This is a repository of the projects I completed during this subject. The highlight folder is the **project** folder, which contains code for an automated irrigation (plant-watering) system. [See the video explaination here](https://www.youtube.com/watch?v=i_nD40_PrZo). In the video, demonstration is between 00:00-06:50, and afterwards is a lengthy reflection on the project and results.

# Plant irrigation system
Using a Sparkfun moisture sensor and Particle Photon device, we can read the dampness of the soil around a plant. When the moisture is below a certain level, the Partacle Photon sends a signal to open a "water valve", which would then automatically water the plant, until the soil becomes sufficiently damp.

The Particle Photon communicates with a Raspberry Pi using the Partacle API. The Raspberry Pi acts as a "processing unit", logging data and verifying that the Particle Photon device is alive. Should the Particle Photon device come offline, such as in the case of a power failure, the Raspberry Pi logs and notifies the user.
