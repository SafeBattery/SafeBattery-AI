from dataclasses import dataclass
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Double, Integer

from flask_test import db


@dataclass
class PEMFC(db.Model):
    """
    +---------------+--------+------+-----+---------+----------------+
    | Field         | Type   | Null | Key | Default | Extra          |
    +---------------+--------+------+-----+---------+----------------+
    | id            | bigint | NO   | PRI | NULL    | auto_increment |
    | heater_power  | int    | NO   |     | NULL    |                |
    | pw            | double | NO   |     | NULL    |                |
    | p_air_inlet   | double | NO   |     | NULL    |                |
    | p_air_supply  | double | NO   |     | NULL    |                |
    | p_h2_inlet    | double | NO   |     | NULL    |                |
    | p_h2_supply   | double | NO   |     | NULL    |                |
    | rh_air        | double | NO   |     | NULL    |                |
    | rh_h2         | double | NO   |     | NULL    |                |
    | t_1           | double | NO   |     | NULL    |                |
    | t_2           | double | NO   |     | NULL    |                |
    | t_3           | double | NO   |     | NULL    |                |
    | t_4           | double | NO   |     | NULL    |                |
    | t_air_inlet   | double | NO   |     | NULL    |                |
    | t_h2_inlet    | double | NO   |     | NULL    |                |
    | t_heater      | double | NO   |     | NULL    |                |
    | t_stack_inlet | double | NO   |     | NULL    |                |
    | u_totv        | double | NO   |     | NULL    |                |
    | ia            | double | NO   |     | NULL    |                |
    | i_write       | double | NO   |     | NULL    |                |
    | m_air         | double | NO   |     | NULL    |                |
    | m_air_write   | double | NO   |     | NULL    |                |
    | m_h2          | double | NO   |     | NULL    |                |
    | m_h2_write    | double | NO   |     | NULL    |                |
    | tsec          | double | NO   |     | NULL    |                |
    +---------------+--------+------+-----+---------+----------------+
    """

    __table_name__ = "pemfc"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False
    )
    pw: Mapped[float] = mapped_column(nullable=False)
    p_air_inlet: Mapped[float] = mapped_column(nullable=False)
    p_air_supply: Mapped[float] = mapped_column(nullable=False)
    p_h2_inlet: Mapped[float] = mapped_column(nullable=False)
    p_h2_supply: Mapped[float] = mapped_column(nullable=False)
    rh_air: Mapped[float] = mapped_column(nullable=False)
    rh_h2: Mapped[float] = mapped_column(nullable=False)
    t_1: Mapped[float] = mapped_column(nullable=False)
    t_2: Mapped[float] = mapped_column(nullable=False)
    t_3: Mapped[float] = mapped_column(nullable=False)
    t_4: Mapped[float] = mapped_column(nullable=False)
    t_air_inlet: Mapped[float] = mapped_column(nullable=False)
    t_h2_inlet: Mapped[float] = mapped_column(nullable=False)
    t_heater: Mapped[float] = mapped_column(nullable=False)
    t_stack_inlet: Mapped[float] = mapped_column(nullable=False)
    u_totv: Mapped[float] = mapped_column(nullable=False)
    ia: Mapped[float] = mapped_column(nullable=False)
    i_write: Mapped[float] = mapped_column(nullable=False)
    m_air: Mapped[float] = mapped_column(nullable=False)
    m_air_write: Mapped[float] = mapped_column(nullable=False)
    m_h2: Mapped[float] = mapped_column(nullable=False)
    m_h2_write: Mapped[float] = mapped_column(nullable=False)
    tsec: Mapped[float] = mapped_column(nullable=False)
