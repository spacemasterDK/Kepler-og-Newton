import numpy as np
from IPython.display import display, Math


# Position_1 = 478

# Position_2 = 278

# tidspunkt_1 = 0

# tidspunkt_2 = 1.30

# Målt_Diameter_1 = 357

# Målt_Diameter_2 = 359

# Tabelværdi_diameter = 2*71492

# Tabelværdi_afstand_til_månen = 421.6*10**(3)


def beregning_af_periode(Position_1, Position_2,tidspunkt_1, tidspunkt_2, Målt_Diameter_1, Målt_Diameter_2,Tabel_værdi_diameter, Tabelværdi_afstand_til_månen):
    
    Radius_1 = Målt_Diameter_1/2
    Radius_2 = Målt_Diameter_2/2
    
    Afstand_til_position_1 = Position_1-Radius_1
    Afstand_til_position_2 = Position_2-Radius_2
    
    
    Vinkel_position_1 = np.arcsin(Afstand_til_position_1/Målt_Diameter_1*(Tabel_værdi_diameter/Tabelværdi_afstand_til_månen))*360/(2*np.pi)
    
    Vinkel_position_2 = np.arcsin(Afstand_til_position_2/Målt_Diameter_2*(Tabel_værdi_diameter/Tabelværdi_afstand_til_månen))*360/(2*np.pi)
    
    relativ_vinkel = np.abs(Vinkel_position_1-Vinkel_position_2)
    
    Delta_t = (tidspunkt_1-tidspunkt_2)/24
    
    Vinkel_hastighed = np.abs(relativ_vinkel/Delta_t)
    
    periode = 360/Vinkel_hastighed
    
    print(f"Den målte periode er fundet til {periode:0.3f} dage.")

# beregning_af_periode(Position_1, Position_2,tidspunkt_1, tidspunkt_2, Målt_Diameter_1, Målt_Diameter_2,Tabelværdi_diameter,Tabelværdi_afstand_til_månen)

# omregn til perioden til antal år.

perioden_i_år = 4.85*10**(-3)

def masse_beregner(perioden_i_år, Tabelværdi_afstand_til_månen):
    
    Afstand_i_AE = Tabelværdi_afstand_til_månen*(1/(149.6*10**(6)))
    
    # print(Afstand_i_AE)
    Planetens_masse = Afstand_i_AE**3/(perioden_i_år)**2
    
    return print(f'Planetens masse målt i antal solmasser er fundet til {Planetens_masse:0.2e} AE')

# masse_beregner(perioden_i_år,Tabelværdi_afstand_til_månen)