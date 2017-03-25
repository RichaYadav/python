import mysql.connector as mariadb


class database:

    def db_connect(self):
        mariadb_cnx = mariadb.connect(user='db_user', password='db_password', database='db_name')
        return mariadb_cnx
        print "connected"

    def db_table(self):
        create_string = (
            "CREATE TABLE `Jsondata` ("
            "  `artistId` varchar(14) ,"
            ") ENGINE=MariaDB")

        insert_string = ("INSERT INTO Jsondata "
                         "(kind)"
                         "VALUES (%(VALUE)s)")

        try:
            db_cnx = database().db_connect()
            cursor = db_cnx.cursor()
            print "db connected"
            cursor.execute(create_string)
            cursor.execute(insert_string)


        except mariadb.Error as error:
            print("Error: {}".format(error))

        else:
            print("Table created")

        cursor.close()
        db_cnx.close()


database().db_table()
