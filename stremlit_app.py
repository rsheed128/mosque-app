st.set_page_config(page_title="جامع التويجري", page_icon="🕌", layout="centered")

# تصميم الألوان الفخمة عبر HTML و CSS مدمج
st.markdown(
    """
    <style>
    .main { background-color: #0b0f19; }
    .header-box {
        background-color: #131a26;
        border: 2px solid #eab308;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
    }
    .header-title { color: #eab308; font-size: 24px; font-weight: bold; margin: 0; }
    .header-sub { color: #94a3b8; font-size: 14px; margin: 5px 0 0 0; }
    
    .clock-box {
        background-color: #131a26;
        border: 1px solid #ffcc00;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .clock-time { color: #00ffcc; font-size: 40px; font-weight: bold; font-family: 'Courier New', monospace; }
    .clock-date { color: #94a3b8; font-size: 14px; margin-top: 5px; }
    
    .prayer-card {
        background-color: #131a26;
        border: 1px solid #eab308;
        border-radius: 8px;
        padding: 12px 20px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .active-card {
        background-color: #eab308;
        border: 1px solid #ffcc00;
        border-radius: 8px;
        padding: 12px 20px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .prayer-name { font-size: 18px; font-weight: bold; }
    .prayer-time { font-size: 16px; font-weight: bold; }
    
    .info-box {
        background-color: #131a26;
        border: 1px solid #ffcc00;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        margin-top: 10px;
    }
    .info-title { color: #eab308; font-size: 14px; font-weight: bold; }
    .info-val { color: #ffffff; font-size: 20px; font-weight: bold; }
    .info-val-active { color: #ef4444; font-size: 20px; font-weight: bold; }
    
    .adv-box {
        background-color: #1e293b;
        border: 1px solid #ffcc00;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        margin-top: 15px;
        color: #34d399;
        font-size: 13px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_stdio=True,
    unsafe_allow_html=True,
)

PRAYER_DATA = [
    {"name": "الفجر", "hour": 3, "minute": 48, "iqama": 27},
    {"name": "الشروق", "hour": 5, "minute": 19, "iqama": 15},
    {"name": "الظهر", "hour": 12, "minute": 10, "iqama": 20},
    {"name": "العصر", "hour": 15, "minute": 37, "iqama": 20},
    {"name": "المغرب", "hour": 19, "minute": 1, "iqama": 12},
    {"name": "العشاء", "hour": 20, "minute": 31, "iqama": 15},
]

# ترويسة الجامع
st.markdown(
    '<div class="header-box"><div class="header-title">جامع علي عبدالعزيز التويجري</div><div class="header-sub">بريدة - المملكة العربية السعودية</div></div>',
    unsafe_allow_html=True,
)

# عرض الوقت والتاريخ الحالي
now = datetime.now()
ampm = "PM" if now.hour >= 12 else "AM"
display_hour = now.hour % 12
if display_hour == 0:
    display_hour = 12
time_str = f"{display_hour:02d}:{now.minute:02d}:{now.second:02d} {ampm}"

st.markdown(
    f'<div class="clock-box"><div class="clock-time">{time_str}</div><div class="clock-date">٢٧ محرم ١٤٤٨ هـ  |  ١٢ يوليو ٢٠٢٦ م</div></div>',
    unsafe_allow_html=True,
)

current_total_seconds = now.hour * 3600 + now.minute * 60 + now.second
current_total_minutes = now.hour * 60 + now.minute

active_idx = 0
for i, p in enumerate(PRAYER_DATA):
    if current_total_minutes < p["hour"] * 60 + p["minute"] + p["iqama"] + 60:
        active_idx = i
        break
