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

import pandas as pd

from dtocean_installation import start_logging
from dtocean_installation.configure import get_operations_template

    
def test_start_logging():

    start_logging()
    
    assert True

def test_get_operations_template():
    
    template_df = get_operations_template()
    
    assert isinstance(template_df, pd.DataFrame)
    assert "Logitic operation [-]" in template_df.columns

