import uvicorn
from config import api_settings


def main():
    # app_logger.info("FastAPI starting...")
    print("FastAPI starting...")
    uvicorn.run(
        'api.main:app',
        host=api_settings.HOST,
        port=api_settings.PORT,
        reload=api_settings.RELOAD,
        workers=api_settings.WORKERS,
        log_level='debug',
    )


if __name__ == "__main__":
    main()
    print("FastAPI ending...")
