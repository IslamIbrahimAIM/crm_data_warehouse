import pandas as pd
import numpy as np
from faker import Faker
import random
import uuid
import os
from datetime import datetime, timedelta

####################### OUTPUT ##########################

OUTPUT_DIR = "dummy_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save(df, filename):
    df.to_csv(os.path.join(OUTPUT_DIR, filename), index=False)
    print(f"✔ {filename}")

####################### INIT ##########################

fake = Faker("en_US")
Faker.seed(42)
random.seed(42)
np.random.seed(42)

####################### VOLUMES ##########################

N_USERS = 50_000
N_ORDERS = 120_000
N_DEVICES = 20_000
N_EVENTS = 1_000_000
N_GEO = 10_000
N_PROMOTIONS = 500
N_REDEMPTIONS = 4_000
N_REFERRALS = 3_000
N_PREFERENCES = 20_000
N_STATUS_HISTORY = 250_000
N_PAYMENT_ATTEMPTS = 80_000
N_MARKETING_COST = 365
N_ATTRIBUTION = 80_000


####################### HELPERS ##########################

def sometimes_null(v, p=0.1):
    return v if random.random() > p else None

def messy_text(t):
    if random.random() < 0.05:
        return t.upper()
    if random.random() < 0.05:
        return t.lower()
    if random.random() < 0.03:
        return t + "??"
    return t

def random_date_backwards(days_back):
    end = datetime.now() - timedelta(days=1)
    start = end - timedelta(days=days_back)
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

####################### UAE CITY BOUNDS ##########################

UAE_CITY_BOUNDS = {
    "Dubai": {"lat": (24.98, 25.35), "lon": (55.08, 55.56)},
    "Abu Dhabi": {"lat": (24.20, 24.65), "lon": (54.30, 54.75)},
    "Sharjah": {"lat": (25.25, 25.42), "lon": (55.35, 55.52)},
    "Ajman": {"lat": (25.35, 25.46), "lon": (55.43, 55.62)},
    "Al Ain": {"lat": (24.00, 24.35), "lon": (55.60, 55.90)},
    "Ras Al Khaimah": {"lat": (25.60, 25.90), "lon": (55.75, 56.10)},
    "Fujairah": {"lat": (25.05, 25.30), "lon": (56.20, 56.42)}
}
CITIES = list(UAE_CITY_BOUNDS.keys())

def faker_lat_lon(city):
    b = UAE_CITY_BOUNDS[city]
    return (
        fake.pyfloat(min_value=b["lat"][0], max_value=b["lat"][1], right_digits=6),
        fake.pyfloat(min_value=b["lon"][0], max_value=b["lon"][1], right_digits=6)
    )

####################### DIRTY ENUMS ##########################


order_statuses = [
    "completed", "complete", "done",
    "pending",
    "cancelled", "canceled",
    "in_progress"
]

order_status_history = [
    "pending", "confirmed",
    "in_progress", "IN_PROGRESS",
    "completed", "COMPLETE",
    "cancelled", "canceled"
]

products = [
    "Shirt", "Pants", "Jacket", "Socks",
    "Dress", "Abaya", "Hoodie",
    "Towel", "Blanket"
]

payment_providers = [
    "stripe", "STRIPE", "stripee",
    "tap", "Tap",
    "cash",
    "apple_pay"
]

event_types = [
    "app_open", "open", "OPEN_APP",
    "signup", "signup_started",
    "order_start", "ORDER_COMPLETED",
    "view", "VIEW_PAGE"
]

platforms = [
    "iOS", "ios", "Iphone", "APPLE",
    "Android", "ANDROIDD",
    "web", "Web", "WEB"
]

####################### USERS ##########################


users = []
for _ in range(N_USERS):
    users.append([
        str(uuid.uuid4())[:8],
        messy_text(fake.name()),
        sometimes_null(fake.email(), 0.07),
        messy_text(f"+9715{random.randint(10000000,99999999)}"),
        random_date_backwards(1095).strftime("%Y-%m-%d"),
        random.choice(["active","inactive","blocked","BLOCKED"]),
        messy_text(random.choice(CITIES)),
        sometimes_null(fake.street_address(),0.15)
    ])

df_users = pd.DataFrame(users, columns=[
    "user_id","full_name","email","phone",
    "signup_date","status","city_raw","address_raw"
])
save(df_users, "raw_users.csv")


####################### GEO ##########################

geo = []
for _ in range(N_GEO):
    city = random.choice(CITIES)
    lat, lon = faker_lat_lon(city)
    geo.append([
        messy_text(city),
        messy_text(random.choice(["UAE","United Arab Emirates","uae","U.A.E"])),
        sometimes_null(lat,0.05),
        sometimes_null(lon,0.05)
    ])

df_geo = pd.DataFrame(geo, columns=[
    "city_raw","country_raw","latitude","longitude"
])
save(df_geo, "raw_geo.csv")


####################### ORDERS ##########################

orders = []
for _ in range(N_ORDERS):
    orders.append([
        str(uuid.uuid4())[:8],
        random.choice(df_users["user_id"]),
        random.choice([
            random_date_backwards(730).strftime("%Y-%m-%d %H:%M:%S"),
            random_date_backwards(730).strftime("%d/%m/%Y %H:%M"),
            random_date_backwards(730).strftime("%b %d %Y %H:%M")
        ]),
        random.choice(order_statuses),
        random.choice(payment_providers)
    ])

df_orders = pd.DataFrame(orders, columns=[
    "order_id","user_id","created_at","order_status","payment_provider"
])


####################### ORDER ITEMS ##########################

items = []
for oid in df_orders["order_id"]:
    for _ in range(random.randint(1,5)):
        qty = random.randint(1,3)
        price = round(random.uniform(15,300),2)
        items.append([
            str(uuid.uuid4())[:8],
            oid,
            messy_text(random.choice(products)),
            qty,
            price,
            round(qty*price,2)
        ])

df_items = pd.DataFrame(items, columns=[
    "order_item_id","order_id","product_name",
    "qty","unit_price","line_total"
])
save(df_items, "raw_order_items.csv")

# totals
totals = df_items.groupby("order_id")["line_total"].sum().reset_index()
df_orders = df_orders.merge(totals, on="order_id", how="left")
save(df_orders, "raw_orders.csv")

####################### DEVICES ##########################

devices = []
for _ in range(N_DEVICES):
    devices.append([
        str(uuid.uuid4())[:10],
        random.choice(df_users["user_id"]),
        messy_text(random.choice(platforms)),
        messy_text(fake.user_agent()),
        sometimes_null(fake.mac_address(),0.2)
    ])

df_devices = pd.DataFrame(devices, columns=[
    "device_id","user_id","platform","device_model","mac_addr"
])
save(df_devices, "raw_devices.csv")


####################### EVENTS ##########################

events = []
device_ids = df_devices["device_id"].tolist()
for _ in range(N_EVENTS):
    ts = random_date_backwards(365)
    events.append([
        str(uuid.uuid4()),
        random.choice(df_users["user_id"]),
        random.choice(event_types),
        random.choice([
            ts.strftime("%Y-%m-%d %H:%M:%S"),
            ts.strftime("%d/%m/%Y %H:%M"),
            ts.strftime("%b %d %Y %H:%M")
        ]),
        random.choice(device_ids) if random.random()<0.85 else None
    ])

df_events = pd.DataFrame(events, columns=[
    "event_id","user_id","event_type","event_ts","device_id"
])
save(df_events, "raw_events.csv")


####################### PROMOTIONS ##########################

promo=[]
for i in range(N_PROMOTIONS):
    promo.append([
        f"PROMO{i:04d}",
        random.choice([5,10,15,20,25,30]),
        random_date_backwards(540),
        random_date_backwards(90)
    ])
df_promo = pd.DataFrame(promo, columns=[
    "promotion_code","discount_pct","valid_from","valid_to"
])
save(df_promo, "raw_promotions.csv")


####################### COUPON REDEMPTIONS ##########################

red=[]
for _ in range(N_REDEMPTIONS):
    red.append([
        str(uuid.uuid4()),
        random.choice(df_users["user_id"]),
        random.choice(df_promo["promotion_code"]),
        random.choice(df_orders["order_id"]),
        random_date_backwards(365)
    ])
save(pd.DataFrame(red, columns=[
    "redemption_id","user_id","promotion_code","order_id","redeemed_ts"
]), "raw_coupon_redemptions.csv")


####################### REFERRALS ##########################

uids = df_users["user_id"].tolist()
ref=[]
for _ in range(N_REFERRALS):
    u1,u2 = random.sample(uids,2)
    ref.append([str(uuid.uuid4()),u1,u2,random_date_backwards(365)])
save(pd.DataFrame(ref, columns=[
    "referral_id","referrer_user_id","referred_user_id","referral_ts"
]), "raw_referrals.csv")


####################### USER PREFERENCES ##########################

prefs=[]
for _ in range(N_PREFERENCES):
    prefs.append([
        str(uuid.uuid4()),
        random.choice(uids),
        random.choice(["notifications","language","offers"]),
        random.choice(["yes","no","en","ar","EN"]),
        random_date_backwards(365)
    ])
save(pd.DataFrame(prefs, columns=[
    "pref_id","user_id","pref_key","pref_value","updated_ts"
]), "raw_user_preferences.csv")


####################### ORDER STATUS HISTORY ##########################

hist=[]
for _ in range(N_STATUS_HISTORY):
    hist.append([
        str(uuid.uuid4()),
        random.choice(df_orders["order_id"]),
        random.choice(order_status_history),
        random_date_backwards(730)
    ])
save(pd.DataFrame(hist, columns=[
    "id","order_id","status","changed_ts"
]), "raw_order_status_history.csv")


####################### PAYMENT ATTEMPTS ##########################

attempts=[]
for _ in range(N_PAYMENT_ATTEMPTS):
    attempts.append([
        str(uuid.uuid4()),
        random.choice(df_orders["order_id"]),
        random.choice(payment_providers),
        round(random.uniform(20,500),2),
        random.choice([0,1]),
        random_date_backwards(540)
    ])
save(pd.DataFrame(attempts, columns=[
    "attempt_id","order_id","provider","amount_attempted","success","attempt_ts"
]), "raw_payment_attempts.csv")


####################### MARKETING COST ##########################

mc=[]
start = datetime.now() - timedelta(days=N_MARKETING_COST)
for i in range(N_MARKETING_COST):
    mc.append([
        str(uuid.uuid4()),
        random.choice(["facebook","google","tiktok","snapchat","email","EMAIL"]),
        round(random.uniform(100,5000),2),
        start + timedelta(days=i)
    ])
save(pd.DataFrame(mc, columns=[
    "spend_id","channel","spend","spend_date"
]), "raw_marketing_cost.csv")


####################### ATTRIBUTION ##########################


attrib=[]
for _ in range(N_ATTRIBUTION):
    attrib.append([
        str(uuid.uuid4()),
        random.choice(uids),
        random.choice(["facebook","google","tiktok","snapchat","email","EMAIL"]),
        fake.word(),
        random.choice(["paid","organic","referral","REFERRAL"]),
        random.choice(["fb","google","direct","email","EMAIL"]),
        random_date_backwards(365)
    ])
save(pd.DataFrame(attrib, columns=[
    "attrib_id","user_id","channel","campaign","medium","source","touch_ts"
]), "raw_marketing_attribution.csv")

print("\n🔥 ALL 14 FILES GENERATED — MESSY BRONZE DATA (AS INTENDED) 🔥")
