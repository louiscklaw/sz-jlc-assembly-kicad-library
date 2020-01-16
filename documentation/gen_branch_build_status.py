#!/usr/bin/env python

import os,sys,re
from pprint import pprint
from string import Template

def get_html_entities(str_in):
  return str_in.replace('/','%2F')

def get_repo_img(repo_in):
  return '[![Build Status](https://travis-ci.com/louiscklaw/sz-jlc-assembly-kicad-library.svg?branch='+get_html_entities(repo_in)+')](https://travis-ci.com/louiscklaw/sz-jlc-assembly-kicad-library)'

def get_filename(repo_in):
  return repo_in.replace('feature/','')

template = Template('| ${filename}.lib | not reviewed | low | ${repo_img} | -- |')

list_repo = [
  'feature/sz_jlc_accelerometer',
  'feature/sz_jlc_active_crystal_oscillator',
  'feature/sz_jlc_active_filter',
  'feature/sz_jlc_ambient_light_sensor',
  'feature/sz_jlc_amplifier',
  'feature/sz_jlc_analog_switch_chip',
  'feature/sz_jlc_analog_to_digital_conversion_chip',
  'feature/sz_jlc_angle_sensor',
  'feature/sz_jlc_angular_velocity_sensor',
  'feature/sz_jlc_attitude_sensor',
  'feature/sz_jlc_audio_power_amplifier',
  'feature/sz_jlc_avalanche_diode',
  'feature/sz_jlc_balanced_unbalanced_transformer',
  'feature/sz_jlc_ballast_controller',
  'feature/sz_jlc_battery_box_battery_holder',
  'feature/sz_jlc_battery_power_management_chip',
  'feature/sz_jlc_battery_protection_chip',
  'feature/sz_jlc_buffers_drivers_receivers_transceivers',
  'feature/sz_jlc_can_chip',
  'feature/sz_jlc_capacitor',
  'feature/sz_jlc_ceramic_resonator',
  'feature/sz_jlc_clock_buffer_driver',
  'feature/sz_jlc_clock_generator_pll_frequency_synthesizer',
  'feature/sz_jlc_clock_timing_dedicated',
  'feature/sz_jlc_codec_chip',
  'feature/sz_jlc_color_sensor',
  'feature/sz_jlc_common_mode_inductor_filter',
  'feature/sz_jlc_diode',
  'feature/sz_jlc_esd_diode',
  'feature/sz_jlc_inductor',
  'feature/sz_jlc_ldo_low_dropout_linear_regulation',
  'feature/sz_jlc_led',
  'feature/sz_jlc_microcontroller_mcu',
  'feature/sz_jlc_resistor',
  'feature/sz_jlc_zener_diode',
]

for each_repo in list_repo:
  print(template.substitute(filename=each_repo,repo_img=get_repo_img(each_repo)))
