import mysql.connector
from SqlConnection import getSqlConnection
def getAllStudents(cnx):
    
    
    mycursor = cnx.cursor()

    mycursor.execute("SELECT * FROM Students")
    response=[]
    for (StudentID,StudentName,StudentMobileNo) in mycursor:
        response.append(
            {'StudentID':StudentID, 'StudentName':StudentName, 'StudentMobileNo':StudentMobileNo}
            )
    return response

        

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
      
if __name__=='__main__':
    Connection=getSqlConnection()
    
    print(getAllStudents(Connection))
    
    
