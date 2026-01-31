import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------------------------------
# Basic Researcher Information
# -----------------------------------------------------------

st.title("🥼 RESEARCHER PROFILE")


name = "Ndivhuwo Thizwilondi"
field = "Animal Science – Reproductive Physiology & Metabolomics"
position = "MSc Candidate"
institution = "Tshwane University of Technology"
research_topic = (
    "Identification of sperm metabolites from sex-sorted and non-sorted semen "
    "as biomarkers for fertility in dairy bulls"
)

st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Position:** {position}")
st.write(f"**Field:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Research Topic:** {research_topic}")

# -----------------------------------------------------------
# Upload: Sperm or Metabolomics Dataset
# -----------------------------------------------------------

st.header("Upload Research Data")

uploaded_data = st.file_uploader(
    "Upload a CSV file containing sperm parameters or metabolomics features", 
    type="csv"
)

if uploaded_data:
    df = pd.read_csv(uploaded_data)
    st.subheader("Raw Dataset Preview")
    st.dataframe(df)

    # Keyword search
    keyword = st.text_input("Search dataset by keyword", "")
    if keyword:
        filtered = df[
            df.apply(
                lambda r: keyword.lower() in r.astype(str).str.lower().values,
                axis=1
            )
        ]
        st.write(f"Search Results for '{keyword}':")
        st.dataframe(filtered)

# -----------------------------------------------------------
# Publication Section
# -----------------------------------------------------------

st.header("Publications")
pub_file = st.file_uploader("Upload publication list (CSV)", type="csv")

if pub_file:
    pubs = pd.read_csv(pub_file)
    st.dataframe(pubs)

    if "Year" in pubs.columns:
        st.subheader("Publication Trend")
        year_counts = pubs["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("No 'Year' column found for trend analysis.")

# -----------------------------------------------------------
# Domain-Specific STEM Data: Animal Science Datasets
# -----------------------------------------------------------

st.header("Animal Science Data Explorer")

datasets = {
    "Semen Quality (Example)": pd.DataFrame({
        "Bull ID": [101, 102, 103, 104],
        "Motility (%)": [85, 76, 91, 88],
        "Concentration (mil/mL)": [1200, 980, 1500, 1100],
        "Morphology (%)": [92, 88, 95, 90]
    }),

    "Fertility Scores (Example)": pd.DataFrame({
        "Bull ID": [101, 102, 103, 104],
        "Pregnancy Rate (%)": [48, 39, 55, 50],
        "Services per Conception": [1.7, 2.1, 1.4, 1.6]
    }),

    "Metabolomics (Dummy Features)": pd.DataFrame({
        "Feature": [f"m/z_{i}" for i in range(1, 11)],
        "Retention Time (min)": np.round(np.random.uniform(1, 20, 10), 2),
        "Intensity": np.random.randint(10000, 90000, 10)
    })
}

selection = st.selectbox("Choose dataset:", list(datasets.keys()))
st.dataframe(datasets[selection])

# Optional Filters
if selection == "Semen Quality (Example)":
    mot_filter = st.slider("Filter by Motility (%)", 0, 100, (0, 100))
    filtered = datasets[selection][
        datasets[selection]["Motility (%)"].between(mot_filter[0], mot_filter[1])
    ]
    st.write("Filtered Semen Quality:")
    st.dataframe(filtered)

elif selection == "Metabolomics (Dummy Features)":
    intensity_filter = st.slider("Filter by Intensity", 0, 100000, (0, 100000))
    filtered = datasets[selection][
        datasets[selection]["Intensity"].between(intensity_filter[0], intensity_filter[1])
    ]
    st.write("Filtered Metabolomics Features:")
    st.dataframe(filtered)

# -----------------------------------------------------------
# Contact Section
# -----------------------------------------------------------

st.header("Contact")
st.write("📧 Email: nthizwilondi6@gmail.com") 
