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
def load():
    
    userTable = pd.read_csv(path + 'userTable.csv')
    hotelTable= pd.read_csv(path+ 'hotelTable.csv' )
    SingleRoom= pd.read_csv(path + 'SingleRoom.csv')
    DoubleRoom = pd.read_csv(path + 'DoubleRoom.csv')
    DuplexRoom = pd.read_csv(path + 'DuplexRoom.csv')
    BookingTable = pd.read_csv(path + 'BookingTable.csv')
    DatesMapping = pd.read_csv(path + 'DatesMapping.csv')
    return userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping


# Login Function 
def login_signup(userTable):
    
    def find_first_index_in_1d(arr, val):
        return np.where(arr == val)[0][0]

    def find_present_or_not_1d(arr,val):
        boolVal = np.shape(np.where(arr == val)[0])[0]
        if boolVal: 
            return True
        else:
            return False

    def login(userTable):
        print("Hello user!")
        
        def enter_credentials():
            print("Enter details to login")
            # type and digits check , check not empty 
            id = input("Enter your user id : ")
            password = input("Enter your 4 digit password : ")
            return id, password 

        def check_Validity(id, password):
            if id and password:
                # checking if user is valid or not
                id = int(id)
                password = int(password)
                user_id_all = userTable['user_id'].values
                pass_all = userTable['password'].values
                # user and password present in table or not 
                if find_present_or_not_1d(user_id_all, id) and find_present_or_not_1d(pass_all , password):
                # if user id matches to that password
                    if  (find_first_index_in_1d(user_id_all, id) == find_first_index_in_1d(pass_all , password)):
                        print("Login Successful")
                        return id 
                    else:
                        print('Invalid Details')
                        return 
            else:
                print('Invalid Details')
                return 
                
        id , password = enter_credentials()
        user_id = check_Validity(id,password)
        return user_id 
            
        """returns user if user gets successfully logged in else none""" 

    def signup(userTable):
        print("Hello from signup")

        user_id_all = userTable['user_id'].values
        # fetching all email id and all passwords 
        email_all = userTable['email'].values
        pass_all = userTable['password'].values 

        def enter_details():
            new_id = user_id_all[-1] + 1 
            # check email , password number 
            name = input("Enter your Name : ")
            birth = input("Enter your DOB:'DD/MM/YYYY ")
            city = input("Enter your city : ")

            # checking if email already registered 
            email = input("Enter your email id : ")
            if find_present_or_not_1d(email_all, email):
                print('Email id already regestered please login')
                return

            # if password already matches some password 
            while(1):
                password = input("Enter your password (4 digit numbers) : ")
                password = int(password)
                if find_present_or_not_1d(pass_all , password):
                    print('Enter another password , this is already used')
                    continue 
                else:
                    break 
            newUser = {'user_id': new_id, 'name': name ,'email': email , 'password': password , 'city':city , 'DOB':birth }
            return newUser 


        def confirm_details_create_id(userTable,newUser):

            print("\n\n Following are the details ")
            print("Select one choice")
            print("1. Confirm and Create")
            print("2. Exit ")

            print("\n")
            for key in newUser.keys():
                if key is not 'user_id':
                    print(key + " : " + str(newUser[key]))

            choice = input("Enter your choice : ")
            if (choice == "1"):
                print("Your new id is :" + str(newUser['user_id']))
                userTable = userTable.append(newUser , ignore_index=True)
                userTable.to_csv(path + 'userTable.csv' ,  index=False)
                print(" Signup success")
                print(" Login again to continue !")
                return True
                
            else:
                print("User not signed up")
                return False
            
        # Functions called here
        newUser = enter_details()
        if newUser : 
            confirm_details_create_id(userTable, newUser)

    uid = None 
    while(1):
        print("Select login or sign up : ")
        print("1. Login")
        print("2. Sign Up")
        choice = input("Enter your choice : ")
        if choice == "1":
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            uid = login(userTable)
            if uid:
                break
            else:
                print("Login again")
        elif choice == '2':
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            signup(userTable)
            continue
        else:
            print("select a valid choice")
            continue 
    return uid


# Search Hotel Function 
def search_hotels(hotelTable):
    print("WELCOME TO SEARCH HOTELS")
    # Inner functions here 
    def select_date():
        def check_Date_Format(DMY):
            try:
                bookDate = datetime(DMY[2],DMY[1], DMY[0])
                correctDate = True
            except ValueError:
                correctDate = False
            return correctDate,bookDate

        def check_Date_x_after_y(x,y,equalCase = False):
            if not equalCase:
                if x > y:
                    return True 
                else:
                    return False
            else:
                if x >= y:
                    return True 
                else:
                    return False

        while(1):
            startValue = input('\nEnter Start Date in the format DD/MM/YYYY : ')
            DMY = [int(i) for i in startValue.split('/')]
            correctDate,startDate = check_Date_Format(DMY)


            # check if date is not a past date 
            curr_date = datetime.now()
            if correctDate:
                if check_Date_x_after_y(startDate , curr_date):
                    break 
                else:
                    print("\nEnter a date in future ") 
            else:
                print("\nDate not correct ")

        while(1):
            endValue = input('\nEnter End Date in the format DD/MM/YYYY : ')
            DMY = [int(i) for i in list(endValue.split('/'))]

            correctDate,endDate = check_Date_Format(DMY)

            # check if date is not a past date 
            curr_date = datetime.now()
            if correctDate:
                if check_Date_x_after_y(endDate , curr_date) and check_Date_x_after_y(endDate, startDate,True):
                    break 
                else:
                    print("\nEnter a date in future ") 
            else:
                print("\nDate not correct ")
        
        searchValues = {'startDate' : startDate , 'endDate': endDate}
        return searchValues

    def dacation_nightout(searchValues):
        print("\nSelect Dacation or Nighout or Both")
        print("Choices are : ")
        print("1. Dacation ")
        print("2. Nightout ")
        print("3. Both ")

        if (searchValues['endDate'].date() == searchValues['startDate'].date()):
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

        searchValues["startTime"] = start_Val
        searchValues["endTime"] = end_Val
        searchValues["startDate"] = searchValues["startDate"].replace(hour=start_Val, minute=0, second=0)
        searchValues["endDate"] = searchValues["endDate"].replace(hour=end_Val, minute=0, second=0)
        return searchValues

    def select_location(searchValues):
        # select the appropriate location 

        print("Select Location for Booking : ")
        print("1. Jaipur ")
        print("2. Delhi ")

        while(1):
            choice = input(" select one among above : ")
            if (choice == "1"):
                searchValues["location"] = "Jaipur"
                break
            elif (choice == "2"):
                searchValues["location"] = "Delhi"
                break
            else:
                print("Not valid ,Choose again! ")
                continue 
        return searchValues

    def choose_filter(searchValues):
        def display_filters(searchValues):
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
            return filterVal,searchValues 

        def select_filters(filterVal, searchValues):
            print("Enter the filters you want by index and comma separated :-")
            filterIndex = input("Enter comma separated index values : ")
            filters_all = [ filterVal['filters'][int(i)-1] for i in filterIndex.split(',')]

            dictFilter = {}
            # Enter filters values among filters choosen 
            for idx in filterIndex.split(','):
                idx = int(idx) - 1
                filterName = filterVal['filters'][idx]
                options = [op for op in filterVal['values'][idx].split(',')]


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

            return dictFilter, filterVal , searchValues


        filterVal,searchValues = display_filters(searchValues)
        dictFilter, filterVal , searchValues = select_filters(filterVal, searchValues)
        return dictFilter

    def display_hotels(hotelTable , searchValues , dictFilter):

        # function to sort the hotels and display 
        def sort_hotels(hotelNames):
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

        # searching by filters 
        # location search 
        hotelNames = hotelTable[hotelTable['location'] == searchValues['location']]
        # search by filters selected before 
        for key in dictFilter.keys():
            if key !='Maximum Offer' and key !='Price-Range':
                hotelNames = hotelNames[hotelNames[key] == dictFilter[key]]
            
            elif key == 'Maximum Offer':
                hotelNames = hotelNames[(hotelNames[key] >= dictFilter[key][0]) & (hotelNames[key] <= dictFilter[key][1])]
            
            elif key == 'Price-Range':
                hotelNames = hotelNames[(hotelNames['price_range_start'] >= dictFilter[key][0]) & (hotelNames['price_range_end'] <= dictFilter[key][1])]
            pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(hotelNames)
        sort_hotels(hotelNames)
        return hotelNames 

    def select_hotel(hotelTable):
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
    
    # Select appropricate date start and end , if same enter two times 
    searchValues = select_date()
    
    # select dacation or nightout 
    searchValues = dacation_nightout(searchValues)
    

    # select location 
    searchValues = select_location(searchValues)
    

    # Apply filters 
    dictFilter = choose_filter(searchValues)
    
    # load all tables
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    hotelNames = display_hotels(hotelTable , searchValues , dictFilter)
    
    
    # select hotel among displayed hotels 
    #load all tables 
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    hotel_id = select_hotel(hotelTable)
    return hotel_id, searchValues
  
    
def select_hotel_room(SingleRoom, DoubleRoom, DuplexRoom,DatesMapping, hotel_id, searchValues):

  def calculate(SingleRoom , DoubleRoom, DuplexRoom):

    def check_avail_one(data,searchValues):
        for key in data.keys():
            if searchValues['startTime'] == 9:
                return data[key][0]
            elif searchValues['startTime'] == 21:
                return data[key][1]
            elif searchValues['startTime'] == 23:
                return min(data[key][0],data[key][0])
            # If date is only one date 
        


    def check_avail_range(data,searchValues):
      # If dates are a range 
      temp = []
      for key in data.keys():
        if key == searchValues['startDate'].date():
          if searchValues['startTime'] == 9 or searchValues['startTime'] == 23:
            temp.append(data[key][0])
            temp.append(data[key][1])
          elif searchValues['startTime'] == 21:
            temp.append(data[key][1])
        elif key == searchValues['endDate'].date():
          if searchValues['startTime'] == 21 or searchValues['startTime'] == 23:
            temp.append(data[key][0])
            temp.append(data[key][1])
          elif searchValues['startTime'] == 9:
            temp.append(data[key][0])
        else:
          temp.append(data[key][0])
          temp.append(data[key][1])
          
      return min(temp)

    def change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType):
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

    def change_0(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType):
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

    def change_1(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType):
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


    def find_room_number(df, id):
      df = df[df["hotel_id"] == id]
      room = df["Number of Room"]
      return int(room)

    # Total rooms of each type in respective hotel 
    roomNo = [0,0,0]
    roomNo[0] = find_room_number(SingleRoom , hotel_id)
    roomNo[1] = find_room_number(DoubleRoom , hotel_id)
    roomNo[2] = find_room_number(DuplexRoom , hotel_id)

    # ALL DATES 
    # if start and end date are same only one date 
    # else both are diff so range of dates 

    sameDay = searchValues["startDate"].date() == searchValues["endDate"].date()
    # Storing all dates in range of start and end for a booking 
    if sameDay: 
      date = [searchValues["startDate"].date()]
    else:
      flag = True
      d = searchValues["startDate"].date()
      date = []
      while(flag):
        date.append(d)
        d += timedelta(days=1)
        if d ==  searchValues["endDate"].date()+timedelta(days=1):
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
    bookingDetail = DatesMapping[DatesMapping["hotel_id"] == hotel_id]
    bookingDetail = bookingDetail[bookingDetail["end_Date"] >= str(searchValues["startDate"].replace(hour=0))]


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
              singleDict ,doubleDict , duplexDict= change_1(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
            elif start_time == 9:
              singleDict ,doubleDict , duplexDict= change_0(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
            elif  start_time == 23:
              singleDict ,doubleDict , duplexDict= change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)

        else:
          
          if (date[d] == start.date()):
            # if for start date only night booked 
            if start_time == 21:
              singleDict ,doubleDict , duplexDict= change_1(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
            elif start_time == 9 or start_time == 23:
              singleDict ,doubleDict , duplexDict= change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)

          elif (date[d] == end.date()):
            if end_time == 9:
              singleDict ,doubleDict , duplexDict= change_0(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
            elif end_time == 21 or end_time == 23:
              singleDict ,doubleDict , duplexDict= change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)
          
          elif (start.date() < date[d] < end.date()):
            
            singleDict ,doubleDict , duplexDict= change(rooms,singleDict ,doubleDict , duplexDict,date,d,roomType)

      #   # if current date is in middle of any date ranges of course one day and one night deleted from total available 
        #   # Process repeated for all room types

    # Calculation of number of rooms available finally 
    if sameDay:
      SR = check_avail_one(singleDict,searchValues)
      DR = check_avail_one(doubleDict,searchValues)
      DUR = check_avail_one(duplexDict,searchValues)
    else:
      SR = check_avail_range(singleDict,searchValues)
      DR = check_avail_range(doubleDict,searchValues)
      DUR = check_avail_range(duplexDict,searchValues)

    if SR < 0:
      SR = 0
    if DR < 0:
      DR = 0
    if DUR < 0:
      DUR = 0

    
    return SR,DR,DUR


  def display(SingleRoom, DoubleRoom, DuplexRoom, hotel_id, SR,DR,DUR):

    SRO = SingleRoom[SingleRoom['hotel_id'] == hotel_id].iloc[0]['Offers']
    SRP = SingleRoom[SingleRoom['hotel_id'] == hotel_id].iloc[0]['Price']

    DRO = DoubleRoom[DoubleRoom['hotel_id'] == hotel_id].iloc[0]['Offers']
    DRP = DoubleRoom[DoubleRoom['hotel_id'] == hotel_id].iloc[0]['Price']

    DURO = DuplexRoom[DuplexRoom['hotel_id'] == hotel_id].iloc[0]['Offers']
    DURP = DuplexRoom[DuplexRoom['hotel_id'] == hotel_id].iloc[0]['Price']

    avail = [SR,DR,DUR]
    offer = [SRO,DRO,DURO]
    price = [SRP, DRP, DURP]

    DisplayDict = {"Availability" : avail , "Offer": offer , "Price": price}
    df = pd.DataFrame(DisplayDict, index=['Single Room', 'Double Room', 'Duplex Room'])
    print(df)
    return avail 


  def select_room(avail):
      while(1):
        print("select one among following option ")
        print("1. Single Room")
        print("2. Double Room")
        print("3. Duplex Room")
        print("4. Exit")
        
        choice = input()

        if (choice == "1"):
          # check availability of room
          if avail[int(choice)-1] == 0:
            print("Availability is zero choose any other ")
            continue 
          # Input nuber of rooms of that type 
          while(1):
            no_of_rooms = input("Enter no of rooms you want according to availability ")
            if (int(no_of_rooms) <= avail[int(choice)-1]):
              break 
          roomType = 1
          break 

        elif (choice == "2"):
          if avail[int(choice)-1] == 0:
            print("Availability is zero choose any other ")
            continue 
          # Input nuber of rooms of that type  
          while(1):
            no_of_rooms = input("Enter no of rooms you want according to availability ")
            
            if int(no_of_rooms) <= avail[int(choice)-1]:
              
              break  
          roomType = 2
          break 

        elif (choice == "3"):
          if avail[int(choice)-1] == 0:
            print("Availability is zero choose any other ")
            continue 
          # Input nuber of rooms of that type 
          while(1):
            no_of_rooms = input("Enter no of rooms you want according to availability ")
            if (int(no_of_rooms) <= avail[int(choice)-1]):
              break 
          roomType = 3
          break 
        elif (choice == "4"):
          roomType = None
          no_of_rooms = None 
          break 

      return roomType , no_of_rooms

  #
  #
  # Load Tables 
  SR , DR, DUR = calculate(SingleRoom , DoubleRoom, DuplexRoom)
  avail = display(SingleRoom, DoubleRoom, DuplexRoom, hotel_id, SR,DR,DUR)
  roomType, no_of_rooms = select_room(avail)

  return roomType, no_of_rooms
    
# Booking function 
def booking_function(BookingTable,user_id,hotel_id,location,no_of_rooms,type_of_room,start_date,end_date):
  userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
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


  review = ""
  payment_pending = 0

  laundry = 0
  laundry_cost = 0

  additional_sanitizers = 0
  additional_sanitizers_cost = 0

  masks = 0
  masks_cost = 0

  face_shields = 0
  face_shields_cost = 0

  num_of_room_available = 0

  def choose_additional_facilities():
    laundry = 0
    additional_sanitizers = 0
    masks = 0
    face_shields = 0
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
        laundry = 1
      elif choice == 2:
        additional_sanitizers = int(input("Enter the number of additional sanitizers"))
      elif choice == 3:
        masks = int(input("Enter the number of additional masks"))
      elif choice == 4:
        face_shields = int(input("Enter the number of additional face_shields"))
      elif choice == 5:
        print("No additional servies added")
        break
      elif choice == 6:
        break
      else:
        print("Please enter correct choice")

    return (laundry,additional_sanitizers,masks,face_shields)

  (laundry,additional_sanitizers,masks,face_shields) = choose_additional_facilities()
  
  #below few lines will calculate amount to be paid by user

  cost_of_room = 0 #to be calculated during amount calculation
  one_room_price = 0
  offer = 0
  #below comment just for reference delete it
  #booking_id	user_id	hotel_id	Location	Area	No of rooms  Type of Room  start	end	amount	review	Payment_pending	laudary	additional sanitizers	masks	face shield
  
  #fetch details of hotel from hotel id
  hotel_details_from_hotel_id = hotelTable.loc[hotelTable['hotel_id']==hotel_id]

  #fetch details of singleRoom, DoubleRoom, DuplexRoom from hotel id
  if type_of_room == 'SingleRoom':
    single_room_details_from_hotel_id = SingleRoom.loc[SingleRoom['hotel_id']==hotel_id]
    single_room_details_from_hotel_id = single_room_details_from_hotel_id.reset_index()
    one_room_price = single_room_details_from_hotel_id['Price'][0]
    offer = single_room_details_from_hotel_id['Offers'][0]
    num_of_room_available = single_room_details_from_hotel_id['Number of Room'][0]
    print(single_room_details_from_hotel_id) 
  elif type_of_room == 'DoubleRoom':
    double_room_details_from_hotel_id = DoubleRoom.loc[DoubleRoom['hotel_id']==hotel_id]
    double_room_details_from_hotel_id = double_room_details_from_hotel_id.reset_index()
    one_room_price = double_room_details_from_hotel_id['Price'][0]
    offer = double_room_details_from_hotel_id['Offers'][0]
    num_of_room_available = double_room_details_from_hotel_id['Number of Room'][0]
  elif type_of_room == 'DuplexRoom':
    duplex_room_details_from_hotel_id = DuplexRoom.loc[DuplexRoom['hotel_id']==hotel_id]
    duplex_room_details_from_hotel_id = duplex_room_details_from_hotel_id.reset_index()
    one_room_price = duplex_room_details_from_hotel_id['Price'][0]
    offer = duplex_room_details_from_hotel_id['Offers'][0]
    num_of_room_available = duplex_room_details_from_hotel_id['Number of Room'][0]

  #calculating addtional requirement price
  hotel_details_from_hotel_id = hotelTable.loc[hotelTable['hotel_id']==hotel_id]
  hotel_details_from_hotel_id = hotel_details_from_hotel_id.reset_index()

  laundry_cost = laundry * hotel_details_from_hotel_id['laundry'][0]
  additional_sanitizers_cost = additional_sanitizers * hotel_details_from_hotel_id['additional sanitizers'][0]
  masks_cost = masks * hotel_details_from_hotel_id['masks'][0]
  face_shields_cost = face_shields * hotel_details_from_hotel_id['face shield'][0]

  #applying offer on one room price
  one_room_price = one_room_price - (one_room_price*offer)/100
  one_room_price = int(one_room_price)

  #calculating cost of room
  cost_of_room = (no_of_rooms * one_room_price ) 

  #calculating final amount to be paid by user after discount
  amount =  cost_of_room + laundry_cost + additional_sanitizers_cost + masks_cost + face_shields_cost
  if type_of_room == 'SingleRoom':
    type_of_room = int(1)
  elif type_of_room == 'DoubleRoom':
    type_of_room = int(2)
  elif type_of_room == 'DuplexRoom':
    type_of_room = int(3)

  #creating a temp Series to be put into DataFrame
  temp = {'booking_id':booking_id, 'user_id':user_id, 'hotel_id':hotel_id, 'Location':location, 'No of rooms':no_of_rooms, 'Type of Room':type_of_room, 'start':start_date, 'end':end_date, 'amount':amount,  'review':review ,'Payment_pending':payment_pending ,'laundry':laundry ,'additional sanitizers':additional_sanitizers ,'masks':masks ,'face shield':face_shields  }
  BookingTable = BookingTable.append(temp,ignore_index=True)
  BookingTable.to_csv(path + 'BookingTable.csv' ,  index=False)

  # write table to database 

  temp2 = {'start_Date':start_date, 'end_Date':end_date, 'booking_id':booking_id, 'hotel_id':hotel_id, 'user_id':user_id, 'roomType':type_of_room, 'No of rooms': no_of_rooms  }
  DatesMapping = DatesMapping.append(temp2,ignore_index=True)
  DatesMapping.to_csv(path + 'DatesMapping.csv' ,  index=False)

  def displaying_final_bill(amount,laundry_cost,additional_sanitizers_cost,masks_cost,face_shields_cost,no_of_rooms,one_room_price,cost_of_room):
    print("-------Your final bill---------")
    print("laundry_cost : ",laundry_cost)
    print("additional_sanitizers_cost : ",additional_sanitizers_cost)
    print("masks_cost : ",masks_cost)
    print("face_shields_cost : ",face_shields_cost)
    print("no_of_rooms : ",no_of_rooms)
    print("one_room_price : ",one_room_price)
    print("cost_of_room : ",cost_of_room)
    print("Total Amount : ",amount)

  def booking_confirmation():
    print("Your booking has been confirmed please proceed to payment.")
  
  displaying_final_bill(amount,laundry_cost,additional_sanitizers_cost,masks_cost,face_shields_cost,no_of_rooms,one_room_price,cost_of_room)
  booking_confirmation()


# Payment function 
def payment(BookingTable, user_id):
  userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
  flag = True 
  #below line for my future reference
  def display_pending_payment(user_id):
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    temp = BookingTable.loc[BookingTable['user_id']==user_id]
    cur_date = datetime.now()
    temp = temp[temp['start'] > str(cur_date)]
    if temp.empty:
      print('No Pending Payment')
      flag = False
    else:
      pd.set_option("display.max_rows", None, "display.max_columns", None)
      print(temp)
      flag = True 
    
    booking_values = temp['booking_id'].values
    return booking_values,flag
  
  booking_values,flag = display_pending_payment(user_id)

  def select_booking_for_payment():
    booking_id = int(input("Enter booking id to proceed with payment :"))
    return booking_id
  

  def make_payment():
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    def choose_payment_method():
      userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
      print("Choose payment method : ")
      print("1. VISA Debit Card")
      print("2. Mastercard Debit")
      print("3. Rupay")
      print("4. Net Banking")
      print("5. Credit Card")
      choose = int(input("Enter your choice : "))
      if choose == 1:
        print("1. VISA Debit Card used")
      elif choose == 2:
        print("2. Mastercard Debit Card used")
      elif choose == 3:
        print("3. Rupay used")
      elif choose == 4:
        print("4. Net Banking used")
      elif choose == 5:
        print("5. Credit Card used")

    def proceed_with_payment():
      userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
      while(1):
        booking_id = select_booking_for_payment()
      
        print("Enter -1 to exit out of payment")
        if booking_id == -1:
          break
        #for checking payment pending
        if booking_id not in booking_values:
          print("Please enter correct booking id")
        else:
          bt = BookingTable.loc[ (BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==user_id)]
          bt.reset_index(inplace=True)
          #print(bt)
          if bt.empty == False:
            if bt['Payment_pending'][0] == 1 or bt['Payment_pending'][0] == 2: 
              print("Payment is already done for the booking id or booking id cancelled before.")
            else:
              BookingTable.loc[ ( BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==user_id ) , 'Payment_pending'] = 1
              BookingTable.to_csv(path + 'BookingTable.csv' ,  index=False)
              userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
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

    choose_payment_method()
    proceed_with_payment()
  if flag:    
    make_payment()
    
# Cancellation function 
def cancel_booking(BookingTable,user_id):
  userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
  flag = True 
  
  #to show all current bookings in cart
  def show_current_bookings(user_id):
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    temp = BookingTable.loc[BookingTable['user_id']==user_id]
    cur_date = datetime.now()
    temp = temp[temp['start'] > str(cur_date)]
    if temp.empty:
      print('No future Bookings for cancellation')
      flag = False 
    else:
      pd.set_option("display.max_rows", None, "display.max_columns", None)
      print(temp)
      flag = True 
    booking_values = temp['booking_id'].values
    return booking_values,flag

  booking_values,flag = show_current_bookings(user_id)

  def select_booking_for_cancel():
    booking_id = int(input("Enter booking id to proceed with cancellation :"))
    return booking_id

  def cancellation_confirmation(input,cancellation_amount):
    if input == 1:
      print("Cancellation was successful, your amount ",cancellation_amount,"  will be refunded soon in your wallet.")
    else:
      print("Cancellation was unsuccessful. please try again later.")
  def cancellation_and_refund():
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    while(1):
      booking_id = select_booking_for_cancel()
      print("Enter -1 to exit out of cancellation")
      if booking_id == -1:
        break
      #for checking payment pending
      print(booking_values)
      if booking_id not in booking_values:
        print("Please enter correct booking id")
      else:
        bt = BookingTable.loc[ (BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==user_id)]
        bt.reset_index(inplace=True)
        # print(bt)
        if bt.empty == False:
          if bt['Payment_pending'][0] == 0 or bt['Payment_pending'][0] == 2: 
            print("Unconfirmed bookings cannot be cancelled, cancellation not possible! ")
          else:
            BookingTable.loc[ ( BookingTable['booking_id']==booking_id) & (BookingTable['user_id']==user_id ) , 'Payment_pending'] = 2
            BookingTable.to_csv(path + 'BookingTable.csv' ,  index=False)
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            # print(BookingTable)
            bt = BookingTable.loc[BookingTable['booking_id']==booking_id]
            bt = bt.reset_index()

            #delting data from DatesMapping
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            indexNames = DatesMapping[ DatesMapping['booking_id'] == booking_id ].index
            DatesMapping.drop(indexNames , inplace=True)
            DatesMapping.to_csv(path + 'DatesMapping.csv' ,  index=False)

            cancellation_amount = bt['amount'][0]
            if bt['Payment_pending'][0] == 2 : 
              cancellation_confirmation(1,cancellation_amount)
              break
            else:
              cancellation_confirmation(0,cancellation_amount)
              break
        else:
          print("Please enter correct booking id")

  if flag:
    cancellation_and_refund()
  else:
    return   
# Logout function 
def logout(user_id):
  return None

def main():
    print("Welcome to Hotel Management")
    # loading data 
    userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    uid = None 
    while(1):
        print("CHOOSE ONE OPTION")
        print("0. Login ")
        print("1. Booking ")
        print("2. Payment")
        print("3. Cancellation")
        print("4. Logout")
        print("5. Exit")
        c = input("Enter choice ")
        if (c == "0"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            if(not uid):
                uid = login_signup(userTable)
        if (c == "1"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            if uid:
                hotel_id, searchValues= search_hotels(hotelTable)
                roomType , no_of_rooms = select_hotel_room(SingleRoom, DoubleRoom, DuplexRoom,DatesMapping, hotel_id, searchValues)

            # if roomType and no of rooms not none continue booking 
                if (roomType):
                # call booking 
                    booking_function(BookingTable, int(uid),int(hotel_id),searchValues['location'],int(no_of_rooms),int(roomType),searchValues['startDate'],searchValues['endDate'])
            else:
                print("operation not possible")
        elif (c == "2"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            if(uid):
                payment(BookingTable, uid)
            else:
                print("operation not possible login")

        elif (c == "3"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            if(uid):
                cancel_booking(BookingTable,uid)
            else:
                print("operation not possible login")

        elif (c == "4"):
            userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
            if(uid):
                 uid = logout(uid)
                 print(" user logged out")
        elif ( c == "5"):
            break 

    # 'startDate': datetime(2020, 11, 3, 21, 0),
    # 'startTime': 9}
    # roomType , no_of_rooms = select_hotel_room(SingleRoom, DoubleRoom, DuplexRoom,DatesMapping, hotel_id, searchValues)
    # userTable,hotelTable, SingleRoom, DoubleRoom,DuplexRoom,BookingTable,DatesMapping = load()
    # booking_function(BookingTable, int(uid),int(hotel_id),searchValues['location'],int(no_of_rooms),int(roomType),searchValues['startDate'],searchValues['endDate'])
    # payment(BookingTable, uid)
    # cancel_booking(BookingTable,uid)
    # flag = logout(uid)

if __name__ == "__main__":
    main()

