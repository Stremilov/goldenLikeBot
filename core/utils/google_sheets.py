import logging
import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")


def get_google_sheets_service():
    creds = Credentials.from_service_account_file(
        'credentials.json',
        scopes=SCOPES
    )
    service = build('sheets', 'v4', credentials=creds)
    return service


def append_comment_to_sheet(project_name: str, username: str, comment: str):
    service = get_google_sheets_service()

    sheet_number = project_name.split()[-1]
    sheet_name = f'Проект {sheet_number}'

    range_name = f'{sheet_name}!A:D'
    
    values = [[
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        project_name,
        username,
        comment
    ]]
    body = {
        'values': values
    }
    logging.info(values)
    
    try:
        logging.info("Оставляем коммент в таблице")
        response = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
        # logging.info(result)
        logging.info(f"Append response: {response}")

        logging.info("Коммент успешно оставлен")
    except Exception as e:

        if 'Unable to parse range' in str(e):

            batch_update_request = {
                'requests': [{
                    'addSheet': {
                        'properties': {
                            'title': sheet_name
                        }
                    }
                }]
            }

            logging.info("Подставка кредов")
            service.spreadsheets().batchUpdate(
                spreadsheetId=SPREADSHEET_ID,
                body=batch_update_request
            ).execute()

            logging.info("Подставка значений")
            headers = [['Дата и время', 'Название проекта', 'Пользователь', 'Комментарий']]
            service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=f'{sheet_name}!A1:D1',
                valueInputOption='RAW',
                body={'values': headers}
            ).execute()

            logging.info("Добавление комментария")
            service.spreadsheets().values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=range_name,
                valueInputOption='RAW',
                body=body
            ).execute()

            logging.info("Комментарий успешно сохранен везде")