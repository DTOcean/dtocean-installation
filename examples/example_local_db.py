"""

Example file using local database files from /databases. This bypasses the
'DTocean/include' directory from the previous example file for all files bar
the coastline data.

@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org; pedro.vicente@wavec.org

"""
import math
import numpy as np
import pandas as pd

import os

from dtocean_logistics.load import load_phase_order_data, load_time_olc_data
from dtocean_logistics.load import load_eq_rates
from dtocean_logistics.load import load_sf
from dtocean_logistics.load import load_vessel_data, load_equipment_data
from dtocean_logistics.load import load_port_data
from dtocean_logistics.load.wp_bom import (load_user_inputs,
                                           load_hydrodynamic_outputs)
from dtocean_logistics.load.wp_bom import (load_electrical_outputs,
                                           load_MF_outputs)
from dtocean_logistics.load.input_checkin import input_check
from dtocean_installation.main import installation_main
from dtocean_installation.configure import get_include_path

from dtocean_installation import start_logging

# Start the logging system
start_logging()

# Set test data directory
mod_path = os.path.realpath(__file__)
mod_dir = os.path.dirname(mod_path)

## Set test data directory
data_dir = os.path.join(mod_dir, "..", "sample_data")


# load local databases
store_path = os.path.join(data_dir, "installation_order_0.xlsx")
phase_order = load_phase_order_data(store_path)

store_path = os.path.join(data_dir, "operations_time_OLC.xlsx")
schedule_OLC = load_time_olc_data(store_path)

store_path = os.path.join(data_dir, "equipment_perf_rates.xlsx")
penet_rates, laying_rates, other_rates = load_eq_rates(store_path)

store_path = os.path.join(data_dir, "safety_factors.xlsx")
port_sf, vessel_sf, eq_sf = load_sf(store_path)

# Internal logistic module databases
store_path = os.path.join(data_dir, "logisticsDB_vessel_python.xlsx")
vessels = load_vessel_data(store_path)

store_path = os.path.join(data_dir, "logisticsDB_equipment_python.xlsx")
equipments = load_equipment_data(store_path)

store_path = os.path.join(data_dir, "logisticsDB_ports_python.xlsx")
ports = load_port_data(store_path)

# Upstream module inputs/outputs
store_path = os.path.join(data_dir, "inputs_user.xlsx")
site, metocean, device, sub_device, landfall, entry_point = load_user_inputs(
    store_path)

store_path = os.path.join(data_dir, "ouputs_hydrodynamic.xlsx")
layout = load_hydrodynamic_outputs(store_path)

store_path = os.path.join(data_dir, "ouputs_electrical.xlsx")
(collection_point, dynamic_cable, static_cable, cable_route, connectors,
 external_protection, topology) = load_electrical_outputs(store_path)

tool = 'Jetting'


all_tool = [[tool.lower()]] * len(static_cable)
static_cable.loc[:, 'trench type [-]'] = pd.Series(all_tool)

store_path = os.path.join(data_dir, "outputs_MF_empty.xlsx")
line, foundation = load_MF_outputs(store_path)

# load coastline data from dtocean/include
include_external_data = get_include_path()
point_path = os.path.join(include_external_data, "Point_DTOcean_0.csv")
graph_path = os.path.join(include_external_data, "graph_sea_european_sea.p")

# output options
# Print outputs to terminal
PRINT_FLAG = False
# Print plots
PLOT_FLAG = False
# Produce csv
PRINT_CSV = False
cvs_filename = "Outputs/Installation_All.csv"
# Plot Gantt chart
PLOT_GANTT = False

CHECK_INPUTS = False

installation_output = installation_main(vessels,
                                                equipments,
                                                ports,
                                                phase_order,
                                                schedule_OLC,
                                                penet_rates,
                                                laying_rates,
                                                other_rates,
                                                port_sf,
                                                vessel_sf,
                                                eq_sf,
                                                site,
                                                metocean,
                                                device,
                                                sub_device,
                                                landfall,
                                                entry_point,
                                                layout,
                                                collection_point,
                                                dynamic_cable,
                                                static_cable,
                                                cable_route,
                                                connectors,
                                                external_protection,
                                                topology,
                                                line,
                                                foundation,
                                                skip_phase=True,
                                                check_inputs=False
                                                )
 