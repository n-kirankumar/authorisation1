from constants import data
from utils import is_valid_mobile, is_valid_email, is_valid_gender, is_valid_blood_group, is_valid_dob
from log import logger

def create_record(record):
    """
    Create a new record.

    Args:
        record (dict): Dictionary containing record data.

    Returns:
        bool: True if record is created successfully, False otherwise.
    """
    if is_valid_mobile(record['mobile']) and is_valid_email(record['email']) and is_valid_gender(
            record['gender']) and is_valid_blood_group(record['blood_group']) and is_valid_dob(record['dob']):
        data['records'].append(record)
        logger.info("Record created successfully")
        return True
    else:
        logger.error("Record creation failed due to invalid data")
        return False

def read_records():
    """
    Read all records.

    Returns:
        list: List of all records.
    """
    logger.info("Reading all records")
    return data['records']

def update_record(mobile, updated_record):
    """
    Update an existing record by mobile number.

    Args:
        mobile (int): Mobile number of the record to update.
        updated_record (dict): Dictionary containing updated record data.

    Returns:
        bool: True if record is updated successfully, False otherwise.
    """
    for record in data['records']:
        if record['mobile'] == mobile:
            record.update(updated_record)
            logger.info(f"Record with mobile {mobile} updated successfully")
            return True
    logger.error(f"Record with mobile {mobile} not found")
    return False

def delete_record(mobile):
    """
    Delete a record by mobile number.

    Args:
        mobile (int): Mobile number of the record to delete.

    Returns:
        bool: True if record is deleted successfully, False otherwise.
    """
    for record in data['records']:
        if record['mobile'] == mobile:
            data['records'].remove(record)
            logger.info(f"Record with mobile {mobile} deleted successfully")
            return True
    logger.error(f"Record with mobile {mobile} not found")
    return False
