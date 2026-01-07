START
	LOAD facilities users bookings from files
	DISPLAY 'Welcome to <...>!'
	DISPLAY 'Enter Student ID or Teacher ID'
	INPUT ID
	DISPLAY 'Enter your password'
	INPUT PASSWORD
	IF ID IS WRONG OR INVALID THEN
		DISPLAY 'Access denied'
		EXIT
	ELSE
		DISPLAY 'Log in successful'
		LOOP
			DISPLAY list of sport facilities with status
				(Available / Not Available / Booked)
			INPUT = facility_choice
			IF facility_choice = not available
				DISPLAY *error message*
			ELSE IF facility_choice = available THEN 
				DISPLAY 'Do you want to book this facility (y/n)'
			ELSE IF choice = “Y” THEN
				DISPLAY 'Enter number of people:'
				INPUT number_of_people
				DISPLAY 'Enter Duration in days'
					INPUT duration
				DISPLAY 'Enter the date:'
				INPUT date
				DISPLAY 'Enter your name'
				INPUT name
				Save booking details, UPDATE facility status = booked
				DISPLAY 'You have successfully booked this facility'
			ELSE IF facility_status = not available THEN
				DISPLAY 'This facility has been booked'
			ELSE IF facility_status = Booked THEN
				DISPLAY 'booking details'
				DISPLAY 'Do you want to cancel (Y/N)'
			IF choice = “Y” THEN
				Cancel booking
				UPDATE facility status to available
				DISPLAY 'Your booking has been successfully canceled'
			END
		UNTIL user decides to exit
	END
END


