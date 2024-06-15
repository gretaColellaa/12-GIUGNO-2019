from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.ingrediente import Ingrediente


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi(calorie):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
                from condiment c 
                where c.condiment_calories <%s"""

        cursor.execute(query,(calorie,))

        for row in cursor:
            result.append(Ingrediente(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.i1 as v1,t2.i2 as v2, count(distinct t1.f1) as peso
from (select fc.food_code as f1, fc.condiment_code as i1
from food_condiment fc ) as t1,(select fc.food_code as f2, fc.condiment_code as i2
from food_condiment fc ) as t2
where t1.i1!=t2.i2 and t1.f1=t2.f2
group by t1.i1,t2.i2"""

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAll():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from condiment c"""

        cursor.execute(query)

        for row in cursor:
            result.append(Ingrediente(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNcibi(idcibo):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select count(distinct fc.food_code) as peso
from food_condiment fc 
where fc.condiment_code=%s
group by fc.condiment_code 
"""

        cursor.execute(query,(idcibo,))

        for row in cursor:
            result=row["peso"]

        cursor.close()
        conn.close()
        return result
