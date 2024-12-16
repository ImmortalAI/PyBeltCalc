from bd_realization.database import sessionmanager
from bd_realization.models import Table_2_7
def fill_table():
    with sessionmanager.session() as session:
        table_2_7 = [Table_2_7(profil="К", V=5, DP1=40, DF0=4.76),
                 Table_2_7(profil="К", V=5, DP1=45, DF0=5.26),
                 Table_2_7(profil="К", V=5, DP1=50, DF0=5.6),
                 Table_2_7(profil="К", V=5, DP1=56, DF0=6.12),
                 Table_2_7(profil="К", V=5, DP1=63, DF0=6.46),
                 Table_2_7(profil="К", V=5, DP1=71, DF0=6.8),
                 Table_2_7(profil="К", V=5, DP1=80, DF0=6.97),
                 Table_2_7(profil="К", V=5, DP1=90, DF0=7.3),
                 Table_2_7(profil="К", V=5, DP1=100, DF0=7.48),
                 Table_2_7(profil="К", V=5, DP1=112, DF0=7.65),
                 Table_2_7(profil="К", V=5, DP1=125, DF0=7.82),
                 Table_2_7(profil="К", V=5, DP1=140, DF0=8.1),
                 Table_2_7(profil="К", V=5, DP1=160, DF0=8.15),
                 Table_2_7(profil="К", V=5, DP1=80, DF0=2.41),
                 Table_2_7(profil="К", V=5, DP1=90, DF0=2.78),
                 Table_2_7(profil="К", V=5, DP1=100, DF0=3.09),
                 Table_2_7(profil="К", V=5, DP1=112, DF0=3.4),
                 Table_2_7(profil="К", V=5, DP1=125, DF0=3.65),
                 Table_2_7(profil="К", V=5, DP1=140, DF0=3.89),
                 Table_2_7(profil="К", V=5, DP1=160, DF0=4.14),
                 Table_2_7(profil="К", V=5, DP1=180, DF0=4.32),
                 Table_2_7(profil="К", V=5, DP1=200, DF0=4.45),
                 Table_2_7(profil="К", V=5, DP1=224, DF0=4.64),
                 Table_2_7(profil="К", V=5, DP1=250, DF0=4.76)]
        
        session.add_all(table_2_7)
        session.flush()
        session.commit()

def get_by_profil_V_DP1(profil: str, V: float, DP1: float) -> Table_2_7 | None:
    with sessionmanager.session() as session:
        return session.query(Table_2_7).filter(Table_2_7.profil == profil, Table_2_7.V == V, Table_2_7.DP1 == DP1).first()