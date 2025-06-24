from database.DB_connect import DBConnect
from model.food import Food


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getNodes(calorie):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.food_id, f.food_code , f.display_name, f.calories  
                    from food f 
                    where f.calories > %s
                    """

        cursor.execute(query, (calorie,))

        for row in cursor:
            result.append(Food(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(calorie):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """with ingredienti as (select f.food_id, f.food_code , f.display_name, f.calories  
                    from food f 
                    where f.calories >%s)
                    select i1.food_id as n1, i2.food_id as n2,count(distinct fc.condiment_food_code) as peso
                    from ingredienti i1
                    join ingredienti i2 on i2.food_id != i1.food_id
                    join food_condiment fc on fc.food_code = i1.food_code
                    join food_condiment fc2 on fc2.food_code = i2.food_code
                    where fc2.condiment_food_code = fc.condiment_food_code
                    group by i1.food_id, i2.food_id 
                        """

        cursor.execute(query, (calorie,))

        for row in cursor:
            result.append((row['n1'], row['n2'], {'weight': row['peso']}))

        cursor.close()
        conn.close()
        return result