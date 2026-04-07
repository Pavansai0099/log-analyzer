import streamlit as st
import matplotlib.pyplot as plt

# 🤖 AI Imports
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

st.title("AI Log Analyzer")

# =========================
# 🤖 AI MODEL (Training)
# =========================
texts = [
    "database failed",
    "disk space low",
    "user login",
    "timeout error",
    "cpu high",
    "service crashed",
    "system failure",
    "restart failed",
    "memory warning",
    "user logout",
    "invalid input error",
    "connection lost"
]

labels_train = [
    "ERROR",
    "WARNING",
    "INFO",
    "ERROR",
    "WARNING",
    "CRITICAL",
    "CRITICAL",
    "ERROR",
    "WARNING",
    "INFO",
    "ERROR",
    "ERROR"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels_train)

# =========================
# 📂 FILE UPLOAD
# =========================
uploaded_file = st.file_uploader("Upload your log file", type=["txt", "log"])

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

    # =========================
    # 📊 RESULTS
    # =========================
    st.subheader("Results")
    st.write("Errors:", error_count)
    st.write("Warnings:", warning_count)
    st.write("Info:", info_count)

    # =========================
    # 📊 PIE CHART
    # =========================
    labels = ['Errors', 'Warnings', 'Info']
    values = [error_count, warning_count, info_count]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Log Distribution")

    st.pyplot(fig)

    # =========================
    # 🔍 SEARCH LOGS
    # =========================
    st.subheader("Search Logs")

    search = st.text_input("Enter keyword")

    if search:
        results = [log for log in logs if search.lower() in log.lower()]
        for r in results:
            st.write(r)

    # =========================
    # 📄 DOWNLOAD REPORT
    # =========================
    report = f"""
Errors: {error_count}
Warnings: {warning_count}
Info: {info_count}
"""

    st.download_button("Download Report", report, file_name="report.txt")

# =========================
# 🤖 AI PREDICTION
# =========================
st.subheader("AI Log Prediction")

user_input = st.text_input("Enter a log message")

if user_input:
    test_vec = vectorizer.transform([user_input])
    prediction = model.predict(test_vec)
    st.write("Predicted Type:", prediction[0])