from bd_realization.database import sessionmanager
from bd_realization.models import Table_2_9
def fill_table():
    with sessionmanager.session() as session:
        table_2_9 = [Table_2_9(profil="К", L0=750, LL0=1, CL=1),
                 Table_2_9(profil="К", L0=750, LL0=1.5, CL=1.05),
                 Table_2_9(profil="К", L0=750, LL0=2, CL=1.1),
                 Table_2_9(profil="К", L0=750, LL0=2.5, CL=1.15),
                 Table_2_9(profil="К", L0=750, LL0=3, CL=1.2),
                 Table_2_9(profil="К", L0=750, LL0=3.5, CL=1.25),
                 Table_2_9(profil="Л", L0=1500, LL0=1, CL=1),
                 Table_2_9(profil="Л", L0=1500, LL0=1.5, CL=1.05),
                 Table_2_9(profil="Л", L0=1500, LL0=2, CL=1.1),
                 Table_2_9(profil="Л", L0=1500, LL0=2.5, CL=1.15),
                 Table_2_9(profil="Л", L0=1500, LL0=3, CL=1.2),
                 Table_2_9(profil="Л", L0=1500, LL0=3.5, CL=1.25)]
        
        session.add_all(table_2_9)
        session.flush()
        session.commit()

def get_by_profil_L0_LL0(profil: str, L0: float, LL0: float) -> Table_2_9 | None:
    with sessionmanager.session() as session:
        return session.query(Table_2_9).filter(Table_2_9.profil == profil, Table_2_9.L0 == L0, Table_2_9.LL0 == LL0).first()