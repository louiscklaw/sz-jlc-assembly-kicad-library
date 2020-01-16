# SZ-JLC-ASSEMBLY-KICAD-LIBRARY

| Master | Development | Chats |
|:--------:|:-------------:|:-------:|
| [![Build Status](https://img.shields.io/travis/com/louiscklaw/sz-jlc-assembly-kicad-library/master)](https://travis-ci.com/louiscklaw/sz-jlc-assembly-kicad-library) | [![Build Status](https://img.shields.io/travis/com/louiscklaw/sz-jlc-assembly-kicad-library/develop)](https://travis-ci.com/louiscklaw/sz-jlc-assembly-kicad-library) | [![Gitter](https://img.shields.io/gitter/room/louiscklaw/sz-jlc-assembly-kicad-library)](https://gitter.im/sz-jlc-assembly-kicad-library/community) |

### Purpose
This is my own kicad library to deal with the assembly services provided by SZ JLC. The origional idea is to build a kicad library according to the Excel table(part list/BOM list) available on the SZ JLC website https://www.sz-jlc.com/portal/smtComponentList.html

### Current progress
Currently it is still a "one-man" job and resources are very limited, the priorities and the progresses are shown below:

| filename | current progress | priority | Remarks |
|----------|----------|----------|---------|
| sz_jlc_accelerometer.lib | not reviewed | low | -- |
| sz_jlc_active_crystal_oscillator.lib | not reviewed | low | -- |
| sz_jlc_active_filter.lib | not reviewed | low | -- |
| sz_jlc_ambient_light_sensor.lib | not reviewed | low | -- |
| sz_jlc_amplifier.lib | not reviewed | low | -- |
| sz_jlc_analog_switch_chip.lib | not reviewed | low | -- |
| sz_jlc_analog_to_digital_conversion_chip.lib | not reviewed | low | -- |
| sz_jlc_angle_sensor.lib | not reviewed | low | -- |
| sz_jlc_angular_velocity_sensor.lib | not reviewed | low | -- |
| sz_jlc_attitude_sensor.lib | not reviewed | low | -- |
| sz_jlc_audio_power_amplifier.lib | not reviewed | low | -- |
| sz_jlc_avalanche_diode.lib | not reviewed | low | -- |
| sz_jlc_balanced_unbalanced_transformer.lib | not reviewed | low | -- |
| sz_jlc_ballast_controller.lib | not reviewed | low | -- |
| sz_jlc_battery_box_battery_holder.lib | not reviewed | low | -- |
| sz_jlc_battery_power_management_chip.lib | not reviewed | low | -- |
| sz_jlc_battery_protection_chip.lib | not reviewed | low | -- |
| sz_jlc_buffers_drivers_receivers_transceivers.lib | not reviewed | low | -- |
| sz_jlc_can_chip.lib | not reviewed | low | -- |
| sz_jlc_capacitor.lib | testing on first fabrication | high | -- |
| sz_jlc_ceramic_resonator.lib | not reviewed | low | -- |
| sz_jlc_clock_buffer_driver.lib | not reviewed | low | -- |
| sz_jlc_clock_generator_pll_frequency_synthesizer.lib | not reviewed | low | -- |
| sz_jlc_clock_timing_dedicated.lib | not reviewed | low | -- |
| sz_jlc_codec_chip.lib | not reviewed | low | -- |
| sz_jlc_color_sensor.lib | not reviewed | low | -- |
| sz_jlc_common_mode_inductor_filter.lib | not reviewed | low | -- |
| sz_jlc_diode.lib | testing | moderate | -- |
| sz_jlc_esd_diode.lib | not reviewed | low | -- |
| sz_jlc_inductor.lib | testing on first fabrication | high | -- |
| sz_jlc_ldo_low_dropout_linear_regulation.lib | not reviewed | low | -- |
| sz_jlc_led.lib | testing | moderate | -- |
| sz_jlc_microcontroller_mcu.lib | not reviewed | high | -- |
| sz_jlc_resistor.lib | testing on first fabrication | high | -- |
| sz_jlc_zener_diode.lib | testing | moderate | -- |

### Terms Explanation:
Progress steps and their meanings:

| steps |  | meaning | Remarks |
|-------|---|---------|---------|
| 1 | not reviewed | directly extract excel table, component name and basic footprint mapping only, no symbol drawings | -- |
| 2 | reviewed | fix missing symbol, align pin assignment to footprint |  |
| 3 | testing | test sample sent to PCB fabrication |  |
| 4 | done | supposing a usable library file here |  |

### Directory structure:
```
.
├── README.md
├── _ref                         # reference repos
├── sz_jlc_accelerometer.lib
├── ... lib files ...
├── sz_jlc_zener_diode.lib
├── test                         # test scripts
└── _util                        # modified kicad-library-utils
```

### Difficulties:
1. The number of component is huge. not everyone of them is being tested
1. The pin assignment and symbol generation (especially MCU) is still a problem as configuration/pin assignment need to be reviewed case by case. Currently looking into some OCR solution to accelerate the progress.

### Ref:
Partner repo, to generate the scaffold of lib and dcm files:
https://github.com/louiscklaw/kicad_factory_assembly_library

### Communication:
If you are interested in this repo/ideas, please don't hesitate to contact me @gitter.
Also, starts and forks are welcomed.
