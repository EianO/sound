while True:
    if input.sound_level() > 110:
        light.set_all(light.rgb(250, 0, 250))
    else:
        light.clear