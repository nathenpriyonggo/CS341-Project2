#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def First_Name(self):
      return self._First_Name
   
   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Phone(self):
      return self._Phone
      

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial,
                Last_Name, Suffix, Address_1, Address_2, City,
                State_Initial, Zip_Code, Country, Email, Phone, Fax, 
                Years_Registered, Employers, Total_Compensation):
      self._Lobbyist_ID = Lobbyist_ID
      self._Salutation = Salutation
      self._First_Name = First_Name
      self._Middle_Initial = Middle_Initial
      self._Last_Name = Last_Name
      self._Suffix = Suffix
      self._Address_1 = Address_1
      self._Address_2 = Address_2
      self._City = City
      self._State_Initial = State_Initial
      self._Zip_Code = Zip_Code
      self._Country = Country
      self._Email = Email
      self._Phone = Phone
      self._Fax = Fax
      self._Years_Registered = Years_Registered
      self._Employers = Employers
      self._Total_Compensation = Total_Compensation

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def Salutation(self):
      return self._Salutation
   
   @property
   def First_Name(self):
      return self._First_Name
      
   @property
   def Middle_Initial(self):
      return self._Middle_Initial
   
   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Suffix(self):
      return self._Suffix
   
   @property
   def Address_1(self):
      return self._Address_1
   
   @property
   def Address_2(self):
      return self._Address_2
   
   @property
   def City(self):
      return self._City
      
   @property
   def State_Initial(self):
      return self._State_Initial
   
   @property
   def Zip_Code(self):
      return self._Zip_Code
   
   @property
   def Country(self):
      return self._Country
   
   @property
   def Email(self):
      return self._Email
   
   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Fax(self):
      return self._Fax
      
   @property
   def Years_Registered(self):
      return self._Years_Registered
   
   @property
   def Employers(self):
      return self._Employers
   
   @property
   def Total_Compensation(self):
      return self._Total_Compensation


##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone,
                Total_Compensation, Clients):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def First_Name(self):
      return self._First_Name
   
   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Total_Compensation(self):
      return self._Total_Compensation
   
   @property
   def Clients(self):
      return self._Clients


##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):

   # SQL code for fetching number of lobbyists in the database
   sql = """
         SELECT COUNT(Lobbyist_ID)
         FROM LobbyistInfo
         """
   
   # Fetch number of lobbyist
   lobbyistNum = datatier.select_one_row(dbConn, sql)

   # Check for errors
   if lobbyistNum == None:
      return -1
   else:
      return lobbyistNum[0]


##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):

   # SQL code for fetching number of employers in the database
   sql = """
         SELECT COUNT(Employer_ID)
         FROM EmployerInfo
         """
   
   # Fetch number of employers
   employerNum = datatier.select_one_row(dbConn, sql)

   # Check for errors
   if employerNum == None:
      return -1
   else:
      return employerNum[0]
   

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   
   # SQL code for fetching number of clients in the database
   sql = """
         SELECT COUNT(Client_ID)
         FROM ClientInfo
         """
   
   # Fetch number of clients
   clientNum = datatier.select_one_row(dbConn, sql)

   # Check for errors
   if clientNum == None:
      return -1
   else:
      return clientNum[0]


##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):

   # SQL code for fetching number of lobbyists with matching pattern
   sql = """
         SELECT Lobbyist_ID, First_Name, Last_Name, Phone
         FROM LobbyistInfo
         WHERE First_Name LIKE ?
         OR Last_Name LIKE ?
         ORDER BY Lobbyist_ID ASC
         """
   
   # Fetch all lobbyists witch matching pattern
   rows = datatier.select_n_rows(dbConn, sql, [pattern, pattern])

   if rows == None:
      return None
   else:

      lobbyistList = []
      for row in rows:
         lobbyistList.append(Lobbyist(row[0], row[1], row[2], row[3]))

      return lobbyistList


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):

   # SQL code for fetching number of lobbyists with matching pattern
   sql = """
         SELECT Lobbyist_ID, Salutation, First_Name, Middle_Initial,
         Last_Name, Suffix, Address_1, Address_2, City, State_Initial,
         ZipCode, Country, Email, Phone, Fax
         FROM LobbyistInfo
         WHERE Lobbyist_ID LIKE ?
         """
   
   # Fetch partial lobbyists details witch matching pattern
   res = datatier.select_one_row(dbConn, sql, [lobbyist_id])

   if res == None or res == ():
      return None
   else:

      # SQL code for fetching years with matching lobbyists id
      sql = """
            SELECT Year
            FROM LobbyistYears
            WHERE Lobbyist_ID LIKE ?
            ORDER BY Year ASC
            """
      
      # Fetch list of years
      years = datatier.select_n_rows(dbConn, sql, [lobbyist_id])

      if years == None:
         return None
      
      yearsList = []
      for year in years:
         yearsList.append(year[0])

      # SQL code for fetching employer names with matching lobbyists id
      sql = """
            SELECT DISTINCT Employer_Name
            FROM EmployerInfo
            JOIN LobbyistAndEmployer
            ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
            WHERE Lobbyist_ID LIKE ?
            ORDER BY Employer_Name ASC
            """
      
      # Fetch list of employer names
      employers = datatier.select_n_rows(dbConn, sql, [lobbyist_id])

      if employers == None:
         return None

      employerNameList = []
      for employer in employers:
         employerNameList.append(employer[0])

      # SQL code for total amount of compensation with matching lobbyists id
      sql = """
            SELECT SUM(Compensation_Amount)
            FROM Compensation
            WHERE Lobbyist_ID LIKE ?
            """
      
      # Fetch total amount
      amount = datatier.select_one_row(dbConn, sql, [lobbyist_id])[0]

      if amount == None:
         amount = 0

      return LobbyistDetails(res[0], res[1], res[2], res[3], res[4], res[5],
                        res[6], res[7], res[8], res[9], res[10], res[11],
                        res[12], res[13], res[14], yearsList, employerNameList,
                        amount)
         

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
      
   # SQL code for fetching top N lobbyists with matching year
   sql = """
         SELECT Lobbyist_ID, SUM(Compensation_Amount) AS Total
         FROM Compensation
         WHERE strftime("%Y", Period_Start) = ?
         GROUP BY Lobbyist_ID
         ORDER BY Total DESC
         LIMIT ?
         """
   
   # Fetch list of top N lobbyists
   ids = datatier.select_n_rows(dbConn, sql, (year, N))

   if ids == None:
      return []
   else:
      
      topNLobbyistsList = []

      for idRow in ids:
         # SQL code for fetching lobbyist deatils with matching id
         sql = """
               SELECT Lobbyist_ID, First_Name, Last_Name, Phone
               FROM LobbyistInfo
               WHERE Lobbyist_ID = ?
               """
         
         # Fetch lobbyist details
         infos = datatier.select_one_row(dbConn, sql, [idRow[0]])

         # SQL code for fetching list of clients matching lobbyist id
         sql = """
               SELECT Client_Name
               FROM ClientInfo
               JOIN Compensation
               ON ClientInfo.Client_ID = Compensation.Client_ID
               WHERE Lobbyist_ID = ?
               AND strftime("%Y", Period_Start) = ?
               GROUP BY Compensation.Client_ID
               ORDER BY Client_Name ASC
               """
         
         # Fetch list of clients
         clients = datatier.select_n_rows(dbConn, sql, [idRow[0], year])

         clientsList = []
         for client in clients:
            clientsList.append(client[0])

         # Append LobbyistClients object to list
         topNLobbyistsList.append(LobbyistClients(infos[0], infos[1],
                                                  infos[2],infos[3], 
                                                  idRow[1], clientsList))
         
      return topNLobbyistsList


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):

   # SQL code for testing whether lobbyist id exists
   sql = """
         SELECT First_Name
         FROM LobbyistInfo
         WHERE Lobbyist_ID = ?
         """ 
   
   test = datatier.select_one_row(dbConn, sql, [lobbyist_id])

   # Check if lobbyist exists
   if test == ():
      return 0
   else:
      # SQL code for inserting given year into database
      sql = """
            INSERT INTO LobbyistYears(Lobbyist_ID, Year)
            VALUES (?, ?)
            """
      
      # Insert given year into databse
      rowCount = datatier.perform_action(dbConn, sql, [lobbyist_id, year])

      # Return 1 if updated succesfully
      if rowCount > 0:
         return 1
      else:
         return 0
   

##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):

   # SQL code for testing whether lobbyist id exists
   sql = """
         SELECT First_Name
         FROM LobbyistInfo
         WHERE Lobbyist_ID = ?
         """ 
   
   test = datatier.select_one_row(dbConn, sql, [lobbyist_id])

   # Check if lobbyist exists
   if test == ():
      return 0
   else:
      # SQL code for setting the salutation for given lobbyist
      sql = """
            UPDATE LobbyistInfo
            SET Salutation = ?
            WHERE Lobbyist_ID = ?
            """
      
      # Insert given year into databse
      rowCount = datatier.perform_action(dbConn, sql, [salutation, lobbyist_id])

      # Return 1 if updated succesfully
      if rowCount > 0:
         return 1
      else:
         return 0