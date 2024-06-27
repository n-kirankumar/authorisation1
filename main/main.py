from crud import create_record, read_records, update_record, delete_record
from users import authenticate, is_admin, is_authenticated
from log import logger

def main():
    """
    Main function to demonstrate CRUD operations based on authentication and authorization.
    """
    # Example 1: Authenticate as admin
    if authenticate('admin', 'admin123'):
        logger.info("Admin logged in successfully")
    else:
        logger.error("Admin login failed")

    # Example 2: Create a new record as admin
    if is_authenticated() and is_admin():
        valid_record = {
            'mobile': 919876543214,
            'email': 'e@gmail.com',
            'gender': 'Male',
            'blood_group': 'B+',
            'dob': '1992-02-02'
        }
        if create_record(valid_record):
            logger.info("Record created successfully")
        else:
            logger.error("Failed to create record")
    else:
        logger.error("Authentication or authorization failed")

    # Example 3: Read all records
    records = read_records()
    logger.info(f"All records: {records}")

    # Example 4: Update the valid record with an invalid email as admin
    if is_authenticated() and is_admin():
        if update_record(919876543214, {'email': 'invalid_email'}):
            logger.info("Record updated successfully")
        else:
            logger.error("Failed to update record")
    else:
        logger.error("Authentication or authorization failed")

    # Example 5: Delete the valid record as admin
    if is_authenticated() and is_admin():
        if delete_record(919876543214):
            logger.info("Record deleted successfully")
        else:
            logger.error("Failed to delete record")
    else:
        logger.error("Authentication or authorization failed")

    # Example 6: Attempt to perform actions as a normal user (should fail)
    if authenticate('user1', 'user123'):
        if create_record(valid_record):
            logger.info("Record created successfully as normal user")
        else:
            logger.error("Failed to create record as normal user")
    else:
        logger.error("Login failed for user1")

if __name__ == "__main__":
    main()
