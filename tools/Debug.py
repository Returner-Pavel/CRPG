import logging
import subprocess
import time
from datetime import datetime
from pathlib import Path

class ClassG_Debug:
    _anyL_logProcess = None
    _strL_logFileTemplate = "logs/logs-{time}.txt"

    def __init__(self, boolT_enabled: bool = True):
        self.boolL_enabled = boolT_enabled
        self.anyL_logger = logging.getLogger(__name__)

        if ClassG_Debug._anyL_logProcess is None and self.boolL_enabled:
            self.noneL_SetupLogging()
            self.noneL_CreateLogTerminal()

    @classmethod
    def pathG_GetLogFilepath(cls) -> Path:
        strT_dateStr = datetime.now().strftime("%y-%m-%d")
        strT_filename = cls._strL_logFileTemplate.replace("{time}", strT_dateStr)
        return Path(strT_filename)

    def noneL_SetupLogging(self) -> None:
        pathT_logFile = self.pathG_GetLogFilepath()

        pathT_logFile.parent.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(pathT_logFile, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )

    def noneL_CreateLogTerminal(self) -> None:
        pathT_logPath = self.pathG_GetLogFilepath()

        pathT_logPath.parent.mkdir(parents=True, exist_ok=True)

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
            self.anyL_logger.error(f"Не удалось создать терминал логов: {anyT_error}")

    @classmethod
    def noneG_CloseLogTerminal(cls) -> None:
        if cls._anyL_logProcess is not None:
            cls._anyL_logProcess.terminate()
            cls._anyL_logProcess = None

    # Вот это вам надо, выше не нужно

    def noneL_LogInfo(self, strT_message: str) -> None:
        if self.boolL_enabled:
            self.anyL_logger.info(strT_message)

    def noneL_LogError(self, strT_message: str) -> None:
        if self.boolL_enabled:
            self.anyL_logger.error(strT_message)

    def noneL_LogWarning(self, strT_message: str) -> None:
        if self.boolL_enabled:
            self.anyL_logger.warning(strT_message)

    def noneL_LogDebug(self, strT_message: str) -> None:
        if self.boolL_enabled:
            self.anyL_logger.debug(strT_message)

