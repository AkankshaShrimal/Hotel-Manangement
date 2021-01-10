# IMPORTING FILES 
import numpy as np
import pandas as pd
from datetime import date
from datetime import datetime
from pandas import option_context
from  dateutil import parser
from datetime import timedelta

path = './data/'
# Loading files 

class Load_data:
    def load(self):
        userTable = pd.read_csv(path + 'userTable.csv')
        hotelTable= pd.read_csv(path+ 'hotelTable.csv' )
        SingleRoom= pd.read_csv(path + 'SingleRoom.csv')
        DoubleRoom = pd.read_csv(path + 'DoubleRoom.csv')
        DuplexRoom = pd.read_csv(path + 'DuplexRoom.csv')
        BookingTable = pd.read_csv(path + 'BookingTable.csv')
        DatesMapping = pd.read_csv(path + 'DatesMapping.csv')
        return userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping

class Sign_up:
    def __init__(self,userTable):
        print("Hello from signup")
        self.user_id_all = userTable['user_id'].values
        # fetching all email id and all passwords 
        self.email_all = userTable['email'].values
        self.pass_all = userTable['password'].values 


    def find_present_or_not_1d(self,arr,val):
        boolVal = np.shape(np.where(arr == val)[0])[0]
        if boolVal: 
            return True
        else:
            return False


    def enter_details(self):
            new_id = self.user_id_all[-1] + 1 
            # check email , password number 
            name = input("Enter your Name : ")
            birth = input("Enter your DOB:'DD/MM/YYYY ")
            city = input("Enter your city : ")

            # checking if email already registered 
            email = input("Enter your email id : ")
            if self.find_present_or_not_1d(self.email_all, email):
                print('Email id already regestered please login')
                return

            # if password already matches some password 
            while(1):
                password = input("Enter your password (4 digit numbers) : ")
                password = int(password)
                if self.find_present_or_not_1d(self.pass_all , password):
                    print('Enter another password , this is already used')
                    continue 
                else:
                    break 
            self.newUser = {'user_id': new_id, 'name': name ,'email': email , 'password': password , 'city':city , 'DOB':birth }
            return self.newUser 

    def confirm_details_create_id(self,userTable):

            print("\n\n Following are the details ")
            print("Select one choice")
            print("1. Confirm and Create")
            print("2. Exit ")

            print("\n")
            for key in self.newUser.keys():
                if key is not 'user_id':
                    print(key + " : " + str(self.newUser[key]))

            choice = input("Enter your choice : ")
            if (choice == "1"):
                print("Your new id is :" + str(self.newUser['user_id']))
                userTable = userTable.append(self.newUser , ignore_index=True)
                userTable.to_csv(path + 'userTable.csv' ,  index=False)
                print(" Signup success")
                print(" Login again to continue !")
                return True
                
            else:
                print("User not signed up")
                return False

    def apply_sign_up(self,userTable):
        newUser = self.enter_details()
        if newUser : 
            self.confirm_details_create_id(userTable)

    
class Login:
    def __init__(self,userTable):
        print("Hello from User")
        self.user_id_all = userTable['user_id'].values
        # fetching all email id and all passwords 
        self.email_all = userTable['email'].values
        self.pass_all = userTable['password'].values 

    def find_first_index_in_1d(self,arr, val):
        return np.where(arr == val)[0][0]
    
    def enter_credentials(self):
            print("Enter details to login")
            # type and digits check , check not empty 
            id = input("Enter your user id : ")
            password = input("Enter your 4 digit password : ")
            return id, password 

    def find_present_or_not_1d(self,arr,val):
        boolVal = np.shape(np.where(arr == val)[0])[0]
        if boolVal: 
            return True
        else:
            return False

    def check_Validity(self,id, password):
        if id and password:
            # checking if user is valid or not
            id = int(id)
            password = int(password)
            # user and password present in table or not 
            if (self.find_present_or_not_1d(self.user_id_all, id)) and (self.find_present_or_not_1d(self.pass_all , password)):
            # if user id matches to that password
                if  (self.find_first_index_in_1d(self.user_id_all, id) == self.find_first_index_in_1d(self.pass_all , password)):
                    print("Login Successful")
                    return id 
                else:
                    print('Invalid Details')
                    return 
        else:
            print('Invalid Details')
            return 

    def apply_login(self):
        id , password = self.enter_credentials()
        user_id = self.check_Validity(id,password)
        return user_id 


class User:
    def __init__(self,uid):
        self.uid = uid

class Hotel:
    def __init__(self,id,hotel_name,location,Area,Category,Covid_Hygiene_Rating,Covid_zones,Maximum_Offer,price_range_start,price_range_end ):
        self.hotel_id = id 
        self.hotel_name = hotel_name
        self.location = location
        self.Area = Area
        self.Category = Category
        self.Covid_Hygiene_Rating = Covid_Hygiene_Rating 
        self.Covid_zones = Covid_zones
        self.Maximum_Offer = Maximum_Offer
        self.price_range_start = price_range_start
        self.price_range_end = price_range_end
        


class Date:
    def __init__(self,DMY):
        self.DMY = DMY

    def check_Date_Format(self):
        try:
            bookDate = datetime(self.DMY[2],self.DMY[1], self.DMY[0])
            correctDate = True
        except ValueError:
            correctDate = False
        return correctDate,bookDate


class Booking_receipt:
    def displaying_final_bill(self,booking):
        booking.displaying_final_bill()
        
class get_search_values:
    searchValues = {}

    def select_date(self):
        while(1):
            startValue = input('\nEnter Start Date in the format DD/MM/YYYY : ')
            DMY = [int(i) for i in startValue.split('/')]
            temp_date = Date(DMY)
            correctDate,startDate = temp_date.check_Date_Format()

            # check if date is not a past date 
            curr_date = datetime.now()
            if correctDate:
                if startDate > curr_date:
                    break 
                else:
                    print("\nEnter a date in future ") 
            else:
                print("\nDate not correct ")

        while(1):
            endValue = input('\nEnter End Date in the format DD/MM/YYYY : ')
            DMY = [int(i) for i in list(endValue.split('/'))]
            temp_date = Date(DMY)

            correctDate,endDate = temp_date.check_Date_Format()

            # check if date is not a past date 
            curr_date = datetime.now()
            if correctDate:
                if (endDate > curr_date and endDate >= startDate):
                    break 
                else:
                    print("\nEnter a date in future ") 
            else:
                print("\nDate not correct ")
        
        self.searchValues = {'startDate' : startDate , 'endDate': endDate}
        

    def dacation_nightout(self):
        print("\nSelect Dacation or Nighout or Both")
        print("Choices are : ")
        print("1. Dacation ")
        print("2. Nightout ")
        print("3. Both ")

        if (self.searchValues['endDate'].date() == self.searchValues['startDate'].date()):
            # If startDate and endDate same ask only once for choice 
            while(1):
                choice = input("Enter you choice  : ")
                start_Val = -1
                
                if (choice == '1'):
                    start_Val = 9
                    break
                elif (choice == '2'):
                    start_Val = 21
                    break
                elif (choice == '3'):
                    start_Val = 23
                    break
                else:
                    continue

            end_Val = start_Val
        else:
            while(1):
                choice = input("Enter you choice for Start Date : ")
                start_Val = -1
                end_Val = -1

                if (choice == '1'):
                    start_Val = 9
                    break
                elif (choice == '2'):
                    start_Val = 21
                    break
                elif (choice == '3'):
                    start_Val = 23
                    break
                else:
                    continue

            while(1):
                choice = input("\nEnter you choice for End Date : ")
                if (choice == '1'):
                    end_Val = 9
                    break 
                elif (choice == '2'):
                    end_Val = 21
                    break
                elif (choice == '3'):
                    end_Val = 23
                    break
                else:
                    continue

        self.searchValues["startTime"] = start_Val
        self.searchValues["endTime"] = end_Val
        self.searchValues["startDate"] = self.searchValues["startDate"].replace(hour=start_Val, minute=0, second=0)
        self.searchValues["endDate"] = self.searchValues["endDate"].replace(hour=end_Val, minute=0, second=0)
        
    
    def select_location(self):
        # select the appropriate location 
        print("Select Location for Booking : ")
        print("1. Jaipur ")
        print("2. Delhi ")

        while(1):
            choice = input(" select one among above : ")
            if (choice == "1"):
                self.searchValues["location"] = "Jaipur"
                break
            elif (choice == "2"):
                self.searchValues["location"] = "Delhi"
                break
            else:
                print("Not valid ,Choose again! ")
                continue 
        

    def apply_searchValues(self):
        self.select_date()
        self.dacation_nightout()
        self.select_location()
        return self.searchValues

    
class Filters:
    def display_filters(self,searchValues):
            # Apply filters to put into searching of hotels 
            # find areas according to location 
            Location_areas = { 'Jaipur': ['(1)Baisgodam' , '(2)Malwiya Nagar'], 'Delhi': ['(1)Gandhi Nagar', '(2)Rohini']}
            select_areas = ','.join(Location_areas[searchValues['location']])
            # Display filters 
            filterVal = {'filters': ['Area', 'Category(stars)', 'Covid Hygiene Rating', 'Maximum Offer', 'Price-Range','Covid-19 zones'],
                        'values' : [ select_areas  , '(1)1, (2)2, (3)3, (4)4, (5)5', '(1)1, (2)2, (3)3, (4)4, (5)5',  '(1)20-40 ,(2)40-60,(3)60-100'
                                    , '(1)0-10000, (2)2000-15000, (3)5000-20000', '(1)Red, (2)Green, (3)Orange' ]}

            filters_df = pd.DataFrame(filterVal)
            filters_df.index = np.arange(1, len(filters_df)+1)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
                print(filters_df)

            self.filterVal = filterVal
            self.searchValues = searchValues

    def select_filters(self):
            print("Enter the filters you want by index and comma separated :-")
            filterIndex = input("Enter comma separated index values : ")
            filters_all = [ self.filterVal['filters'][int(i)-1] for i in filterIndex.split(',')]

            dictFilter = {}
            # Enter filters values among filters choosen 
            for idx in filterIndex.split(','):
                idx = int(idx) - 1
                filterName = self.filterVal['filters'][idx]
                options = [op for op in self.filterVal['values'][idx].split(',')]

                print("Select one among choices given for " , filterName)
                val = int(input())
                
                try:
                    print("selected :" , options[val-1].split(')')[1])
                    dictFilter[filterName] = options[val-1].split(')')[1]
                except IndexError:
                    print(" There is no such index for this filter so default first entry taken")
                    dictFilter[filterName] = options[0].split(')')[1]

            # displaying values of each filter 
            print(" FILTERS SELECTED ARE:")
            for key in dictFilter.keys():
                print(key , dictFilter[key])

            # changing dict filter to run the searching queries , converting string to number , range to list [start,end]
            numericCol = ['Category(stars)','Covid Hygiene Rating']
            rangeCol = ['Maximum Offer','Price-Range'] 

            for key in dictFilter.keys():
                if key in numericCol:
                    dictFilter[key] = int(dictFilter[key])
                elif key in rangeCol:
                    l =  dictFilter[key].split('-')
                    dictFilter[key] = [int(i) for i in l]

            self.dictFilter = dictFilter
            

    def apply_filters(self,searchValues):
        self.display_filters(searchValues)
        self.select_filters()
        return self.dictFilter


class Display_hotels:
    # function to sort the hotels and display 
    def __init__(self, searchValues , dictFilter):
        self.searchValues = searchValues
        self.dictFilter = dictFilter

    def sort_hotels(self,hotelNames):
        # sort the results by price low to high or high to low 
        print(" Hello , select one choice to sort minimum price value")
        print("1. Minimum Price Low  to How")
        print("2. Minimum Price High to Low")
        choice = input()

        if choice == "1":
            hotelNames = hotelNames.sort_values(by = ['price_range_start'])
        else:
            hotelNames = hotelNames.sort_values(by = ['price_range_start'], ascending=False)

        print("Hotel Names after sorting are : ")
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(hotelNames)

    def apply_display_hotels(self,hotelTable ):
        # searching by filters 
        # location search 
        hotelNames = hotelTable[hotelTable['location'] == self.searchValues['location']]
        # search by filters selected before 
        for key in self.dictFilter.keys():
            if key !='Maximum Offer' and key !='Price-Range':
                hotelNames = hotelNames[hotelNames[key] == self.dictFilter[key]]
            
            elif key == 'Maximum Offer':
                hotelNames = hotelNames[(hotelNames[key] >= self.dictFilter[key][0]) & (hotelNames[key] <= self.dictFilter[key][1])]
            
            elif key == 'Price-Range':
                hotelNames = hotelNames[(hotelNames['price_range_start'] >= self.dictFilter[key][0]) & (hotelNames['price_range_end'] <= self.dictFilter[key][1])]
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(hotelNames)
        self.sort_hotels(hotelNames)


class Select_hotel:
    def apply_select_hotel(self,hotelTable):
        # Enter from search only expected , or checked if such hotel id exists or not 
        while(1):
            hotel_id = input("Enter the hotel id to be selected : ")
            hotel_id = int(hotel_id)

            # check if hotel id exists or not else keep on typing hotel id
            df = hotelTable[hotelTable["hotel_id"] == hotel_id]
            if not df.empty:
                break
            else:
                print("Enter valid hotel id")
                continue 
        return hotel_id

class Calculate_availability:
    def __init__(self, hotel_id, searchValues):
        self.hotel_id  = hotel_id
        self.searchValues = searchValues

    def check_avail_one(self, data):
        for key in data.keys():
            if self.searchValues['startTime'] == 9:
                return data[key][0]
            elif self.searchValues['startTime'] == 21:
                return data[key][1]
            elif self.searchValues['startTime'] == 23:
                return min(data[key][0],data[key][0])
            # If date is only one date

    def check_avail_range(self,data):
      # If dates are a range 
      temp = []
      for key in data.keys():
        if key == self.searchValues['startDate'].date():
          if self.searchValues['startTime'] == 9 or self.searchValues['startTime'] == 23:
            temp.append(data[key][0])
            temp.append(data[key][1])
          elif self.searchValues['startTime'] == 21:
            temp.append(data[key][1])
        elif key == self.searchValues['endDate'].date():
          if self.searchValues['startTime'] == 21 or self.searchValues['startTime'] == 23:
            temp.append(data[key][0])
            temp.append(data[key][1])
          elif self.searchValues['startTime'] == 9:
            temp.append(data[key][0])
        else:
          temp.append(data[key][0])
          temp.append(data[key][1])
          
      return min(temp)

    def change(self,rooms,singleDict ,doubleDict , duplexDict,date,d,roomType):
      if roomType == 1:
        temp = singleDict[date[d]]
        temp = [ t-rooms for t in temp]
        singleDict[date[d]] = temp
      elif roomType == 2:
        temp = doubleDict[date[d]]
        temp = [ t-rooms for t in temp]
        doubleDict[date[d]] = temp
      elif roomType == 3:
        temp = duplexDict[date[d]]
        temp = [ t-rooms for t in temp]
        duplexDict[date[d]] = temp 

      return singleDict ,doubleDict , duplexDict

    
    def change_0(self,rooms,singleDict ,doubleDict , duplexDict,date,d,roomType):
      if roomType == 1:
        temp = singleDict[date[d]][0]
        temp = temp -rooms
        singleDict[date[d]][0] = temp
      elif roomType == 2:
        temp = doubleDict[date[d]][0]
        temp = temp -rooms
        doubleDict[date[d]][0] = temp
      elif roomType == 3:
        temp = duplexDict[date[d]][0]
        temp = temp -rooms
        duplexDict[date[d]][0] = temp
      return singleDict ,doubleDict , duplexDict

    def change_1(self,rooms,singleDict ,doubleDict , duplexDict,date,d,roomType):
      if roomType == 1:
        temp = singleDict[date[d]][1]
        temp = temp - rooms
        singleDict[date[d]][1] = temp
      elif roomType == 2:
        temp = doubleDict[date[d]][1]
        temp = temp - rooms
        doubleDict[date[d]][1] = temp
      elif roomType == 3:
        temp = duplexDict[date[d]][1]
        temp = temp - rooms
        duplexDict[date[d]][1] = temp   
      return singleDict ,doubleDict , duplexDict

    
    def find_room_number(self,df, id):
      df = df[df["hotel_id"] == id]
      room = df["Number of Room"]
      return int(room)

    def apply_calcualte_availability(self,SingleRoom, DoubleRoom, DuplexRoom,DatesMapping):
        # Total rooms of each type in respective hotel 
        roomNo = [0,0,0]
        roomNo[0] = self.find_room_number(SingleRoom , self.hotel_id)
        roomNo[1] = self.find_room_number(DoubleRoom , self.hotel_id)
        roomNo[2] = self.find_room_number(DuplexRoom , self.hotel_id)

        # ALL DATES 
        # if start and end date are same only one date 
        # else both are diff so range of dates 

        sameDay = self.searchValues["startDate"].date() == self.searchValues["endDate"].date()
        # Storing all dates in range of start and end for a booking 
        if sameDay: 
            date = [self.searchValues["startDate"].date()]
        else:
            flag = True
            d = self.searchValues["startDate"].date()
            date = []
            while(flag):
                date.append(d)
                d += timedelta(days=1)
                if d ==  self.searchValues["endDate"].date()+timedelta(days=1):
                    flag = False

        
        # storing total room values for each room type 
        singleDict = {}
        doubleDict = {}
        duplexDict = {}

        for d in date: 
            singleDict[d] = [roomNo[0] ,roomNo[0]] 
            doubleDict[d] = [roomNo[1],roomNo[1]] 
            duplexDict[d] = [roomNo[2] ,roomNo[2]]

        #CLACULATING NO OF ROOMS FOR RESPECTIVE ROOMS 

        # booking detail ( for belonging to that hotel and not using booking from dates before than start date)
        bookingDetail = DatesMapping[DatesMapping["hotel_id"] == self.hotel_id]
        bookingDetail = bookingDetail[bookingDetail["end_Date"] >= str(self.searchValues["startDate"].replace(hour=0))]


        for d in range(len(date)):
        
            for i in range(len(bookingDetail)):
                start =  parser.parse(bookingDetail.iloc[i,0])
                end = parser.parse(bookingDetail.iloc[i,1])
                start_time = parser.parse(bookingDetail.iloc[i,0]).hour
                end_time = parser.parse(bookingDetail.iloc[i,1]).hour
                rooms = bookingDetail.iloc[i,6]
                roomType = bookingDetail.iloc[i,5]

                if (start.date() == end.date()):
                    if (date[d] == start.date()):
                    # if for start date only night booked 
                    
                        if start_time == 21:
                            singleDict ,doubleDict , duplexDict= self.change_1(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
                        elif start_time == 9:
                            singleDict ,doubleDict , duplexDict= self.change_0(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
                        elif  start_time == 23:
                            singleDict ,doubleDict , duplexDict= self.change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)

                else:
                
                    if (date[d] == start.date()):
                        # if for start date only night booked 
                        if start_time == 21:
                            singleDict ,doubleDict , duplexDict= self.change_1(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
                        elif start_time == 9 or start_time == 23:
                            singleDict ,doubleDict , duplexDict= self.change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)

                    elif (date[d] == end.date()):
                        if end_time == 9:
                            singleDict ,doubleDict , duplexDict= self.change_0(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
                        elif end_time == 21 or end_time == 23:
                            singleDict ,doubleDict , duplexDict= self.change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
                    
                    elif (start.date() < date[d] < end.date()):
                        
                        singleDict ,doubleDict , duplexDict= self.change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)

        #   # if current date is in middle of any date ranges of course one day and one night deleted from total available 
            #   # Process repeated for all room types

        # Calculation of number of rooms available finally 
        if sameDay:
            SR = self.check_avail_one(singleDict)
            DR = self.check_avail_one(doubleDict)
            DUR = self.check_avail_one(duplexDict)
        else:
            SR = self.check_avail_range(singleDict)
            DR = self.check_avail_range(doubleDict)
            DUR = self.check_avail_range(duplexDict)

        if SR < 0:
            SR = 0
        if DR < 0:
            DR = 0
        if DUR < 0:
            DUR = 0
        return SR,DR,DUR


class Display_calculate_availability:
    def __init__(self,hotel_id, SR,DR,DUR):
        self.hotel_id = hotel_id
        self.SR = SR
        self.DR = DR
        self.DUR = DUR

    def apply_display(self,SingleRoom, DoubleRoom, DuplexRoom):
        SRO = SingleRoom[SingleRoom['hotel_id'] == self.hotel_id]['Offers'][0]
        SRP = SingleRoom[SingleRoom['hotel_id'] == self.hotel_id]['Price'][0]

        DRO = DoubleRoom[DoubleRoom['hotel_id'] == self.hotel_id]['Offers'][0]
        DRP = DoubleRoom[DoubleRoom['hotel_id'] == self.hotel_id]['Price'][0]

        DURO = DuplexRoom[DuplexRoom['hotel_id'] == self.hotel_id]['Offers'][0]
        DURP = DuplexRoom[DuplexRoom['hotel_id'] == self.hotel_id]['Price'][0]

        avail = [self.SR,self.DR,self.DUR]
        offer = [SRO,DRO,DURO]
        price = [SRP, DRP, DURP]

        DisplayDict = {"Availability" : avail , "Offer": offer , "Price": price}
        df = pd.DataFrame(DisplayDict, index=['Single Room', 'Double Room', 'Duplex Room'])
        print(df)
        return avail

class Select_room:
    def __init__(self,avail):
        self.avail = avail 

    def apply_select_room(self):
      while(1):
        print("select one among following option ")
        print("1. Single Room")
        print("2. Double Room")
        print("3. Duplex Room")
        print("4. Exit")
        
        choice = input()

        if (choice == "1"):
          # check availability of room
          if self.avail[int(choice)-1] == 0:
            print("Availability is zero choose any other ")
            continue 
          # Input nuber of rooms of that type 
          while(1):
            no_of_rooms = input("Enter no of rooms you want according to availability ")
            if (int(no_of_rooms) <= self.avail[int(choice)-1]):
              break 
          roomType = 1
          break 

        elif (choice == "2"):
          if self.avail[int(choice)-1] == 0:
            print("Availability is zero choose any other ")
            continue 
          # Input nuber of rooms of that type  
          while(1):
            no_of_rooms = input("Enter no of rooms you want according to availability ")
            
            if int(no_of_rooms) <= self.avail[int(choice)-1]:
              
              break  
          roomType = 2
          break 

        elif (choice == "3"):
          if self.avail[int(choice)-1] == 0:
            print("Availability is zero choose any other ")
            continue 
          # Input nuber of rooms of that type 
          while(1):
            no_of_rooms = input("Enter no of rooms you want according to availability ")
            if (int(no_of_rooms) <= self.avail[int(choice)-1]):
              break 
          roomType = 3
          break 
        elif (choice == "4"):
          roomType = None
          no_of_rooms = None 
          break 

      return roomType , no_of_rooms

class Room:
    def __init__(self,hotel_id,no_of_rooms,Offers,Price):
        self.hotel_id = hotel_id
        self.no_of_rooms = no_of_rooms
        self.Offers = Offers 
        self.Price = Price 


class Single_Room(Room):
    def __init__(self,hotel_id,no_of_rooms,Offers,Price,type):
        super().__init__(hotel_id,no_of_rooms,Offers,Price)
        self.type_of_room = 1


class Double_Room(Room):
    def __init__(self,hotel_id,no_of_rooms,Offers,Price,type):
        super().__init__(hotel_id,no_of_rooms,Offers,Price)
        self.type_of_room = 1

class Duplex_Room(Room):
    def __init__(self,hotel_id,no_of_rooms,Offers,Price,type):
        super().__init__(hotel_id,no_of_rooms,Offers,Price)
        self.type_of_room = 1


# class Search_hotels:
#     def __init__(self,userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping):
#         print("WELCOME TO SEARCH HOTELS")
#         self.userTable = userTable
#         self.hotelTable = hotelTable
#         self.SingleRoom = SingleRoom
#         self.DoubleRoom = DoubleRoom
#         self.DuplexRoom = DuplexRoom
#         self.BookingTable = BookingTable
#         self.DatesMapping = DatesMapping

#     def apply_search_hotels(self):
#         search_obj = get_search_values()
#         self.searchValues = search_obj.apply_searchValues

#         filter_obj = Filters()
#         self.dictFilter = filter_obj.apply_filters(self.searchValues)

#         display_obj = Display_hotels(self.hotelTable , self.searchValues , self.dictFilter)
#         display_obj.apply_display_hotels()

#         select_hotel_obj = Select_hotel()
#         hotel_id = select_hotel_obj.apply_select_hotel(self.hotelTable)









#####################################
##RR##
#####################################
class Additional_Facilities:
    def __init__(self):
        self.laundry = 0
        self.additional_sanitizers = 0
        self.masks = 0
        self.face_shields = 0
        
    def choose_additional_facilities(self):
        while(1):
            print("Please enter any additinal services you want with your bookings :")
            print("1. Laundry")
            print("2. Additional Sanitizers")
            print("3. Masks")
            print("4. Face shield")
            print("5. No additional services")
            print("6. Done ordering")
            choice = 0
            choice = input("Enter your choice :")
            choice = int(choice)
            if choice == 1:
                self.laundry = 1
            elif choice == 2:
                self.additional_sanitizers = int(input("Enter the number of additional sanitizers"))
            elif choice == 3:
                self.masks = int(input("Enter the number of additional masks"))
            elif choice == 4:
                self.face_shields = int(input("Enter the number of additional face_shields"))
            elif choice == 5:
                print("No additional servies added")
                break
            elif choice == 6:
                break
            else:
                print("Please enter correct choice")

        return (self.laundry,self.additional_sanitizers,self.masks,self.face_shields)
        
    
class Booking:
    def __init__(self):
#        self.hotel_id = hotel_id
#        self.no_of_rooms = no_of_rooms
#        self.Offers = Offers
#        self.Price = Price
#        self.type = type
        self.review = ""
        self.payment_pending = 0

        self.laundry = 0
        self.laundry_cost = 0

        self.additional_sanitizers = 0
        self.additional_sanitizers_cost = 0

        self.masks = 0
        self.masks_cost = 0

        self.face_shields = 0
        self.face_shields_cost = 0

        self.num_of_room_available = 0
        
        
        
        self.cost_of_room = 0 #to be calculated during amount calculation
        self.one_room_price = 0
        self.offer = 0
        
        self.amount = 0
        
        self.hotel_details_from_hotel_id = 0
        
    def booking_function(self,BookingTable,user_id,hotel_id,location,no_of_rooms,type_of_room,start_date,end_date):
#       userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
#       below one is the new line to load data
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
        if type_of_room == 1:
            type_of_room = 'SingleRoom'
        elif type_of_room == 2:
            type_of_room = 'DoubleRoom'
        elif type_of_room == 3:
            type_of_room = 'DuplexRoom'

  
        booking_id = 0
        if BookingTable.empty == True:
            booking_id = 1
        else:
            BookingTable.sort_values('booking_id')
            booking_id = pd.DataFrame(BookingTable['booking_id'])
            booking_id = int(booking_id.iloc[-1]) + 1




        Additional_Facilities_obj = Additional_Facilities()
        (self.laundry,self.additional_sanitizers,self.masks,self.face_shields)  = Additional_Facilities_obj.choose_additional_facilities()
  
  
  
  #below few lines will calculate amount to be paid by user


  #below comment just for reference delete it
  #booking_id    user_id    hotel_id    Location    Area    No of rooms  Type of Room  start    end    amount    review    Payment_pending    laudary    additional sanitizers    masks    face shield
  
  
  
  #fetch details of hotel from hotel id
        self.hotel_details_from_hotel_id = hotelTable.loc[hotelTable['hotel_id']==hotel_id]

  #fetch details of singleRoom, DoubleRoom, DuplexRoom from hotel id
        if type_of_room == 'SingleRoom':
            single_room_details_from_hotel_id = SingleRoom.loc[SingleRoom['hotel_id']==hotel_id]
            single_room_details_from_hotel_id = single_room_details_from_hotel_id.reset_index()
            self.one_room_price = single_room_details_from_hotel_id['Price'][0]
            self.offer = single_room_details_from_hotel_id['Offers'][0]
            self.num_of_room_available = single_room_details_from_hotel_id['Number of Room'][0]
            # print(single_room_details_from_hotel_id)
        elif type_of_room == 'DoubleRoom':
            double_room_details_from_hotel_id = DoubleRoom.loc[DoubleRoom['hotel_id']==hotel_id]
            double_room_details_from_hotel_id = double_room_details_from_hotel_id.reset_index()
            self.one_room_price = double_room_details_from_hotel_id['Price'][0]
            self.offer = double_room_details_from_hotel_id['Offers'][0]
            self.num_of_room_available = double_room_details_from_hotel_id['Number of Room'][0]
        elif type_of_room == 'DuplexRoom':
            duplex_room_details_from_hotel_id = DuplexRoom.loc[DuplexRoom['hotel_id']==hotel_id]
            duplex_room_details_from_hotel_id = duplex_room_details_from_hotel_id.reset_index()
            self.one_room_price = duplex_room_details_from_hotel_id['Price'][0]
            self.offer = duplex_room_details_from_hotel_id['Offers'][0]
            self.num_of_room_available = duplex_room_details_from_hotel_id['Number of Room'][0]

        #calculating addtional requirement price
        hotel_details_from_hotel_id = hotelTable.loc[hotelTable['hotel_id']==hotel_id]
        hotel_details_from_hotel_id = hotel_details_from_hotel_id.reset_index()
        # print(self.laundry , hotel_details_from_hotel_id['laundry'][0] , "hello")
        self.laundry_cost = self.laundry * hotel_details_from_hotel_id['laundry'][0]
        self.additional_sanitizers_cost = self.additional_sanitizers * hotel_details_from_hotel_id['additional sanitizers'][0]
        self.masks_cost = self.masks * hotel_details_from_hotel_id['masks'][0]
        self.face_shields_cost = self.face_shields * hotel_details_from_hotel_id['face shield'][0]

        #applying offer on one room price
        self.one_room_price = self.one_room_price - (self.one_room_price*self.offer)/100
        self.one_room_price = int(self.one_room_price)

        #calculating cost of room
        self.cost_of_room = (no_of_rooms * self.one_room_price )

        #calculating final amount to be paid by user after discount
        self.amount =  self.cost_of_room + self.laundry_cost + self.additional_sanitizers_cost + self.masks_cost + self.face_shields_cost

        if type_of_room == 'SingleRoom':
            type_of_room = int(1)
        elif type_of_room == 'DoubleRoom':
            type_of_room = int(2)
        elif type_of_room == 'DuplexRoom':
            type_of_room = int(3)
        #creating a temp Series to be put into DataFrame
        temp = {'booking_id':booking_id, 'user_id':user_id, 'hotel_id':hotel_id, 'Location':location, 'No of rooms':no_of_rooms, 'Type of Room':type_of_room, 'start':start_date, 'end':end_date, 'amount':self.amount,  'review':self.review ,'Payment_pending':self.payment_pending ,'laundry':self.laundry ,'additional sanitizers':self.additional_sanitizers ,'masks':self.masks ,'face shield':self.face_shields  }
        BookingTable = BookingTable.append(temp,ignore_index=True)
        BookingTable.to_csv(path + 'BookingTable.csv' ,  index=False)

        # write table to database

        temp2 = {'start_Date':start_date, 'end_Date':end_date, 'booking_id':booking_id, 'hotel_id':hotel_id, 'user_id':user_id, 'roomType':type_of_room, 'No of rooms': no_of_rooms  }
        DatesMapping = DatesMapping.append(temp2,ignore_index=True)
        DatesMapping.to_csv(path + 'DatesMapping.csv' ,  index=False)

    def displaying_final_bill(self):
        print("-------Your final bill---------")
        print("laundry_cost : ",self.laundry_cost)
        print("additional_sanitizers_cost : ",self.additional_sanitizers_cost)
        print("masks_cost : ",self.masks_cost)
        print("face_shields_cost : ",self.face_shields_cost)
        print("one_room_price : ",self.one_room_price)
        print("cost_of_room : ",self.cost_of_room)
        print("Total Amount : ",self.amount)
    
    def booking_confirmation(self):
        print("Your booking has been confirmed please proceed to payment.")
  
  
#ABSTRACT METHODS
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    # abstract method
    def typeofpayment(self):
        pass
  
class VISA(PaymentMethod):
  
    # overriding abstract method
    def typeofpayment(self):
        print("1. VISA Debit Card used")
  
class Mastercard(PaymentMethod):
  
    # overriding abstract method
    def typeofpayment(self):
        print("2. Mastercard Debit Card used")
        
class Rupay(PaymentMethod):
  
    # overriding abstract method
    def typeofpayment(self):
        print("3. Rupay used")
        
class NetBanking(PaymentMethod):
  
    # overriding abstract method
    def typeofpayment(self):
        print("4. Net Banking used")
        
class Credit(PaymentMethod):
  
    # overriding abstract method
    def typeofpayment(self):
        print("5. Credit Card used")
        
        
        
class PaymentMethods:
    def __init__(self):
        self.choose = 0
        
    def choose_payment_method(self):
        print("Choose payment method : ")
        print("1. VISA Debit Card")
        print("2. Mastercard Debit")
        print("3. Rupay")
        print("4. Net Banking")
        print("5. Credit Card")
        self.choose = int(input("Enter your choice : "))
        if self.choose == 1:
            VISA_obj = VISA()
            VISA_obj.typeofpayment()
        elif self.choose == 2:
            Mastercard_obj = Mastercard()
            Mastercard_obj.typeofpayment()
        elif self.choose == 3:
            Rupay_obj = Rupay()
            Rupay_obj.typeofpayment()
        elif self.choose == 4:
            NetBanking_obj = NetBanking()
            NetBanking_obj.typeofpayment()
        elif self.choose == 5:
            Credit_obj = Credit()
            Credit_obj.typeofpayment()



class Payment:
    def __init__(self,user_id):
        self.booking_values = 0
        self.user_id = user_id
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
    
    def display_pending_payment(self,user_id):
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
        self.flag = True
        temp = BookingTable.loc[BookingTable['user_id']==user_id]
        cur_date = datetime.now()
        temp = temp[temp['start'] > str(cur_date)]

        if temp.empty:
            print('No Pending Payment')
            self.flag = False
            # flag = False
        else:
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            print(temp)
            self.flag = True
        self.booking_values = temp['booking_id'].values
    
    def select_booking_for_payment(self):
        booking_id = int(input("Enter booking id to proceed with payment :"))
        return booking_id
        
    def make_payment(self):
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
        while(1):
          booking_id = self.select_booking_for_payment()
      
          print("Enter -1 to exit out of payment")
          if booking_id == -1:
            break
          #for checking payment pending
          if booking_id not in self.booking_values:
            print("Please enter correct booking id")
          else:
            bt = BookingTable.loc[ (BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==self.user_id)]
            bt.reset_index(inplace=True)
            #print(bt)
            if bt.empty == False:
              if bt['Payment_pending'][0] == 1 or bt['Payment_pending'][0] == 2: 
                print("Payment is already done for the booking id or booking id cancelled before.")
              else:
                BookingTable.loc[ ( BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==self.user_id ) , 'Payment_pending'] = 1
                BookingTable.to_csv(path + 'BookingTable.csv' ,  index=False)
                load_obj = Load_data()
                userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                bt = BookingTable.loc[BookingTable['booking_id']==booking_id]
                bt = bt.reset_index()
                if bt['Payment_pending'][0] :
                  print("Payment was successful, your booking has been confirmed.")
                  break
                else:
                  print("Payment was unsuccessful, please enter correct booking id.")
                  break
            else:
              print("Please enter correct booking id")



class Cancellation:
    def __init__(self,user_id):
        self.booking_values = 0
        self.user_id = user_id
        self.payment_pending_status = -1
        self.cancellation_amount = 0
        
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
        
        
    def show_current_bookings(self,user_id):
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
        self.flag = True
        
        temp = BookingTable.loc[BookingTable['user_id']==user_id]
        cur_date = datetime.now()
        temp = temp[temp['start'] > str(cur_date)]
        if temp.empty:
            print('No future Bookings for cancellation')
            self.flag = False 
        else:
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            print(temp)
            self.flag = True 

        self.booking_values = temp['booking_id'].values
        
            
    def cancellation_confirmation(self,input,cancellation_amount):
        if input == 1:
            print("Cancellation was successful, your amount ",cancellation_amount,"  will be refunded soon in your wallet.")
        else:
            print("Cancellation was unsuccessful. please try again later.")
      
    def cancellation(self):
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
        
        while(1):
            booking_id = int(input("Enter booking id to proceed with cancellation :"))
            print("Enter -1 to exit out of cancellation")
            if booking_id == -1:
                break
            #for checking payment pending
            print(self.booking_values)
            if booking_id not in self.booking_values:
                print("Please enter correct booking id")
            else:
                bt = BookingTable.loc[ (BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==self.user_id)]
                bt.reset_index(inplace=True)
                print(bt)
                if bt.empty == False:
                    if bt['Payment_pending'][0] == 0 or bt['Payment_pending'][0] == 2:
                        print("Unconfirmed bookings cannot be cancelled, cancellation not possible! ")
                    else:
                        BookingTable.loc[ ( BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==self.user_id ) , 'Payment_pending'] = 2
                        BookingTable.to_csv(path + 'BookingTable.csv' ,  index=False)
                        load_obj = Load_data()
                        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                        bt = BookingTable.loc[BookingTable['booking_id']==booking_id]
                        bt = bt.reset_index()

                        #delting data from DatesMapping
                        load_obj = Load_data()
                        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
#                        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
                        indexNames = DatesMapping[ DatesMapping['booking_id'] == booking_id ].index
                        DatesMapping.drop(indexNames , inplace=True)
                        DatesMapping.to_csv(path + 'DatesMapping.csv' ,  index=False)

                        self.cancellation_amount = bt['amount'][0]
                        if bt['Payment_pending'][0] == 2 :
                            self.payment_pending_status = 1
                            self.cancellation_confirmation(1,self.cancellation_amount)
                            break
                        else:
                            self.payment_pending_status = 0
                            self.cancellation_confirmation(0,self.cancellation_amount)
                            break


                else:
                    print("Please enter correct booking id")

class Refund:
    def __init__(self):
        load_obj = Load_data()
        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
    
    def refund_amount(self,input,refund_amount):
        if input == 1:
            print("your amount ",refund_amount,"refunded in your wallet.")
        else:
            print("Refund was unsuccessful. please try again later.")

    
    
class LogOut:
    def logout(self,user_id):
        return None
        
        
#####################################
##RR##
#####################################









# MAIN FUNCTION 
def main():
    print("Welcome to Hotel Management")
    # loading data 
    load_obj = Load_data()
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
    uid = None 

    while(1):
        print("CHOOSE ONE OPTION")
        print("0. Login ")
        print("1. Booking ")
        print("2. Payment ")
        print("3. Cancellation ")
        print("4. Logout ")
        print("5. Exit ")
        c = input("Enter choice ")
        if (c == "0"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
            if(not uid):
                while(1):
                    print("Select login or sign up : ")
                    print("1. Login")
                    print("2. Sign Up")
                    choice = input("Enter your choice : ")
                    if choice == "1":
                        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                        login_obj = Login(userTable)
                        uid = login_obj.apply_login()
                        if uid:
                            # object created for the guest in the hotel management 
                            guest = User(uid)
                            break
                        else:
                            print("Login again")
                    elif choice == '2':
                        userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                        sign_obj = Sign_up(userTable)
                        sign_obj.apply_sign_up(userTable)
                        continue
                    else:
                        print("select a valid choice")
                        continue 
        if (c == "1"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
            if uid:
                # Implemeting sarch hotel functionality 
                print("WELCOME TO SEARCH HOTELS")
                search_obj = get_search_values()
                searchValues = search_obj.apply_searchValues()

                filter_obj = Filters()
                dictFilter = filter_obj.apply_filters(searchValues)

                userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                display_obj = Display_hotels(searchValues , dictFilter)
                display_obj.apply_display_hotels(hotelTable)

                userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                select_hotel_obj = Select_hotel()
                hotel_id = select_hotel_obj.apply_select_hotel(hotelTable)

                # object made for selected hotel 
                userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                df = hotelTable[hotelTable["hotel_id"] == hotel_id]
                print(df)
                hotel_obj = Hotel(df["hotel_id"],df["hotel_name"],df["location"],df["Area"],df["Category(stars)"],df["Covid Hygiene Rating"],df["Covid-19 zones"],df["Maximum Offer"],df["price_range_start"],df["price_range_end"])

                #   selecting hotel room 
                userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
                calculate_avail_obj = Calculate_availability(hotel_id, searchValues)
                SR,DR,DUR = calculate_avail_obj.apply_calcualte_availability(SingleRoom, DoubleRoom, DuplexRoom,DatesMapping)

                # displaying availability 
                display_calc_avail_obj = Display_calculate_availability(hotel_id, SR,DR,DUR)
                avail = display_calc_avail_obj.apply_display(SingleRoom, DoubleRoom, DuplexRoom)

                # select desired room 
                select_room_obj = Select_room(avail)
                roomType , no_of_rooms = select_room_obj.apply_select_room()

                # object created for the room selected 
                if int(roomType) == 1:
                    temp_df = SingleRoom[SingleRoom["hotel_id"] == hotel_id]
                    room_selected_obj = Single_Room(hotel_id,no_of_rooms,temp_df["Offers"],temp_df["Price"],roomType)

                elif int(roomType) == 2:
                    temp_df = DoubleRoom[DoubleRoom["hotel_id"] == hotel_id]
                    room_selected_obj = Double_Room(hotel_id,no_of_rooms,temp_df["Offers"],temp_df["Price"],roomType)

                elif int(roomType) == 3:
                    temp_df = DuplexRoom[DuplexRoom["hotel_id"] == hotel_id]
                    room_selected_obj = Duplex_Room(hotel_id,no_of_rooms,temp_df["Offers"],temp_df["Price"],roomType)

        
#                roomType , no_of_rooms = select_hotel_room(SingleRoom, DoubleRoom, DuplexRoom,DatesMapping, hotel_id, searchValues)

                # if roomType and no of rooms not none continue booking
                
                if (roomType):
                    # call booking
                    Booking_obj = Booking()
                    Booking_obj.booking_function(BookingTable, int(uid),int(hotel_id),searchValues['location'],int(no_of_rooms),int(roomType),searchValues['startDate'],searchValues['endDate'])
                    
                    Booking_receipt_obj = Booking_receipt()
                    Booking_receipt_obj.displaying_final_bill(Booking_obj)
                    
                else:
                    print("operation not possible")
        
        elif (c == "2"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
            #userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            if uid:
                Payment_obj = Payment(uid)
                Payment_obj.display_pending_payment(uid)

                if(Payment_obj.flag == True):
                    PaymentMethods_obj = PaymentMethods()
                    PaymentMethods_obj.choose_payment_method()
                
                if(Payment_obj.flag == True):
                    Payment_obj.make_payment()
                
            else:
                print("operation not possible login")

        elif (c == "3"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
            if uid:
                CancelBooking_obj = Cancellation(uid)
                CancelBooking_obj.show_current_bookings(uid)
                if CancelBooking_obj.flag == True:

                    CancelBooking_obj.cancellation()
                    # CancelBooking_obj.flag ---> use of flag put here 
                    
                    RefundBooking_obj = Refund()
                    CancelBooking_obj.payment_pending_status
                    if CancelBooking_obj.payment_pending_status == 1 :
                        RefundBooking_obj.refund_amount(1,CancelBooking_obj.cancellation_amount)
                    else:
                        RefundBooking_obj.refund_amount(0,CancelBooking_obj.cancellation_amount)
            else:
                print("operation not possible login")

        elif (c == "4"):
            load_obj = Load_data()
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load_obj.load()
            if(uid):
                logout = LogOut()
                logout.logout(uid)
                print(" user logged out")
        elif ( c == "5"):
            break




if __name__ == "__main__":
    main()

