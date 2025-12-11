
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from bbb_model import (
    size_window_curve,
    corona_tiny_curve,
    corona_mid_curve,
    corona_large_curve,
    compute_probability_only_size
)

st.set_page_config(page_title="Size-Only BBB Model v4", layout="wide")

st.title("Nanoplastic Size-Dependent BBB Modeling")

size_nm = st.slider("Nanoplastic Particle Size (nm)", 1.0, 500.0, 80.0, 1.0)
prob = compute_probability_only_size(size_nm)

st.subheader("Modeled Probability for ApoE3-mediated BBB Crossing")
st.metric("Estimated Probability", f"{prob*100:.1f}%")

sizes = np.linspace(1,500,500)

# === GRAPH 1 ===
fig1, ax1 = plt.subplots()
ax1.plot(sizes, size_window_curve(sizes))
ax1.set_xlabel("Nanoplastic Particle Size (nm)")
ax1.set_ylabel("Probability (0–1)")
ax1.set_title("Modeled Probability for ApoE3-mediated BBB Crossing")
ax1.axvline(size_nm, linestyle="--")
st.pyplot(fig1)

# === CORONA GRAPHS ===
st.header("Predicted ApoE3 Corona Stability Across Nanoplastic Sizes")

# tiny
fig2a, ax2a = plt.subplots()
ax2a.plot(sizes, corona_tiny_curve(sizes))
ax2a.set_title("Corona Formation: Very Tiny Particles (<10 nm) – Minimal Binding")
ax2a.set_xlabel("Nanoplastic Size (nm)")
ax2a.set_ylabel("Corona Likelihood (0–1)")
st.pyplot(fig2a)

# mid
fig2b, ax2b = plt.subplots()
ax2b.plot(sizes, corona_mid_curve(sizes))
ax2b.set_title("Corona Formation: Mid-Sized Particles (50–150 nm) – Strong Binding")
ax2b.set_xlabel("Nanoplastic Size (nm)")
ax2b.set_ylabel("Corona Likelihood (0–1)")
st.pyplot(fig2b)

# large
fig2c, ax2c = plt.subplots()
ax2c.plot(sizes, corona_large_curve(sizes))
ax2c.set_title("Corona Formation: Large Particles (>200 nm) – Weak/Unstable Binding")
ax2c.set_xlabel("Nanoplastic Size (nm)")
ax2c.set_ylabel("Corona Likelihood (0–1)")
st.pyplot(fig2c)
