#!/usr/bin/python
# -*- coding: utf-8 -*-
# ----------------------------------------------
# --- Author         : Ahmet Ozlu
# --- Mail           : ahmetozlu93@gmail.com
# --- Date           : 27th January 2018
# ----------------------------------------------
# from utils.image_utils import image_saver

def predict_speed(
    past_front,
    current_front,
    scale_constant = 1  # manual scaling because we did not performed camera calibration
    ):
    movement = current_front-past_front
    speed = scale_constant * movement
    return speed




