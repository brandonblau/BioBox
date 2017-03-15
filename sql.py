import MySQLdb

def lastEntry(database, table, col):

    if ((type(database) is str) & (type(table) is str) & (type(col) is str)):
        execute = "SELECT " + col + " FROM " + table + " ORDER BY DateTime DESC LIMIT 1;";
        connection = MySQLdb.connect(host= "localhost", user="root", passwd="raspberry", db=database);
        curs = connection.cursor();
        curs.execute(execute);
        connection.commit();
        data = curs.fetchone();
        return int(data[0]);
    else:
        return None;

def avgDailyValue(StringIn):
    #Server Connection to MySQL:
    conn = MySQLdb.connect(host= "localhost",
        user="root",
        passwd="raspberry",
        db="sensor_database")
    x = conn.cursor()
    try:
        execute = "SELECT Avg("+StringIn+") from plant_log where Date(DateTime) = CURDATE();"
        x.execute(execute)
        conn.commit()
        data = x.fetchone()
        avgValue = data[0]
    except:
        conn.rollback()
    conn.close();
    return avgValue

