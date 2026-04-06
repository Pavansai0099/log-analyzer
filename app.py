import streamlit as st
import matplotlib.pyplot as plt

st.title("AI Log Analyzer")

# Upload file
uploaded_file = st.file_uploader("Upload your log file", type=["txt"])

if uploaded_file is not None:
    logs = uploaded_file.read().decode("utf-8").splitlines()

    error_count = 0
    warning_count = 0
    info_count = 0

    for log in logs:
        if "ERROR" in log:
            error_count += 1
        elif "WARNING" in log:
            warning_count += 1
        elif "INFO" in log:
            info_count += 1

    # Show results
    st.subheader("Results")
    st.write("Errors:", error_count)
    st.write("Warnings:", warning_count)
    st.write("Info:", info_count)

    # Plot graph
    labels = ['Errors', 'Warnings', 'Info']
    values = [error_count, warning_count, info_count]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Log Analysis")

    st.pyplot(fig)