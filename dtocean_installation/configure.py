# -*- coding: utf-8 -*-

#    Copyright (C) 2016 Mathew Topper
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

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


