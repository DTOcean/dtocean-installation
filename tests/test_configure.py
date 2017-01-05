
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

