import os


class Config:
    def __init__(self):
        # Основные настройки сервиса
        self.environment = os.getenv("ENVIRONMENT", "dev")
        self.service_name = os.getenv("KONTUR_ORGANIZATION_CONTAINER_NAME", "kontur-employee")
        self.http_port = os.getenv("KONTUR_ORGANIZATION_PORT", "8000")
        self.service_version = os.getenv("SERVICE_VERSION", "1.0.0")
        self.root_path = os.getenv("ROOT_PATH", "/")
        self.prefix = os.getenv("KONTUR_ORGANIZATION_PREFIX", "/api/employee")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

        # Настройки базы данных PostgreSQL
        self.db_host = os.getenv("KONTUR_ORGANIZATION_POSTGRES_CONTAINER_NAME", "localhost")
        self.db_port = os.getenv("KONTUR_ORGANIZATION_POSTGRES_PORT", "5432")
        self.db_name = os.getenv("KONTUR_ORGANIZATION_POSTGRES_DB_NAME", "hr_interview")
        self.db_user = os.getenv("KONTUR_ORGANIZATION_POSTGRES_USER", "postgres")
        self.db_pass = os.getenv("KONTUR_ORGANIZATION_POSTGRES_PASSWORD", "password")

        # Настройки телеметрии
        self.alert_tg_bot_token = os.getenv("KONTUR_ALERT_TG_BOT_TOKEN", "")
        self.alert_tg_chat_id = os.getenv("KONTUR_ALERT_TG_CHAT_ID", "")
        self.alert_tg_chat_thread_id = os.getenv("KONTUR_ALERT_TG_CHAT_THREAD_ID", "")
        self.grafana_url = os.getenv("KONTUR_GRAFANA_URL", "")

        self.monitoring_redis_host = os.getenv("KONTUR_MONITORING_REDIS_CONTAINER_NAME", "localhost")
        self.monitoring_redis_port = int(os.getenv("KONTUR_MONITORING_REDIS_PORT", "6379"))
        self.monitoring_redis_db = int(os.getenv("KONTUR_MONITORING_DEDUPLICATE_ERROR_ALERT_REDIS_DB", "0"))
        self.monitoring_redis_password = os.getenv("KONTUR_MONITORING_REDIS_PASSWORD", "")

        # Настройки OpenTelemetry
        self.otlp_host = os.getenv("KONTUR_OTEL_COLLECTOR_CONTAINER_NAME", "kontur-otel-collector")
        self.otlp_port = int(os.getenv("KONTUR_OTEL_COLLECTOR_GRPC_PORT", "4317"))

        # Настройки клиента авторизации Kontur
        self.kontur_authorization_host = os.getenv("KONTUR_AUTHORIZATION_CONTAINER_NAME", "localhost")
        self.kontur_authorization_port = int(os.getenv("KONTUR_AUTHORIZATION_PORT", "8081"))