# Tomo parameters
#
angular_range = 180
NoP = 60
proj_per_angle = 1
scanlist = []
#
# ---------------
# Pre-work & Settings
#
SetDetectors(area_detector_collector)
area_detector_collector.doPrepare()
rotation_stage.doWriteSpeed(6)
rotation_stage.move(0)
set(NexusStructure,"alias",'NexusStructure_AreaDetector')
hama_image_type.set_to_invalid()
#
# ---------------
# Tomography
#
with nexusfile_open('ODIN tomo basic script - Test 1'):
# Dark field acquisition
    print("STEP 1: Dark field images must be acquired. For this, turn the LIGHT OFF and REMOVE SAMPLE from rotation stage.")
    sleep(15)
    print("Dark field image acquisition. This will take a couple of seconds.")
    hama_image_type.set_to_dark_field()
    count(hama_camera=5)
# Flat field acquisition
    print("STEP 2: Flat field images must be acquired. For this, turn the LIGHT ON.")
    sleep(30)
    print("Flat field image acquisition. This will take a couple of seconds.")
    hama_image_type.set_to_flat_field()
    count(hama_camera=5)
# Projection acquisition
    print("STEP 3: You are ready to launch a light tomography. For this, place your SAMPLE ON the rotation stage.")
    sleep(30)
    print("Light tomography image acquisition. This will take a few minutes.")
    rotation_stage.maw(0)
    hama_image_type.set_to_projection()
    x = range(NoP + 1)
    for i in x:
        angular_position = i * angular_range/NoP
        y = range(proj_per_angle)
        for j in y:
            scanlist.append(angular_position)
    scan(rotation_stage,scanlist,hama_camera=proj_per_angle)
#
# THE END
#
hama_image_type.set_to_invalid()
area_detector_collector.doStop()
print("Your light tomography is done!")
