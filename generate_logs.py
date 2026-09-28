import random
import uuid
from datetime import datetime, timedelta

def generate_enterprise_log_file(filename="server_logs.txt", num_lines=5000):
    log_levels = ["INFO", "INFO", "INFO", "WARNING", "ERROR", "CRITICAL"]
    components = [
        "AuthService.Login", 
        "PaymentGateway.Process", 
        "CourierTracking.UpdateLocation", 
        "CouponEngine.Redeem", 
        "Database.ConnectionPool"
    ]
    error_messages = {
        "ERROR": [
            "Database connection timeout after 3000ms.",
            "Failed to authorize payment token verification.",
            "Courier tracking sync failed with mobile client.",
            "CORS policy restriction blocked incoming frontend origin."
        ],
        "CRITICAL": [
            "Thread deadlock detected inside internal memory engine!",
            "Out of memory space allocation failure in connection pool.",
            "Payment transaction logged database write failure, rollback triggered!"
        ],
        "WARNING": [
            "Slow query execution detected on coupon cache lookup.",
            "High CPU usage spike over 85% on thread pool.",
            "API request payload size limits approaching max boundary."
        ]
    }
    info_messages = [
        "User authentication sequence completed successfully.",
        "Payload data model validated across internal channel.",
        "State tracking model synchronized back to main cache.",
        "Connection token refreshed inside connection context lifecycle."
    ]
    start_time = datetime.utcnow() - timedelta(days=1)
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(num_lines):
            log_time = start_time + timedelta(seconds=i * random.randint(1, 10))
            time_str = log_time.strftime("%Y-%m-%d %H:%M:%S")
            level = random.choice(log_levels)
            component = random.choice(components)
            request_id = str(uuid.uuid4())[:8]
            if level in ["ERROR", "CRITICAL", "WARNING"]:
                msg = random.choice(error_messages[level])
            else:
                msg = random.choice(info_messages)
            log_line = f"[{time_str}] [{level}] [{component}] [ReqID:{request_id}] - {msg}\n"
            file.write(log_line)

if __name__ == "__main__":
    generate_enterprise_log_file()
