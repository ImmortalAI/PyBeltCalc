from bd_realization.database import sessionmanager
from bd_realization.models import Table_2_8
def fill_table():
    with sessionmanager.session() as session:
        table_2_8 = [Table_2_8(profil="К", u=1.05, dDFi=0.05),
                 Table_2_8(profil="К", u=1.2, dDFi=0.13),
                 Table_2_8(profil="К", u=1.5, dDFi=0.17),
                 Table_2_8(profil="К", u=3, dDFi=0.24),
                 Table_2_8(profil="Л", u=1.05, dDFi=0.06),
                 Table_2_8(profil="Л", u=1.2, dDFi=0.18),
                 Table_2_8(profil="Л", u=1.5, dDFi=0.28),
                 Table_2_8(profil="Л", u=3, dDFi=0.35)]
        
        session.add_all(table_2_8)
        session.flush()
        session.commit()

def get_by_profil_u(profil: str, u: float) -> Table_2_8 | None:
    with sessionmanager.session() as session:
        return session.query(Table_2_8).filter(Table_2_8.profil == profil, Table_2_8.u == u).first()