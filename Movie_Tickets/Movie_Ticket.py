import random
from datetime import datetime, timedelta
import pyqrcode,png
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
print("========== Welcome to MovieTicket Booking AI ==========\n")
gmail=input("Enter Email:")
name = input("Enter your name: ").title()
print(f"\nHi {name}! Book your tickets now.\n")
movies = {
    "1": ("Action", ["Leo", "Vikram", "Jailer","Spiderman"]),
    "2": ("Comedy", ["Jathi Ratnalu", "F2", "Mad"]),
    "3": ("Horror", ["Masooda", "Virupaksha", "Kanchana"]),
    "4": ("Romance", ["Hi Nanna", "Sita Ramam", "Geetha Govindam"])
}
show_times = [
    "08:00 AM",
    "10:00 AM",
    "01:00 PM",
    "04:00 PM",
    "07:30 PM",
    "10:00 PM"
]
now = datetime.now() + timedelta(hours=5, minutes=30)

print("Choose Genre:")
print("1. Action")
print("2. Comedy")
print("3. Horror")
print("4. Romance")
choice = input("\nEnter your choice (1-4): ")
if choice in movies:
    genre, movie_list = movies[choice]
    print(f"\n{genre} Movies:")
    for movie in movie_list:
        print(movie)
    selected_movie = input("\nEnter movie name: ").title()
    if selected_movie in movie_list:
        while True:
            now = datetime.now() + timedelta(hours=5, minutes=30)
            dates = []
            print("\nAvailable Dates:")
            for i in range(3):
                d = now + timedelta(days=i)
                dates.append(d.date())
                print(f"{i+1}. {d.strftime('%d-%m-%Y')}")
            print("4. Exit")
            date_choice = input("\nSelect Date (1-4): ")
            if date_choice == "4":
                print("\nThank You! Visit Again.")
                break
            if date_choice not in ["1", "2", "3"]:
                print("Invalid date selection.")
                continue
            selected_date = dates[int(date_choice) - 1]
            available_shows = []
            if selected_date == now.date():
                for show in show_times:
                    show_datetime = datetime.combine(
                        selected_date,
                        datetime.strptime(show, "%I:%M %p").time()
                    )
                    if show_datetime > now:
                        available_shows.append(show)
            else:
                available_shows = show_times.copy()
            if not available_shows:
                print("\nSorry! No shows available for this date.")
                continue
            print("\nAvailable Show Times:")
            for i, show in enumerate(available_shows, 1):
                print(f"{i}. {show}")
            show_choice = input("\nSelect Show: ")
            if not show_choice.isdigit():
                print("Invalid show selection.")
                continue
            show_choice = int(show_choice)
            if show_choice < 1 or show_choice > len(available_shows):
                print("Invalid show selection.")
                continue
            selected_show = available_shows[show_choice - 1]
            seats = [
                "A1", "A2", "A3", "A4", "A5",
                "B1", "B2", "B3", "B4", "B5",
                "C1", "C2", "C3", "C4", "C5"
            ]
            booked_seats = random.sample(seats, random.randint(3, 6))
            available_seats = [seat for seat in seats if seat not in booked_seats]
            print("\nAvailable Seats:")
            count = 0
            for seat in available_seats:
                print(f"{seat:3}", end="  ")
                count += 1
                if count % 5 == 0:
                    print()
            no_of_seats = int(input("\n\nHow many seats do you want to book? "))
            selected_seats = input(
                f"Enter {no_of_seats} seat numbers (comma separated): "
            ).upper().split(",")
            selected_seats = [seat.strip() for seat in selected_seats]
            if len(selected_seats) != no_of_seats:
                print("Please enter the correct number of seats.")
                continue
            valid = True
            for seat in selected_seats:
                if seat not in available_seats:
                    valid = False
                    break
            if not valid:
                print("One or more selected seats are unavailable.")
                continue
            ticket_id= random.randint(100000,999999)
            print("\n========== BOOKING CONFIRMED ==========")
            print(f"Customer     : {name}")
            print(f"Genre        : {genre}")
            print(f"Movie        : {selected_movie}")
            print(f"Booking Date : {selected_date.strftime('%d-%m-%Y')}")
            print(f"Show Time    : {selected_show}")
            print(f"Seats        : {', '.join(selected_seats)}")
            print(f"Ticket ID    :{ticket_id}")
            print("\nEnjoy your movie!")
            booking_details = f"""
            ========== BOOKING CONFIRMED ==========
            Customer     : {name}
            Genre        : {genre}
            Movie        : {selected_movie}
            Booking Date : {selected_date.strftime('%d-%m-%Y')}
            Show Time    : {selected_show}
            Seats        : {', '.join(selected_seats)}
            Ticket ID    : {ticket_id}
            """
            qr = pyqrcode.create(booking_details)
            tick=str(ticket_id)
            qr.png(f"Ticket_tick.png", scale=8)
            From='kasarlasaikiran002@gmail.com'
            Subject="Movie Tickets Booking Confirmed"
            app_password="sxlk uqbw yvgm zcqe"
            body=f"""
            Dear {name},

            Thank you for booking with MovieTicket Booking AI.

            Your booking has been confirmed successfully.

            ==================================================
                            BOOKING CONFIRMED
            ==================================================

            Booking ID   : MT{ticket_id}
            Customer     : {name}
            Genre        : {genre}
            Movie        : {selected_movie}
            Booking Date : {selected_date.strftime('%d-%m-%Y')}
            Show Time    : {selected_show}
            Seats         : {', '.join(selected_seats)}
            Tickets      : {len(selected_seats)}
            Ticket ID    : {ticket_id}

            Status       : Confirmed

            Please show the attached QR Code at the theatre entrance.

            Thank you for choosing MovieTicket Booking AI.

            Enjoy your movie!

            Regards,
            MovieTicket Booking AI Team
            """
            
            attach ="Ticket_tick.png"
            msg=MIMEMultipart()
            msg['From']=From
            msg["To"]=gmail
            msg["Subject"]=Subject
            msg.attach(MIMEText(body))
            part=MIMEBase('application','octet-stream')
            part.set_payload(open(attach,'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition','attachment ; filename="%s" '%(os.path.basename(attach))) 
            msg.attach(part)
            text=msg.as_string(part)
            server =smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(From,app_password)
            server.sendmail(From,gmail,text)
            print("Success")
            server.quit()
            again = input("\nBook another ticket? (y/n): ").lower()
            if again != "y":
                print("\nThank You! Visit Again.")
                break
    else:
        print("Movie not available in this genre.")
else:
    print("Invalid genre choice.")
