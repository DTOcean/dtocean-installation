# -*- coding: utf-8 -*-
"""
"""

import os

import pandas as pd

# Helpers for configuration files
from polite.appdirs import site_data_dir
from polite.paths import Directory
from polite.configuration import ReadINI

DIR_PATH = os.path.dirname(__file__)


def get_root_configuration(root_config_name="install.ini"):
    
    """Pick the necessary paths to configure the external files for the wave
    and tidal packages."""
    
    # Get the root path from the site data path.
    root_config_dir = site_data_dir("DTOcean Installation", "DTOcean")
    configdir = Directory(root_config_dir)

    ini_reader = ReadINI(configdir, root_config_name)
    config = ini_reader.get_config() 
    
    return config

def get_include_path():
    
    root_config = get_root_configuration()
    root_path = root_config["InstallSettings"]["InstallPath"]
    include_path = root_config["InstallSettings"]["IncludePath"]
    
    full_path = os.path.join(root_path, include_path)
    
    return full_path
    
def get_operations_template(template_name="operations_time_OLC.xlsx"):

    template_path = os.path.join(DIR_PATH, "config", template_name)
    template_df = pd.read_excel(template_path)
    
    return template_df


