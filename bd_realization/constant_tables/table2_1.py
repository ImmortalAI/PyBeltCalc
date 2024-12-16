from bd_realization.database import sessionmanager
from bd_realization.models import Table_2_1
def fill_table():
    with sessionmanager.session() as session:
        table_2_1 = [Table_2_1(profil="К", record="H", value=4),
                 Table_2_1(profil="К", record="delta", value=1.9),
                 Table_2_1(profil="К", record="h", value=2.15),
                 Table_2_1(profil="К", record="ht", value=3.3),
                 Table_2_1(profil="К", record="e", value=2.4),
                 Table_2_1(profil="К", record="S10", value=60),
                 Table_2_1(profil="К", record="L_min", value=450),
                 Table_2_1(profil="К", record="L_max", value=2000),
                 Table_2_1(profil="К", record="Dp", value=40),
                 Table_2_1(profil="К", record="q10", value=0.09),
                 Table_2_1(profil="К", record="V_max", value=35),
                 Table_2_1(profil="Л", record="H", value=9.5),
                 Table_2_1(profil="Л", record="delta", value=4.8),
                 Table_2_1(profil="Л", record="h", value=4.68),
                 Table_2_1(profil="Л", record="ht", value=6.6),
                 Table_2_1(profil="Л", record="e", value=4.8),
                 Table_2_1(profil="Л", record="S10", value=330),
                 Table_2_1(profil="Л", record="L_min", value=1250),
                 Table_2_1(profil="Л", record="L_max", value=4500),
                 Table_2_1(profil="Л", record="Dp", value=80),
                 Table_2_1(profil="Л", record="q10", value=0.45),
                 Table_2_1(profil="Л", record="V_max", value=35)]
        
        session.add_all(table_2_1)
        session.flush()
        session.commit()

def get_by_profil_record(profil: str, record: str) -> Table_2_1:
    with sessionmanager.session() as session:
        return session.query(Table_2_1).filter(Table_2_1.profil == profil, Table_2_1.record == record).first() # type: ignore