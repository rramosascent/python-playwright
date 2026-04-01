import logging
import os
import sys
from datetime import datetime
from loguru import logger

class CustomLogger:
    @staticmethod
    def setup_logging():
        # Remove default loguru handler
        logger.remove()
        
        # Create logs directory if it doesn't exist
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        
        # Add a file handler
        logger.add(
            log_file,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level="INFO",
            rotation="10 MB",
            retention="10 days"
        )
        
        # Add a console handler
        logger.add(
            sys.stderr,
            format="<green>\n{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>",
            level="INFO"
        )
        
        return logger

# Globally available logger instance
log = logger
