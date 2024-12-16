import math
from webbrowser import get
from bd_realization.constant_tables.table1_8 import get_by_HN_TM_TD
from bd_realization.constant_tables.table2_1 import get_by_profil_record
from bd_realization.constant_tables.table2_4 import get_by_alpha1
from bd_realization.constant_tables.table2_7 import get_by_profil_V_DP1
from bd_realization.constant_tables.table2_8 import get_by_profil_u
from bd_realization.constant_tables.table2_9 import get_by_profil_L0_LL0
from .models import Unit, AssemblyUnit, Part
from .database import sessionmanager

def generate_default() -> tuple[Unit, AssemblyUnit, Part, Part]:
    with sessionmanager.session() as session:
        stmt = session.query(Unit).order_by(Unit.id.desc()).first()
        if stmt is None:
            u_id = 0
        else:
            u_id = stmt.id
        u = Unit(id=u_id + 1)
        
        stmt = session.query(AssemblyUnit).order_by(AssemblyUnit.id.desc()).first()
        if stmt is None:
            a_id = 0
        else:
            a_id = stmt.id

        a = AssemblyUnit(id=a_id+1)
        a.unit_id = u.id
        a.NSE = "Передача"
        a.TSE = "Ременная"
        a.VSE = "Поликлиновая"

        p1 = Part()
        p1.assembly_unit_id = a.id
        p1.ND = "Ремень"

        p2 = Part()
        p2.assembly_unit_id = a.id
        p2.ND = "Шкив"

        return u, a, p1, p2

def calculate(u: Unit, a: AssemblyUnit, p1: Part, p2: Part) -> None:
    a.NV = a.N / p1.V
    a.F = 10**3 * a.NV
    
    request = get_by_profil_V_DP1(p1.profil, p1.V, p2.DP1)
    if request is None:
        print(p1.profil, p1.V, p2.DP1)
        raise ValueError("Не найдено соответствие в таблице 2.7")
    a.DF0 = request.DF0
    
    request = get_by_profil_u(p1.profil, a.u)
    if request is None:
        raise ValueError("Не найдено соответствие в таблице 2.8")
    a.dDFi = request.dDFi
    
    a.dDF0 = 100 * a.dDFi / p2.DP1
    
    request = get_by_alpha1(p2.alpha1)
    if request is None:
        raise ValueError("Не найдено соответствие в таблице 2.4")
    p1.C1 = request.C1
    
    request = get_by_HN_TM_TD(u.HN, u.TM, u.TD)
    if request is None:
        raise ValueError("Не найдено соответствие в таблице 1.8")
    a.C3 = request.C3
    
    p1.LL0 = p1.L / p1.L0
    
    request = get_by_profil_L0_LL0(p1.profil, p1.L0, p1.LL0)
    if request is None:
        raise ValueError("Не найдено соответствие в таблице 2.9")
    p1.CL = request.CL
    
    a.DF = (a.DF0 + a.dDF0) * p1.C1 * a.C3 * p1.CL
    
    p1.S10 = get_by_profil_record(p1.profil, "S10").value
    
    a.Z = int(10 * a.F / (p1.S10 * a.DF))

def save_values(n: Unit, a: AssemblyUnit, p1: Part, p2: Part) -> None:
    with sessionmanager.session() as session:
        session.add(n)
        session.add(a)
        session.add(p1)
        session.add(p2)
        session.flush()