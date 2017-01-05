"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org; pedro.vicente@wavec.org

Example.py is an example file of the Installation module within the suite of design tools
developed under the EU FP7 DTOcean project. Example.py provides an estimation of
the predicted performance of feasible maritime infrastructure solutions
that can carry out marine operations pertaining to the installation of
wave and tidal energy arrays.

Example.py can be described in the following sub-modules:
0 - Loading the example input data
1 - Calling the Installation module

Input Parameters
----------
dictionnaries containing the vessel, equipment and ports databases from the Logistics module:
    vessels(DataFrame): Panda table containing the vessel database
    equipments (DataFrame): Panda table containing the equipment database
    ports (DataFrame): Panda table containing the ports database

dictionnaries containing the vessel, equipment and ports databases from the Logistics module:
    'phase_order' (Dataframe): dataframe containing a panda dataframe with the logitic operation phase order
    'schedule_OLC' (Dataframe): dataframe containing a panda dataframe with time duration and olc
    'penet_rates' (Dataframe): dataframe containing the penetration rates according to soil type
    'laying_rates' (Dataframe): dataframe containing the laying rates according to soil type
    'other_rates' (Dataframe): dataframe containing other rates
    'port_sf' (Dataframe): dataframe containing the safety factors applied to ports
    'vessel_sf' (Dataframe): dataframe containing the safety factors applied to vessels
    'eq_sf' (Dataframe): dataframe containing the safety factors applied to equipments

dictionnaries containing all required inputs to the Installation module coming from Database/end-user:
     'site' (Dataframe): inputs required from the site leasa area coordinates
     'metocean' (Dataframe): metocean data
     'device' (Dataframe): inputs required from the device
     'sub_device' (Dataframe): inputs required from the sub-device
     'landfall' (Dataframe): inputs required from the landfall point

dictionnaries containing all required inputs to the Installation module coming from Hydrodynamics module:
     'layout' (DataFrame): UTM position of the devices

dictionnaries containing all required inputs to the Installation module coming from Electrical module:
     'collection_point' (Dataframe): collection point data
     'dynamic_cable' (Dataframe): dynamic cable data
     'static_cable' (Dataframe): static cable data
     'cable_route' (Dataframe): cable route data
     'connectors' (Dataframe): cabe connectors data
     'external_protection' (Dataframe): coordinates and type of the external protection elements data
     'topology' (Dataframe): electrical layout type

dictionnaries containing all required inputs to the Installation module coming from Mooring and Foundations module:
    'line' (Dataframe): mooring lines data
    'foundation' (Dataframe): foundations data

flags indicating the required outputs of the modules:
    'PRINT_FLAG' (boolean): flag to indicate if output prints should be sent to terminal
    'PLOT_FLAG' (boolean): flag to indicate if output plots should be presented and saved
    'PLOT_GANTT' (boolean): flag to indicate if the installation gantt chart should be presented and saved
    'PRINT_CSV' (boolean): flag to indicate if the output .csv file with results per logistic phase should be produced

name to give to the csv output file:
    'PRINT_CSV' (string): name to give to the csv output file (if requested as an output)

location of the outside file for the port selection process:
    'point_path' (path): location of the european coastline grid data
    'graph_path' (path): location of the graph structure for the port selection algorithm


Outputs returns:
-------

installation (dict): dictionnary compiling all key results obtained from the assessment of the logistic phases for installation:
'inst_log':	List of logistic phase during installation
'port_req':	Dictionary of the port requirements calculated
'port_feas': Dictionary of ports satisfying the requirements
'port_sol':	Dictionary of the port selected and its distance to site
'planning':	Dictionary containing the layering rules for the planning of the logitic phases during installation
'inst_sol':	Dictionary containing the outcome of the optimal solutions for each logistic phase during installation
'dev_com':    Commissioning time per device
'warning':	Warning message

The 'inst_sol' dictionnary compiles all key results obtained from the assessment of each logistic phase in the installation:
    'plan' (dict): installation sequence of the required logistic phases
    'port' (DataFrame): port data related to the selected installation port
    'requirement' (tuple): minimum requirements returned from the feasibility functions
    'eq_select' (dict): list of equipments satisfying the minimum requirements
    've_select' (dict): list of vessels satisfying the minimum requirements
    'combi_select' (dict): list of solutions passing the compatibility check
    'schedule' (dict): list of parameters with data about time
    'cost' (dict): vessel equiment and port cost
    'risk (dict)': currently empty
    'envir (dict)': currently empty
    'status': string indicating if the computation was successful and a solution was found

Additional output plots can be produced if the user indicates.
    Plot bar: indicating the cost, schedule and simulation time values
    Plot pie: indicating the cost, schedule and simulation time percentual distribution
    Plot table: indicating the number and type of vessel equipment available through selection process and the selection requirements
per logistic phase, with the name of the file accordingly.

See also: ...

                       DTOcean project
                    http://www.dtocean.eu

                   WavEC Offshore Renewables
                    http://www.wavec.org/en

"""

import os

from dtocean_logistics.load import load_phase_order_data, load_time_olc_data
from dtocean_logistics.load import load_eq_rates
from dtocean_logistics.load import load_sf
from dtocean_logistics.load import load_vessel_data, load_equipment_data
from dtocean_logistics.load import load_port_data
from dtocean_logistics.load.wp_bom import load_user_inputs, load_hydrodynamic_outputs
from dtocean_logistics.load.wp_bom import load_electrical_outputs, load_MF_outputs
from dtocean_logistics.load.input_checkin import input_check
from dtocean_installation.main import installation_main
from dtocean_installation.configure import get_include_path

this_dir = os.path.realpath(os.path.dirname(__file__))



def get_store_path(store_dir, store_name):
    """shortcut function to load files from the storage folder
    """
    store_path = os.path.join(store_dir, '{0}'.format(store_name))

    return store_path

#def run():


"""
Load required inputs and database into panda dataframes
"""

import pickle

def load_test(store_dir, force_load=True, pkl_file='objs.pickle'):

    pkl_path = os.path.join(this_dir, pkl_file)

    if os.path.isfile(pkl_path) and not force_load:

        with open(pkl_path) as f:
            (vessels, equipments, ports,
             phase_order, schedule_OLC, penet_rates, laying_rates, other_rates, port_sf, vessel_sf, eq_sf,
             site, metocean, device, sub_device,landfall,
             layout,
             collection_point, dynamic_cable, static_cable, cable_route, connectors, external_protection, topology,
             line, foundation,
             PRINT_FLAG, PLOT_FLAG, PLOT_GANTT, PRINT_CSV, cvs_filename,
             point_path,
             graph_path) = pickle.load(f)

    else:

        #default_values inputs
        store_path = get_store_path(store_dir, "installation_order_0.xlsx")
        phase_order = load_phase_order_data(store_path)
        #
        store_path = get_store_path(store_dir, "operations_time_OLC.xlsx")
        schedule_OLC = load_time_olc_data(store_path)

        store_path = get_store_path(store_dir, "equipment_perf_rates.xlsx")
        penet_rates, laying_rates, other_rates = load_eq_rates(store_path)

        store_path = get_store_path(store_dir, "safety_factors.xlsx")
        port_sf, vessel_sf, eq_sf = load_sf(store_path)

        #Internal logistic module databases
        store_path = get_store_path(store_dir, "logisticsDB_vessel_python.xlsx")
        vessels = load_vessel_data(store_path)

        store_path = get_store_path(store_dir, "logisticsDB_equipment_python.xlsx")
        equipments = load_equipment_data(store_path)

        store_path = get_store_path(store_dir, "logisticsDB_ports_python.xlsx")
        ports = load_port_data(store_path)

        #upstream module inputs/outputs
        store_path = get_store_path(store_dir, "inputs_user.xlsx")
        site, metocean, device, sub_device,landfall = load_user_inputs(store_path)

        store_path = get_store_path(store_dir, "ouputs_hydrodynamic.xlsx")
        layout = load_hydrodynamic_outputs(store_path)

        store_path = get_store_path(store_dir, "ouputs_electrical.xlsx")
        collection_point, dynamic_cable, static_cable, cable_route, connectors, external_protection, topology = load_electrical_outputs(store_path)

        store_path = get_store_path(store_dir, "outputs_MF.xlsx")
        line, foundation = load_MF_outputs(store_path)

        # Transit points and graph
        point_path = get_store_path(store_dir, "Point_DTOcean_0.csv")
        graph_path = get_store_path(store_dir, "graph_sea_european_sea.p")

        # OUTPUT options:
        # *** Print outputs to terminal ***
        PRINT_FLAG = True
        # PRINT_FLAG = False
        # *** Print plots ***
        # PLOT_FLAG = True
        PLOT_FLAG = False
        # *** Produce csv ***
        PRINT_CSV = True
        # PRINT_CSV = False
        cvs_filename = "Outputs/Installation_All.csv"
        # *** Plot Gantt chart ***
        PLOT_GANTT = True
        # PLOT_GANTT = False

        with open(pkl_path, 'w') as f:
            pickle.dump([vessels, equipments, ports,
                                         phase_order, schedule_OLC, penet_rates, laying_rates, other_rates, port_sf, vessel_sf, eq_sf,
                                         site, metocean, device, sub_device,landfall,
                                         layout,
                                         collection_point, dynamic_cable, static_cable, cable_route, connectors, external_protection, topology,
                                         line, foundation,
                                         PRINT_FLAG, PLOT_FLAG, PLOT_GANTT, PRINT_CSV, cvs_filename,
                                         point_path,
                                         graph_path], f)


    return (vessels, equipments, ports,
         phase_order, schedule_OLC, penet_rates, laying_rates, other_rates, port_sf, vessel_sf, eq_sf,
         site, metocean, device, sub_device,landfall,
         layout,
         collection_point, dynamic_cable, static_cable, cable_route, connectors, external_protection, topology,
         line, foundation,
         PRINT_FLAG, PLOT_FLAG, PLOT_GANTT, PRINT_CSV, cvs_filename,
         point_path,
         graph_path)

if __name__ == "__main__":

    store_path = get_include_path()

    (vessels, equipments, ports,
     phase_order, schedule_OLC, penet_rates, laying_rates, other_rates, port_sf, vessel_sf, eq_sf,
     site, metocean, device, sub_device,landfall,
     layout,
     collection_point, dynamic_cable, static_cable, cable_route, connectors, external_protection, topology,
     line, foundation,
     PRINT_FLAG, PLOT_FLAG, PLOT_GANTT, PRINT_CSV, cvs_filename,
     point_path,
     graph_path) = load_test(store_path)

    ERROR_IN_INPUT = input_check( vessels, equipments, ports,
                             site, metocean, device, sub_device,landfall,
                             layout,
                             collection_point, dynamic_cable, static_cable, cable_route, connectors, external_protection, topology,
                             line, foundation,
                             PRINT_FLAG, PLOT_FLAG, PLOT_GANTT, PRINT_CSV, cvs_filename
                             )

    if not ERROR_IN_INPUT:
        installation_output = installation_main( vessels, equipments, ports,
                                             phase_order, schedule_OLC, penet_rates, laying_rates, other_rates, port_sf, vessel_sf, eq_sf,
                                             site, metocean, device, sub_device,landfall,
                                             layout,
                                             collection_point, dynamic_cable, static_cable, cable_route, connectors, external_protection, topology,
                                             line, foundation,
                                             PRINT_FLAG, PLOT_FLAG, PLOT_GANTT, PRINT_CSV, cvs_filename
                                             )
    else:
         print 'Error in the Inputs!'


