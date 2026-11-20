"""Small web UI.   Run:  streamlit run app.py"""
import streamlit as st

from housing_utils import PRICE_UNIT
from predict import DEFAULTS, load, predict_price

st.set_page_config(page_title="California House Price Predictor", page_icon="🏠")
st.title("🏠 California House Price Predictor")
st.caption("Linear Regression trained on the California Housing dataset (1990 census, price in USD).")

which = st.radio("Model", ["baseline", "improved"], horizontal=True,
                 help="baseline = plain Linear Regression; improved = engineered features")
bundle = load(which)

c1, c2 = st.columns(2)
with c1:
    med_inc = st.slider("Median income (x $10,000)", 0.5, 15.0, DEFAULTS["MedInc"], 0.1)
    age = st.slider("House age (years)", 1, 52, int(DEFAULTS["HouseAge"]))
    rooms = st.slider("Avg rooms per household", 1.0, 15.0, DEFAULTS["AveRooms"], 0.1)
    bedrms = st.slider("Avg bedrooms per household", 0.5, 5.0, DEFAULTS["AveBedrms"], 0.05)
with c2:
    pop = st.number_input("Block population", 3, 35000, int(DEFAULTS["Population"]))
    occ = st.slider("Avg occupants per household", 0.5, 10.0, DEFAULTS["AveOccup"], 0.1)
    lat = st.slider("Latitude", 32.5, 42.0, DEFAULTS["Latitude"], 0.01)
    lon = st.slider("Longitude", -124.4, -114.3, DEFAULTS["Longitude"], 0.01)

if st.button("Predict price", type="primary"):
    price = predict_price(bundle, MedInc=med_inc, HouseAge=age, AveRooms=rooms, AveBedrms=bedrms,
                          Population=pop, AveOccup=occ, Latitude=lat, Longitude=lon)
    st.success(f"Estimated median house value: **${price:,.0f}**")
    mae = bundle.get("metrics", {}).get("mae")
    if mae:
        st.caption(f"Typical error of this model on unseen data (MAE): about ${mae * PRICE_UNIT:,.0f}")
