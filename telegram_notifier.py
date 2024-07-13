import requests
import logging
from typing import Optional

class TelegramNotifier:
    """
    A class to send notifications to a Telegram chat.
    """

    def __init__(self, token_id: str, chat_id: str, logger: Optional[logging.Logger] = None):
        """
        Initializes the TelegramNotifier.

        Args:
            token_id (str): The token ID of the Telegram bot.
            chat_id (str): The chat ID to send messages to.
            logger (Optional[logging.Logger]): A logger instance for logging messages. Defaults to None.
        """
        self.token_id = token_id
        self.chat_id = chat_id
        self.logger = logger or logging.getLogger(__name__)

    def handle_logging(self, level: int, message: str) -> None:
        """
        Handles logging or printing messages based on the availability of a logger.

        Args:
            level (int): The log level for the message.
            message (str): The message to log or print.
        """
        if self.logger:
            self.logger.log(level, message)
        else:
            print(message)

    def send_notification(self, msg_title: str, msg: str) -> None:
        """
        Sends a notification to the specified Telegram chat.

        Args:
            msg_title (str): The title of the message.
            msg (str): The body of the message.
        """
        post_msg = "Your faithful employee,\nTeleUPS"
        full_msg = f"<b>{msg_title}</b>\n\n{msg}\n\n<b>{post_msg}</b>"
        payload = {
            'chat_id': self.chat_id,
            'text': full_msg,
            'parse_mode': 'HTML'
        }
        url = f"https://api.telegram.org/bot{self.token_id}/sendMessage"
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            self.handle_logging(logging.INFO, "Telegram notification has been sent successfully")
        except requests.exceptions.RequestException as e:
            self.handle_logging(logging.ERROR, f"Failed to send Telegram notification: {e}")
