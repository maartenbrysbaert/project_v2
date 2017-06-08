class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "maarten",
            "passwd": "password",
            "db": "securitycam"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getDataFromDatabase(self, table):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM {table}"
        sqlCommand = sqlQuery.format(table=table)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)
        
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def setDataToDatabase(self, table, column, value):
        # Query met parameters
        sqlQuery = "INSERT INTO {table} ({column}) VALUES ('{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(table=table, column=column, param1=value)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def updateData(self, table, column, value):
        # Query met parameters
        sqlQuery = "UPDATE {table} SET {column} = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(table=table, column=column, param1=value)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()