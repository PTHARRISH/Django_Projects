from django.utils.timezone import now
from .mongo import login_events


def log_login_event(user, request, status="success"):
    ip = get_client_ip(request)
    user_agent = request.META.get("HTTP_USER_AGENT", "")
    
    login_events.insert_one({
        "user_id": str(user.id),
        "username": user.username,
        "login_time": now(),
        "ip_address": ip,
        "user_agent": user_agent,
        "status": status
    })

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]
    return request.META.get("REMOTE_ADDR")
