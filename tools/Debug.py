import logging
import subprocess
import time
from datetime import datetime
from pathlib import Path
import sys  # Добавляем для проверки ОС


class ClassG_Debug:
    _anyL_logProcess = None
    _strL_logFileTemplate = "logs/log-{time}.log"

    def __init__(self, boolT_enabled: bool = True):
        self.boolL_enabled = boolT_enabled
        self.anyL_logger = logging.getLogger(__name__)

        if not self.anyL_logger.handlers:
            self.noneT_SetupLogging()

        if ClassG_Debug._anyL_logProcess is None and self.boolL_enabled:
            self.noneT_CreateLogTerminal()
    @classmethod
    def pathT_GetLogFilepath(cls) -> Path:
        strT_dateStr = datetime.now().strftime("%y-%m-%d")
        strT_filename = cls._strL_logFileTemplate.replace("{time}", strT_dateStr)
        return Path(strT_filename)

    def noneT_SetupLogging(self) -> None:
        pathT_logFile = self.pathT_GetLogFilepath()
        pathT_logFile.parent.mkdir(parents=True, exist_ok=True)

        self.anyL_logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(pathT_logFile, encoding='utf-8')
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s | %(levelname)s: %(message)s', datefmt='%H:%M')
        )

        self.anyL_logger.addHandler(file_handler)

    def noneT_CreateLogTerminal(self) -> None:
        pathT_logPath = self.pathT_GetLogFilepath()

        try:
            ClassG_Debug._anyL_logProcess = subprocess.Popen(
                [
                    'powershell',
                    '-NoExit',
                    '-Command',
                    f'Get-Content "{pathT_logPath}" -Wait -Encoding UTF8'
                ],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            time.sleep(0.3)

        except Exception as anyT_error:
            self.anyL_logger.error(f"Failed to create terminal logs: {anyT_error}")

    @classmethod
    def noneG_CloseLogTerminal(cls) -> None:
        if cls._anyL_logProcess is not None:
            cls._anyL_logProcess.terminate()
            cls._anyL_logProcess = None

    def noneG_LogInfo(self, strT_message: str) -> None:
        self.anyL_logger.info(strT_message)

    def noneG_LogError(self, strT_message: str) -> None:
        self.anyL_logger.error(strT_message)

    def noneG_LogWarning(self, strT_message: str) -> None:
        self.anyL_logger.warning(strT_message)

    def noneG_LogDebug(self, strT_message: str) -> None:
        self.anyL_logger.debug(strT_message)