from bd_realization.database import sessionmanager
from bd_realization.models import Table_2_4
def fill_table():
    with sessionmanager.session() as session:
        table_2_4 = [Table_2_4(alpha1=70, C1=0.56),
                 Table_2_4(alpha1=80, C1=0.62),
                 Table_2_4(alpha1=90, C1=0.68),
                 Table_2_4(alpha1=100, C1=0.74),
                 Table_2_4(alpha1=110, C1=0.79),
                 Table_2_4(alpha1=120, C1=0.83),
                 Table_2_4(alpha1=130, C1=0.87),
                 Table_2_4(alpha1=140, C1=0.90),
                 Table_2_4(alpha1=150, C1=0.93),
                 Table_2_4(alpha1=160, C1=0.96),
                 Table_2_4(alpha1=170, C1=0.98),
                 Table_2_4(alpha1=180, C1=1)]
        
        session.add_all(table_2_4)
        session.flush()
        session.commit()

def get_by_alpha1(alpha1: float) -> Table_2_4 | None:
    with sessionmanager.session() as session:
        return session.query(Table_2_4).filter(Table_2_4.alpha1 == alpha1).first()