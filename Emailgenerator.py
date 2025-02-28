import re
import datetime

def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}$"
    return re.match(email_regex, email) is not None

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def generate_personalized_email(user):
    occasion = user["occasion"].lower()
    email_template = ""
    
    if occasion == "birthday":
        email_template = f"""
        Dear {user['name']},

        Wishing you a very Happy Birthday! May this special day bring you lots of happiness, love, and wonderful memories.

        Best wishes,
        Your Friend
        """
    elif occasion == "leave":
        email_template = f"""
        Dear {user['name']},

        I hope you are doing well. I wanted to inform you that I will be on leave from {user['start_date']} to {user['end_date']}. Please let me know if you need any urgent assistance before my leave.

        Best regards,
        [Your Name]
        """
    elif occasion == "alert":
        email_template = f"""
        Dear {user['name']},

        This is an important alert: [Alert Message]. Please make sure to take the necessary actions immediately.

        Kind regards,
        Your Team
        """
    elif occasion == "festival":
        email_template = f"""
        Dear {user['name']},

        Wishing you a joyful and prosperous {user['festival_name']}. May the festival bring happiness, peace, and good health to you and your loved ones.

        Warm regards,
        [Your Name]
        """
    elif occasion == "holiday":
        email_template = f"""
        Dear {user['name']},

        Happy Holidays! I hope you are enjoying a well-deserved break from {user['holiday_start_date']} to {user['holiday_end_date']}. Wishing you a peaceful and relaxing holiday season.

        Best wishes,
        Your Team
        """
    elif occasion == "announcement":
        email_template = f"""
        Dear {user['name']},

        We are excited to announce the following:
        {user['announcement_details']}
        
        For more information, please contact ph no.- 9087654321

        Best regards,
        Your Team
        """
    else:
        email_template = "Sorry, we don't have a template for this occasion. Please try again later."
    
    return email_template

def main():
    name = input("Enter recipient's name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    
    occasion = input("Enter the occasion (Birthday, Leave, Alert, Festival, Holiday, Announcement): ").strip().lower()
    if not occasion:
        print("Occasion cannot be empty.")
        return
    
    email = input("Enter recipient's email: ").strip()
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    
    user = {"name": name, "occasion": occasion, "email": email}
    
    if occasion == "leave":
        user["start_date"] = input("Enter start date of your leave (MM/DD/YYYY): ").strip()
        user["end_date"] = input("Enter end date of your leave (MM/DD/YYYY): ").strip()
        if not is_valid_date(user["start_date"]) or not is_valid_date(user["end_date"]):
            print("Invalid date format. Use MM/DD/YYYY.")
            return
    
    elif occasion == "festival":
        user["festival_name"] = input("Enter the festival name: ").strip()
        if not user["festival_name"]:
            print("Festival name cannot be empty.")
            return
    
    elif occasion == "holiday":
        user["holiday_start_date"] = input("Enter holiday start date (MM/DD/YYYY): ").strip()
        user["holiday_end_date"] = input("Enter holiday end date (MM/DD/YYYY): ").strip()
        if not is_valid_date(user["holiday_start_date"]) or not is_valid_date(user["holiday_end_date"]):
            print("Invalid date format. Use MM/DD/YYYY.")
            return
    
    elif occasion == "announcement":
        user["announcement_details"] = input("Enter announcement details: ").strip()
        if not user["announcement_details"]:
            print("Announcement details cannot be empty.")
            return
    
    email_content = generate_personalized_email(user)
    print("\nGenerated Email:\n")
    print(email_content)

if __name__ == "__main__":
    main()
